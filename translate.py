# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:17:36 2020

@author: Emmanuel Efewongbe

list of languages: {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 
                    'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 
                    'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 
                    'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 
                    'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 
                    'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 
                    'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 
                    'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 
                    'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 
                    'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 
                    'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 
                    'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 
                    'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 
                    'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 
                    'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 
                    'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 
                    'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 
                    'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 
                    'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 
                    'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 
                    'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 
                    'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 
                    'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', '
                    yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
"""

import cv2
import pytesseract
from googletrans import Translator

#determine what language you want to translate to
langTo = input("What would you like to translate to? (refer to the list): ")

#Assuming this is the location tesseract is located
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#read the image and convert to gray
img = cv2.imread('OIP.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#convert image to data
boxes = pytesseract.image_to_data(img)


for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b = b.split()
        if len(b)==12:
            text = Translator().translate(b[11], dest = langTo)
            print(text.text, file = open('output.txt', 'a'))
cv2.imshow('result', img)
cv2.waitkey(0)