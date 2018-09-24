from PIL import Image
import pytesseract
from gtts import gTTS
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
im = Image.open("sample.jpg")

text = pytesseract.image_to_string(im, lang='eng')

print(text)

language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)

myobj.save("sample.mp3")

playsound('sample.mp3')


