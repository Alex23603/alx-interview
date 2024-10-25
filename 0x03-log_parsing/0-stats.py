#!/usr/bin/python3
import sys
import signal

# Initialize tracking variables
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
    """Parse a single log line and update the metrics if the format matches."""
    global total_file_size
    try:
        parts = line.split()
        # Ensure the log format has a file size and status code as the last two parts
        status_code = parts[-2]
        file_size = int(parts[-1])
        
        # Update total file size
        total_file_size += file_size
        
        # Update count for valid status codes
        if status_code in status_counts:
            status_counts[status_code] += 1
    except (IndexError, ValueError):
        # Ignore lines that don't match expected format or have invalid data
        pass

def signal_handler(sig, frame):
    """Handle keyboard interrupt to print metrics before exiting."""
    print_metrics()
    sys.exit(0)

# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Read and process each line from standard input
try:
    for line in sys.stdin:
        parse_log_line(line.strip())
        line_count += 1
        
        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)

# Print final metrics when the input stream ends
print_metrics()

