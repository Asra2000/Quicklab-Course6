#!/usr/bin/env python3

from PIL import Image
import os

folder = "/opt/icons/"
current_dir = os.getcwd()

# Load the images

for imagepath in os.listdir(current_dir + "/images"):
        name, e = os.path.splitext(imagepath)
        outpath = name + ".jpg"
        if imagepath != outpath:
                try:
                        # outpath = imagepath.split('.')[0]
                        # print(imagepath, outpath)
                        image = Image.open(current_dir + "/images/" + imagepath)
                        # Image resolution to 128 x 128 px
                        # Rotate image 90 deg clockwise
                        newimage = image.resize((128, 128)).rotate(-90).convert("RGB")

                        # Change the file type to jpeg
                        newimage.save(current_dir + folder + outpath)
                except OSError:
                        print(imagepath, "cannot be converted")

