try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    pytesseract.pytesseract.tesseract_cmd =\
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(Image.open(filename))
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
