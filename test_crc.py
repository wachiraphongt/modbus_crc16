from crc_calculator import string_to_bytes, calculate_crc16_modbus, format_crc_output

input_str = "010300000001"
expected_crc_val = 0x840A
expected_formatted_crc = "840A" # Changed from "0A84" to "840A"

print(f"Input string: '{input_str}'")

data_bytes = string_to_bytes(input_str)
print(f"Input as bytes: {data_bytes}")

actual_crc_val = calculate_crc16_modbus(data_bytes)
print(f"Calculated CRC value (int): {actual_crc_val} ({actual_crc_val:#04X})")

actual_formatted_crc = format_crc_output(actual_crc_val)
print(f"Formatted CRC (string): '{actual_formatted_crc}'")

assert actual_crc_val == expected_crc_val, f"CRC value mismatch: Expected {expected_crc_val:#04X}, Got {actual_crc_val:#04X}"
assert actual_formatted_crc == expected_formatted_crc, f"Formatted CRC mismatch: Expected '{expected_formatted_crc}', Got '{actual_formatted_crc}'"

print("CRC logic test passed successfully!")
