# Import the required libraries
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont

# Function to generate a password
def generate_passwoed():
    # Get the user input from the GUI
    length_str = entry_length.get()
    upper = bool_var_upper.get()
    lower = bool_var_lower.get()
    digits = bool_var_digits.get()
    symbols = bool_var_symbols.get()
    
    # Convert the length of the password from string to integer
    length = int(length_str)

    # Add the selected types of characters to the characters string
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Check if no types of characters were selected, if so display an error message
    if characters == "":
        messagebox.showerror("Error", "You must select at least one type of characters.")
        return

    # Generate the password
    password = "".join(random.choice(characters) for _ in range(length))
    password_str.set(password)

# Function to copy the generated password to the clipboard
def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_str.get())

# Create a tkinter window
window = Tk()
window.title("Password Generator")
window.geometry("1000x340")
window.resizable(False, False)
window.config(bg = "black")

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int((screen_width / 2) - (1000 / 2))
center_y = int((screen_height / 2) - (340 / 2))

# Set the window to appear at the center of the screen
window.geometry("+{}+{}".format(center_x, center_y))

# Set the font style for the text in the GUI
fontStyle = tkFont.Font(family = "Arial", size = 20)

# Create the GUI elements
Label(window, text = "Password length:", font = fontStyle, bg = "black").grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
entry_length = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, width = 20, length = 800)
entry_length.grid(row = 0, column = 1, sticky = W, padx = 10, pady = 10)

# Checkboxes for selecting the types of characters to include in the password
bool_var_upper = BooleanVar()
Checkbutton(window, text = "Include uppercase letters", variable = bool_var_upper, font = fontStyle, bg = "black").grid(row = 1, column = 0, columnspan = 2, sticky = W, padx = 10)
bool_var_lower = BooleanVar()
Checkbutton(window, text="Include lowercase letters", variable = bool_var_lower, font = fontStyle, bg = "black").grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 10)
bool_var_symbols = BooleanVar()
Checkbutton(window, text="Include symbols", variable = bool_var_symbols, font = fontStyle, bg = "black").grid(row = 3, column = 0, columnspan = 2, sticky = W, padx = 10)
bool_var_digits = BooleanVar()
Checkbutton(window, text="Include digits", variable = bool_var_digits, font = fontStyle, bg = "black").grid(row = 4, column = 0, columnspan = 2, sticky = W, padx = 10)

# Button to generate the password
Button(window, text = "Generate password", command = generate_passwoed, font = fontStyle).grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)

# Label to display the generated password
password_str = StringVar()
Label(window, textvariable = password_str, font = tkFont.Font(family = "Arial", size = 14), bg = "black").grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

# Button to copy the generated password
Button(window, text = "Copy", command = copy_password, font = fontStyle, bg = "black").grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10)

# Start the tkinter event loop
window.mainloop()
