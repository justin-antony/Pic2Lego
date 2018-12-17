#Pixelate function copied from https://github.com/useless-tools/pixelate/blob/master/pixelate/pixelate.py and modified
from PIL import Image
from tkinter import filedialog as fd

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image

input("Press enter to choose a source file")

input_path = fd.askopenfilename(title = "Select image", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

print(input_path, " is the selected input path")
input("Please select a save location")

output_path = fd.asksaveasfilename(title = "Choose save location")

pixelsize = int(input("Choose the new pixel size (larger number means more blocky: "))

input("Press enter to run script...")

legoFied = pixelate(input_path, pixelsize)

legoFied.save(output_path)

