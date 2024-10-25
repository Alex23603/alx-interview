#!/usr/bin/python3
import sys
import signal

# Initialize counters for file size and status codes
total_file_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

def print_metrics():
    """Print the accumulated metrics for total file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_log_line(line):
    """Parse a single log line, update the metrics if format matches, and handle errors."""
    global total_file_size
    try:
        # Split log line by whitespace and confirm it has the expected length
        parts = line.split()
        if len(parts) < 2:
            return
        
        # Extract status code and file size (last two elements)
        status_code = parts[-2]
        file_size = int(parts[-1])
        
        # Increment the total file size
        total_file_size += file_size
        
        # Update status code count if the code is valid
        if status_code in status_counts:
            status_counts[status_code] += 1
    except (IndexError, ValueError):
        # Skip the line if format is invalid
        pass

def signal_handler(sig, frame):
    """Handle keyboard interruption and print metrics before exiting."""
    print_metrics()
    sys.exit(0)

# Register signal handler for keyboard interrupt (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

# Read lines from standard input
try:
    for line in sys.stdin:
        parse_log_line(line.strip())
        line_count += 1
        
        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    # Print metrics on keyboard interrupt
    print_metrics()
    sys.exit(0)

# Print final metrics at the end of input
print_metrics()

