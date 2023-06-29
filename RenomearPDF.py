import re
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user-name\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
path = "pdfs"  # pasta com os pdfs
filename = "page_2.jpg"
n_file = 0

for pdfName in os.listdir(path):
    inputPath = os.path.join(path, pdfName)
    pages = convert_from_path(inputPath, 100)
    pages[1].save(filename, 'JPEG')

    image = Image.open(filename)
    text = pytesseract.image_to_string(image, lang='por')
    image.close()
    os.remove(filename)

    r = re.compile(r'SETOR = \d{15}')
    setor = r.findall(text)[0][8:]
    PDF_new_name = path + '\\' + setor + '.pdf'

    n_file = 0
    result = 0
    while result == 0:
        try:
            os.rename(inputPath, PDF_new_name)
            result = 1
        except FileExistsError:
            n_file = n_file + 1
            str_file = "_" + n_file.__str__()
            PDF_new_name = path + '\\' + setor + str_file + '.pdf'

    print("Arquivo renomeado com sucesso de: " + inputPath + " para: " + PDF_new_name)
