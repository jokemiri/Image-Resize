from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

class ImageResizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        self.file_label = Label(master, text="No file selected")
        self.file_label.pack()

        self.select_button = Button(master, text="Select file", command=self.select_file)
        self.select_button.pack(pady=10)

        self.width_label = Label(master, text="Width (pixels):")
        self.width_label.pack()

        self.width_input = Entry(master)
        self.width_input.pack()

        self.height_label = Label(master, text="Height (pixels):")
        self.height_label.pack()

        self.height_input = Entry(master)
        self.height_input.pack()

        self.resize_button = Button(master, text="Resize", command=self.resize_image)
        self.resize_button.pack(pady=10)

        self.status_label = Label(master, text="")
        self.status_label.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=file_path)

    def resize_image(self):
        image_path = self.file_label.cget("text")
        if not image_path:
            self.status_label.config(text="Please select a file")
            return

        try:
            width = int(self.width_input.get())
            height = int(self.height_input.get())
        except ValueError:
            self.status_label.config(text="Please enter valid dimensions")
            return

        with Image.open(image_path) as image:
            resized_image = image.resize((width, height))

            base_path, ext = os.path.splitext(image_path)
            new_image_path = f"{base_path}_resized{ext}"
            resized_image.save(new_image_path)

        self.status_label.config(text="Image resized successfully")

root = Tk()
gui = ImageResizerGUI(root)
root.mainloop()
