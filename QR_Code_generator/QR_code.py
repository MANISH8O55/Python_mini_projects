from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk


root = Tk()
root.title("QR Code Generator")
root.iconbitmap('qrcode.png')
root.geometry("500x550")

def create_code():
    #File Dialog
    input_path = filedialog.asksaveasfilename(title="Save Image",
          filetyp=(("PNG File",".png"),("All Files", "*.*")))

    if input_path:
        if input_path.endswith(".png"):
            # Create QR code from entry box
            get_code = pyqrcode.create(my_entry.get())
            # Save as PNG File
            get_code.png(input_path, scale=5)
        else:
            # Add that .png to the end of the file name
            input_path = f'{input_path}.png'
            # Create QR code from entry box
            get_code = pyqrcode.create(my_entry.get())
            # Save as PNG file
            get_code.png(input_path, scale=5)

        # put QR code on screen
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        # Add imge to label
        my_label.config(image=get_image)


def clear_all():
    my_entry.delete(0,END)
    my_entry.insert(0,"")


# Create  GUI

my_entry = Entry(root, font=("Helvetica",18))
my_entry.pack(pady=20)

my_button = Button(root, text="create QR code", command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text="Clear", command=clear_all)
my_button2.pack()

my_label = Label(root,text=" ")
my_label.pack(pady=20)

root.mainloop()