import os

DIR = "Data"

count = 0
for f in os.listdir(DIR):
    fname = os.path.join(DIR, f)
    os.rename(fname, f"Data/img-{count}.jpg")
    count += 1
