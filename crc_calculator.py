def string_to_bytes(input_string: str) -> bytes:
    """
    Converts a string of hexadecimal characters to bytes.

    Each pair of characters in the string is interpreted as a single byte.
    For example, "01" becomes 0x01, "AB" becomes 0xAB.

    Args:
        input_string: The input string of hexadecimal characters.

    Returns:
        The corresponding bytes.

    Raises:
        ValueError: If the input string has an odd number of characters
                    or contains non-hexadecimal characters.
    """
    if len(input_string) % 2 != 0:
        raise ValueError("Input string must have an even number of characters.")

    try:
        return bytes.fromhex(input_string)
    except ValueError:
        raise ValueError("Input string contains non-hexadecimal characters.")

def calculate_crc16_modbus(data_bytes: bytes) -> int:
    """
    Calculates the CRC16 MODBUS checksum.

    Args:
        data_bytes: The input data as bytes.

    Returns:
        The calculated CRC16 MODBUS checksum as an integer,
        with its bytes swapped. For example, if the standard
        calculation results in 0x1234, this function will return 0x3412.
    """
    crc = 0xFFFF  # Initial CRC value
    polynomial = 0xA001  # Polynomial (reversed form of 0x8005)

    for byte in data_bytes:
        crc ^= byte  # XOR byte into the LSB of CRC
        for _ in range(8):
            if crc & 0x0001:  # If LSB of CRC is 1
                crc >>= 1  # Right shift CRC by one
                crc ^= polynomial  # XOR with polynomial
            else:
                crc >>= 1  # Right shift CRC by one

    # Swap bytes of the calculated CRC
    swapped_crc = ((crc << 8) & 0xFF00) | ((crc >> 8) & 0x00FF)
    return swapped_crc

def format_crc_output(crc_value: int) -> str:
    """
    Formats the 16-bit CRC value into a string (lower byte first).

    Args:
        crc_value: The 16-bit CRC value.

    Returns:
        A string representation of the CRC value, with lower byte first,
        each byte as a two-character hexadecimal string.
        Example: crc_value = 0x1234 should return "3412".
    """
    low_byte = crc_value & 0xFF
    high_byte = (crc_value >> 8) & 0xFF
    return f"{low_byte:02X}{high_byte:02X}"
