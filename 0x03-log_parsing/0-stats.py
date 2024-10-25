#!/usr/bin/python3
import sys

def print_stats(file_size, status_codes):
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        # Ensure valid log entry format (IP - [date] "GET ..." <status code> <file size>)
        if len(parts) < 7:
            continue
        
        # Extract status code and file size
        try:
            status_code = int(parts[-2])
            file_size += int(parts[-1])

            # Update status code count if it's valid
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            continue
        
        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats(file_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    # Print stats upon interruption
    print_stats(file_size, status_codes)
