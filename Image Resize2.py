from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageResizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")
        master.geometry('800x500')
        master.resizable(False, False)
        master.configure(bg='#abdbe3') #background

        icon = ImageTk.PhotoImage(Image.open('icon.png'))
        master.iconphoto(False, icon)

        self.file_path = ""
        self.original_image = None

        # Create a frame to hold the file selection components
        self.file_frame = Frame(master)
        self.file_frame.pack(padx=10, pady=10)

        # Create the file selection label and button
        self.file_label = Label(self.file_frame, text="No file selected")
        self.file_label.pack(side=LEFT, padx=(0, 10))

        self.select_button = Button(self.file_frame, text="Select file", command=self.select_file, bg='#eab676')
        self.select_button.pack(side=LEFT)

        # Create a frame to hold the preview and dimensions components
        self.preview_frame = Frame(master, bg='#abdbe3')
        self.preview_frame.pack(padx=10, pady=10)

        # Create the preview image label
        self.preview_label = Label(self.preview_frame, bg='#abdbe3')
        self.preview_label.pack(side=LEFT, padx=(0, 10))

        # Create a frame to hold the dimensions input components
        self.dimensions_frame = Frame(self.preview_frame, bg='#abdbe3')
        self.dimensions_frame.pack(side=LEFT)

        # Create the dimensions input labels and entry boxes
        self.width_label = Label(self.dimensions_frame, text="Width:", bg='#abdbe3')
        self.width_label.pack()

        self.width_input = Entry(self.dimensions_frame)
        self.width_input.pack()

        self.height_label = Label(self.dimensions_frame, text="Height:", bg='#abdbe3')
        self.height_label.pack()

        self.height_input = Entry(self.dimensions_frame)
        self.height_input.pack()

        # Create a frame to hold the unit type options
        self.unit_frame = Frame(master, bg='#abdbe3')
        self.unit_frame.pack(padx=10, pady=10)

        # Create the unit type label and option menu
        self.unit_label = Label(self.unit_frame, text="Unit type:", bg='#abdbe3')
        self.unit_label.pack(side=LEFT, padx=(0, 10))

        self.unit_var = StringVar(self.unit_frame)
        self.unit_var.set("pixels")

        self.unit_menu = OptionMenu(self.unit_frame, self.unit_var, "pixels", "cm", "inches", "mm")
        self.unit_menu.pack(side=LEFT)

        # Create the resize button and status label
        self.resize_button = Button(master, text="Resize", command=self.resize_image, bg='#eab676')
        self.resize_button.pack(pady=10)

        self.status_label = Label(master, text="", bg='#abdbe3')
        self.status_label.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=os.path.basename(file_path))

            # Load the image and display the preview
            self.original_image = Image.open(file_path)
            preview_image = self.original_image.copy()
            preview_image.thumbnail((300, 300))
            self.preview_image = ImageTk.PhotoImage(preview_image)
            self.preview_label.config(image=self.preview_image)

            # Display the current dimensions in the input fields
            self.display_current_dimensions()

    def resize_image(self):
        if not self.file_path:
            self.status_label.config(text="Please select a file")
            return

        try:
            # Convert the input dimensions to pixels
            unit_type = self.unit_var.get()
            width = self.convert_to_pixels(self.width_input.get(), unit_type)
            height = self.convert_to_pixels(self.height_input.get(), unit_type)

            # Resize the image
        except ValueError:
            self.status_label.config(text="Please enter valid dimensions")
            return

        with Image.open(unit_type) as image:
            resized_image = image.resize((width, height))

            base_path, ext = os.path.splitext(unit_type)
            new_image_path = f"{base_path}_resized{ext}"
            resized_image.save(new_image_path)

        self.status_label.config(text="Image resized successfully")

root = Tk()
gui = ImageResizerGUI(root)
root.mainloop()

