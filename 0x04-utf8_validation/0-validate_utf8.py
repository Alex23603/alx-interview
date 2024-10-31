#!/usr/bin/python3
"""
Function to determine if a data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits of a byte
    byte_mask1 = 1 << 7  # 10000000 in binary
    byte_mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Mask to check if the most significant bit is 1 (for 2, 3, or 4-byte characters)
        mask = 1 << 7

        if num_bytes == 0:
            # Count the number of leading 1s to determine the character length
            while (byte & mask):
                num_bytes += 1
                mask >>= 1
            
            # 1-byte character
            if num_bytes == 0:
                continue
            
            # Invalid scenarios (more than 4 bytes or 1 byte with 10xxxxxx pattern)
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For each byte in the sequence, it should start with "10"
            if not (byte & byte_mask1 and not (byte & byte_mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
