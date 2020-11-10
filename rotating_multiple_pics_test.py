#Pillow (PIL Fork) module is required to be installed
import glob
from PIL import Image

def image_processing(e, r):
    conc = "*." + e
    pics_list = glob.glob(conc)
    for i in pics_list:
        img = Image.open(i)
        img = img.rotate(int(r)) # 90, -90, 180, ...
        img.save(i) # to override your old file

e = input("Which file extension u want to rotate: ")
r = input("For how much degrees: ")
image_processing(e, r)
print("Done!")