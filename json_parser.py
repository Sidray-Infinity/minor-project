import urllib.request
import requests
import json
import requests

with open("Data/Indian_Number_plates.json") as f:
    data = json.load(f)

links = []

for d in data:
    links.append(d['content'])

count = 0
for link in links:
    print(".", end=' ')
    try:
        urllib.request.urlretrieve(link, f"Images/img-{count}.jpg")
        print(count)
        count += 1
    except:
        pass

# str_ = "https://f1.media.brightcove.com/8/1078702682/1078702682_6004950245001_6004956161001-vs.jpg?pubId=1078702682&videoId=6004956161001"

# imgURL = str_

# urllib.request.urlretrieve(imgURL, "local-filename.jpg")
