# Import required libraries
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

# Define a class for the image converter application
class ImageConverter:
    def __init__(self, root):
        # Initialize the instance variables
        self.image_files = []  # List to hold the selected image files
        self.root = root  # The tkinter root window

        # Set properties of the root window
        self.root.title('Image Converter')
        self.root.geometry('500x650')

        # Create the GUI widgets
        self.create_widgets()
        self.root.resizable(False, False)

    # Method to create the GUI widgets
    def create_widgets(self):
        # Create a frame to hold the widgets
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a button for selecting images
        self.select_files_button = ttk.Button(frame, text="Select Images", command=self.select_files)
        self.select_files_button.pack(pady=10)

        # Create a listbox to display the selected image files
        self.listbox = tk.Listbox(frame, width=50, height=20)
        self.listbox.pack(pady=10)

        # Create a button for removing selected images
        self.remove_button = ttk.Button(frame, text="Remove Selected", command=self.remove_selected)
        self.remove_button.pack(pady=10)

        # Create a label for output format selection
        self.label = ttk.Label(frame, text="Output Format:")
        self.label.pack(pady=10)

        # Create a variable to hold the selected output format
        self.format_var = tk.StringVar()
        self.format_var.set('jpeg')

        # Create a dropdown menu for selecting the output format
        self.option_menu = ttk.OptionMenu(frame, self.format_var, 'jpeg', 'png', 'webp', 'jpeg')
        self.option_menu.pack(pady=10)

        # Create a button for starting the conversion
        self.convert_button = ttk.Button(frame, text="Convert", command=self.convert_images)
        self.convert_button.pack(pady=10)

    # Method to select the image files
    def select_files(self):
        # Open a file dialog to select the image files
        files = filedialog.askopenfilenames(filetypes=[('Image Files', '*.png'), ('Image Files', '*.jpg'), ('Image Files', '*.webp'), ('Image Files', '*.jpeg')])
        # Add the selected files to the list
        self.image_files.extend(files)
        # Update the listbox
        self.update_listbox()

    # Method to update the listbox
    def update_listbox(self):
        # Delete all existing items from the listbox
        self.listbox.delete(0, tk.END)
        # Add the current image files to the listbox
        for file in self.image_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    # Method to remove selected files
    def remove_selected(self):
        # Get the indices of the selected listbox items
        selected_indices = self.listbox.curselection()
        # Remove the selected items from the list of image files
        for index in selected_indices[::-1]:
            del self.image_files[index]
        # Update the listbox
        self.update_listbox()

    # Method to convert the images
    def convert_images(self):
        # Get the selected output format
        target_format = self.format_var.get()
        # Ask the user to select an output directory
        output_dir = filedialog.askdirectory()
        output_dir = os.path.join(output_dir, 'output_images')
        # Create the output directory if it does not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Convert each image file
        for file in self.image_files:
            # Open the image file
            img = Image.open(file).convert("RGB")
            # Get the filename without the extension
            root, ext = os.path.splitext(os.path.basename(file))
            # Save the image in the new format
            img.save(os.path.join(output_dir, f"{root}.{target_format}"), target_format)

        # Show a message box indicating the conversion was successful
        messagebox.showinfo("Conversion Successful", f"Images converted to {target_format} format!")
        # Open the output directory
        subprocess.call(["open", output_dir])

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverter(root)
    root.mainloop()
