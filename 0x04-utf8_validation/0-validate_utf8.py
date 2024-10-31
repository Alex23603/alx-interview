def validUTF8(data):
    # Tracks the number of remaining bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the patterns of UTF-8 bytes
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Apply a mask to restrict to the last 8 bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in this character based on the leading bits
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If byte starts with 10xxxxxx, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
            # For a single-byte character
            if num_bytes == 0:
                continue
        else:
            # Check if byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # All characters should be complete at the end
    return num_bytes == 0
