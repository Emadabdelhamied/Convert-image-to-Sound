'''Converting image to Sound'''
import os
import time
import sys
from cv2 import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def loading():
    '''loading'''
    print("\u001b[37;1mLoading...")
    for i in range(0, 100):
        time.sleep(0.001)
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.flush()
        time.sleep(0.001)
        sys.stdout.write(str(i + 1) + "%")
        sys.stdout.flush()
lan = input('\u001b[33;1mEnter The Image language (\'eng\' For English or \'ara\' For Arabic) :- ')
path = input('\u001b[33;1mEnter The Image Path :- ')
image = cv2.imread(path)
image_to_text = pytesseract.image_to_string(image, lang=lan)
print('-'*45)
time.sleep(1)
os.system('cls')
file = open('image_to_text.txt', 'w', encoding='utf-8')
file.writelines(image_to_text)
file.close()
file = open('image_to_text.txt', encoding='utf-8')
txt = file.read()
file.close()
loading()
name = os.path.basename(path)
audio = name[:name.index('.')]+'.mp3'
sp = gTTS(text=txt, lang=lan[:2], slow=False)
try:
    sp.save(audio)
    playsound(audio)
except ValueError:
    pass
