#!/usr/bin/python3
import sys
import signal

# Initialize tracking variables
file_size = 0
status_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0, 
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

def print_metrics():
    """ Print the accumulated metrics """
    print(f"File size: {file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """Parse a single line of log and update metrics."""
    global file_size
    try:
        # Split line and extract required parts
        parts = line.split()
        if len(parts) < 7:
            return
        # Extract status code and file size
        status_code = parts[-2]
        size = int(parts[-1])
        
        # Update file size
        file_size += size
        
        # Update status code count if it's a valid code
        if status_code in status_counts:
            status_counts[status_code] += 1
    except (IndexError, ValueError):
        pass  # Ignore lines that don't match the expected format

def signal_handler(sig, frame):
    """ Handle keyboard interrupt to print metrics before exiting """
    print_metrics()
    sys.exit(0)

# Register signal handler for graceful exit
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    parse_line(line.strip())
    line_count += 1
    
    # Print metrics every 10 lines
    if line_count % 10 == 0:
        print_metrics()

# Print final metrics when input ends
print_metrics()
