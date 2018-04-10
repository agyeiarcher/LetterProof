from string import *

f=CurrentFont()

PunctuationList=[]

for f in AllFonts():
    for k in f.keys():
        if k not in ascii_letters:
                PunctuationList.append(k)
                if k=="space":
                    PunctuationList.remove(k)    
       
print(PunctuationList)