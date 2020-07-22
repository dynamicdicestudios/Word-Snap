import pytesseract, pyperclip    
from PIL import Image     

def main(file):
    #file = 'substinces.PNG'
    # opening an image from the source path 
    img = Image.open()

    # path where the tesseract module is installed 
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img)

    pyperclip.copy(result)

    
        
    
