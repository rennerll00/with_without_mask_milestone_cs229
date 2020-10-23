import os

i = 0

for file in os.listdir("/Users/rennerll/Desktop/without_mask"):
    os.rename("/Users/rennerll/Desktop/without_mask/" + file, f"/Users/rennerll/Desktop/without_mask/without_mask_{i}.jpg")
    i = i+1
