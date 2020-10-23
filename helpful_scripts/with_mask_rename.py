import os

i = 0

for file in os.listdir("/Users/rennerll/Desktop/with_mask"):
    os.rename("/Users/rennerll/Desktop/with_mask/" + file, f"/Users/rennerll/Desktop/with_mask/with_mask_{i}.jpg")
    i = i+1
