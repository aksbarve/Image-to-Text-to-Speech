from PIL import Image
import pytesseract
from gtts import gTTS
from playsound import playsound


# Tesseract path to downloaded directory. Add to path variable

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# Open the image and get text from the image using tesseract
# select the image you want here
im = Image.open("sample.jpg")
text = pytesseract.image_to_string(im, lang='eng')

print(text)

# Store output as a txt file
f = open("output.txt", "w+")
f.write(text)

# Text to speech using gTTS and save the speech as mp3
language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("sample.mp3")

# Play mp3 from terminal
playsound('sample.mp3')



