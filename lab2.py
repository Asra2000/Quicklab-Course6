#! usr/bin/env python3

import os
import requests
import json

DIR = "/data/feedback/"
url = "http://35.202.163.144/feedback/"
raw_data = {}

for file in os.listdir(DIR):
        try :
                lines = open(DIR + file, 'r').read().splitlines()
                raw_data["title"] = lines[0]
                raw_data["name"] = lines[1]
                raw_data["date"] = lines[2]
                raw_data["feedback"] = lines[3]

                res = requests.post(url, json=raw_data)
                res.raise_for_status()
                print(res.status_code)
        except:
                print("The task failed !!")

print("All the post requests completed !!")
