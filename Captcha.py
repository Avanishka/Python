from PIL import Image
from requests import get
from pytesseract import image_to_string 
from io import BytesIO
a = get("https://i.imgur.com/53EnC0i.png") 
img = Image.open(BytesIO(a.content))
txt = image_to_string(img)
if(txt[1] == '+'):
    print(int(txt[0])+int(txt[2]))
elif(txt[1] == '-'):
    print(int(txt[0])-int(txt[2]))
elif(txt[1] == '/'): 
    print(int(txt[0])/int(txt[2]))
elif(txt[1] == '*'): 
    print(int(txt[0])*int(txt[2]))
