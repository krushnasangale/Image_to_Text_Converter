import pytesseract
from PIL import Image
import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_path = input("enter image file path to convert file into text file :")
img = Image.open(file_path)
txt = pytesseract.image_to_string(img, lang='eng')
txt.replace("\n", " ")
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f'{time_stamp}.txt'
with open(file_name, "w") as file:
    file.write(txt)
