import pytesseract as pt
from PIL import Image

def process(names):
    aktivis = {}
    ignore = ["", "Pengumuman", "Aksub", "PR", "EEO", "FAVE", "FILE", "LnT", "HRD", "RnD"]
    for name in names:
        temp = name.split(" ")
        for key in temp:
            if key not in ignore and len(key) > 2:
                if key in aktivis:
                    aktivis[key] += 1
                else:
                    aktivis[key] = 1

    for ind in aktivis:
        print(ind + " - " + str(aktivis[ind]))

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open('435182.jpg')
text = pt.image_to_string(img)

names = text.splitlines()

process(names)