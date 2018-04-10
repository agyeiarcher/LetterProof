from string import *

f=CurrentFont()

fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

LowerCaseLetters=[]
UpperCaseLetters=[]
FontDigits=[]

#MAKE A LIST OF THE GLYPHS IN THE FONT

#UPPERCASE
for f in AllFonts():
    for k in f.keys():
        if k in ascii_lowercase:
            LowerCaseLetters.append(k)
#LOWERCASE
for f in AllFonts():
    for k in f.keys():
        if k in ascii_uppercase:
            UpperCaseLetters.append(k)
#NUMBERS       
for f in AllFonts():
    for k in f.keys():
        if k in digits:
            FontDigits.append(k)

#SORT LISTS NUMERICALLY/ALPHABETICALLY

LowerCaseLetters=sorted(LowerCaseLetters)    
UpperCaseLetters=sorted(UpperCaseLetters)

print(LowerCaseLetters)
print(UpperCaseLetters)
print(FontDigits)