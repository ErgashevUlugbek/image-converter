import tkinter as tk
from tkinter import StringVar
from tkinter import filedialog, messagebox
from classes import converter, text_formatter
from tkinter import ttk

class App:
    mainframe = None
    def __init__(self):
        self.text_formatter = text_formatter.TextFormatter()
        self.image_converter = converter.ImageConverter()

    def start(self):
        root = tk.Tk()
        root.title("Image to WebP Converter")
        root.geometry("400x250")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=('W', 'E', 'N', 'S'))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe,
                  justify="center",
                  text="Convert all images to the webp format in place").grid(column=3,row=1, sticky=('W', 'E'))
        ttk.Button(self.mainframe, text="Convert", command=self.convert).grid(column=3, row=3, sticky=('W', 'E'))

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        root.mainloop()

    def convert(self, results_path="results"):
        """Open folder selection dialog and start conversion."""
        selected_folder = filedialog.askdirectory(title="Select a Folder Containing Images")
        print(selected_folder)
        if selected_folder:
            self.image_converter.set_source_path(selected_folder)
            self.image_converter.batch_convert()
            self.show_result()

    def show_result(self):
        print('images converted: ', self.image_converter.count)
        ttk.Label(self.mainframe, text=f"{self.image_converter.count} images converted").grid(column=2, row=2, sticky='E')
