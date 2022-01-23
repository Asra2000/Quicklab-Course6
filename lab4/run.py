'''
Script to process the text files (001.txt, 003.txt ...) from the 
supplier-data/descriptions directory. The script should turn the data 
into a JSON dictionary by adding all the required fields, including the image 
associated with the fruit (image_name), and uploading it to 
http://[linux-instance-external-IP]/fruits using the Python requests library.
'''
#!/usr/bin/env python3
import os
import requests


folder = "supplier-data/descriptions/"
url = "http://localhost/fruits/"
description_json = {}

for file in os.listdir(folder):
        try :
                lines = open(folder + file, 'r').read().splitlines()
                description_json["name"] = lines[0]
                description_json["weight"] = int(lines[1].replace("lbs", "").strip())
                description_json["description"] = lines[2]
                description_json["image_name"] = os.path.splitext(file)[0] + ".jpeg"

                res = requests.post(url, json=description_json)
                res.raise_for_status()
                print(res.status_code)
        except:
                print("The task failed !!")

print("All the post requests completed !!")


