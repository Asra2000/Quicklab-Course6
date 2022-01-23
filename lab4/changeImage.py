'''
Script to process supplier images.

Specifications include - 
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
'''

#!/usr/bin/env python3
from PIL import Image
import os   

folder = "supplier-data/images/"

# Load the images
for imagepath in os.listdir(folder):
        name, e = os.path.splitext(imagepath)
        outpath = name + ".jpeg"
        if 'tiff' != imagepath:
                try:
                        image = Image.open(folder + imagepath)
                        newimage = image.convert("RGB").resize((600, 400))
                        # Change the file type to jpeg
                        newimage.save(folder + outpath, "JPEG")
                except OSError:
                        print(imagepath, "cannot be converted")
