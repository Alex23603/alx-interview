def validUTF8(data):
    # Number of bytes left to check for a character
    num_bytes = 0

    # Masks to check leading bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine how many bytes are in this character
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            
            if num_bytes == 0:
                continue
            
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        num_bytes -= 1
    
    return num_bytes == 0
