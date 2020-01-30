import os

DIR = "Images"

count = 0
for f in os.listdir(DIR):
    fname = os.path.join(DIR, f)
    os.rename(fname, f"Images/img-{count}.jpg")
    count += 1
