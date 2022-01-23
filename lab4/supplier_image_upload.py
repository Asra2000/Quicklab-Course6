'''
Script that takes the jpeg images from the supplier-data/images 
directory that you've processed previously and uploads them to the 
web server fruit catalog.
'''

#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

for image in os.listdir(path):
  if image.endswith(".jpeg"):
    with open(path + image, 'rb') as file:
      r = requests.post(url, files={'file': file})