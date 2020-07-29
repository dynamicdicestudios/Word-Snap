import pytesseract, pyperclip    
from PIL import ImageGrab, Image   

def convert():
    try:
        file = 'image.PNG'
        # opening an image from the source path 
        img = ImageGrab.grabclipboard()

        img.save(file, 'PNG')

        image = Image.open(file)
        # path where the tesseract module is installed 
        pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
        # converts the image to result and saves it into result variable 
        result = pytesseract.image_to_string(image)

        pyperclip.copy(result)

        if len(result) == 0:
            return None
    except AttributeError:
        return False
