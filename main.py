import customtkinter
from crc_calculator import string_to_bytes, calculate_crc16_modbus, format_crc_output

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Main application window
app = customtkinter.CTk()
app.title("CRC16 MODBUS Calculator")
app.geometry("400x300")

# Placeholder function for CRC calculation
def calculate_and_display_crc():
    """Calculates CRC and updates the display."""
    input_string = input_entry.get()
    if not input_string:
        crc_result_label.configure(text="CRC16: ")
        full_string_label.configure(text="Full String: ")
        return

    data_bytes = string_to_bytes(input_string)
    crc_value = calculate_crc16_modbus(data_bytes)
    formatted_crc = format_crc_output(crc_value)

    crc_result_label.configure(text=f"CRC16: {formatted_crc}")
    full_string_label.configure(text=f"Full String: {input_string}{formatted_crc}")

# GUI Elements
# Input Label and Entry
input_label = customtkinter.CTkLabel(app, text="Input String:")
input_label.pack(pady=5)

input_entry = customtkinter.CTkEntry(app, width=300)
input_entry.pack(pady=5)

# Calculate Button
calculate_button = customtkinter.CTkButton(app, text="Calculate CRC", command=calculate_and_display_crc)
calculate_button.pack(pady=10)

# CRC Result Label
crc_result_label = customtkinter.CTkLabel(app, text="CRC16:")
crc_result_label.pack(pady=5)

# Full String Label
full_string_label = customtkinter.CTkLabel(app, text="Full String:")
full_string_label.pack(pady=5)

# Start the customtkinter main loop
app.mainloop()
