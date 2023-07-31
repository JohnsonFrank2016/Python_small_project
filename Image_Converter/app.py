import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

class ImageConverter:
    def __init__(self, root):
        self.image_files = []
        self.root = root
        self.root.title('Image Converter')
        self.root.geometry('500x650')
        self.create_widgets()
        self.root.resizable(False, False)

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        self.select_files_button = ttk.Button(frame, text="Select Images", command=self.select_files)
        self.select_files_button.pack(pady=10)

        self.listbox = tk.Listbox(frame, width=50, height=20)
        self.listbox.pack(pady=10)

        self.remove_button = ttk.Button(frame, text="Remove Selected", command=self.remove_selected)
        self.remove_button.pack(pady=10)

        self.label = ttk.Label(frame, text="Output Format:")
        self.label.pack(pady=10)

        self.format_var = tk.StringVar()
        self.format_var.set('jpeg')

        self.option_menu = ttk.OptionMenu(frame, self.format_var, 'jpeg', 'png', 'webp', 'jpeg')
        self.option_menu.pack(pady=10)

        self.convert_button = ttk.Button(frame, text="Convert", command=self.convert_images)
        self.convert_button.pack(pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames(filetypes=[('Image Files', '*.png'), ('Image Files', '*.jpg'), ('Image Files', '*.webp'), ('Image Files', '*.jpeg')])
        self.image_files.extend(files)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.image_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    def remove_selected(self):
        selected_indices = self.listbox.curselection()
        for index in selected_indices[::-1]:
            del self.image_files[index]
        self.update_listbox()

    def convert_images(self):
        target_format = self.format_var.get()
        output_dir = filedialog.askdirectory()
        output_dir = os.path.join(output_dir, 'output_images')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for file in self.image_files:
            img = Image.open(file).convert("RGB")
            root, ext = os.path.splitext(os.path.basename(file))
            img.save(os.path.join(output_dir, f"{root}.{target_format}"), target_format)

        messagebox.showinfo("Conversion Successful", f"Images converted to {target_format} format!")
        subprocess.call(["open", output_dir])

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverter(root)
    root.mainloop()
