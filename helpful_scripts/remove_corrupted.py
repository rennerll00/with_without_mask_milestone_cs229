import os
from PIL import Image

i = 0
j = 0

for file in os.listdir("/Users/rennerll/Desktop/mask-attempt/train"):
    i += 1

    try:
        img = Image.open("/Users/rennerll/Desktop/mask-attempt/train/" + file)
    except Exception as e:
        print(e)
        print(file)
        print("")
        j += 1

print("total:", i)
print("problems:", j)
