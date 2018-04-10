from string import *

startsize=35
textwaterfall=3

margin=40

f=CurrentFont()

fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

LowerCaseLetters=[]
UpperCaseLetters=[]
Punctuation=[]

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
#PUNCTUATION       
for f in AllFonts():
    for k in f:
        if str(k) in punctuation:
            Punctuation.append(k)

#SORT LISTS NUMERICALLY/ALPHABETICALLY

LowerCaseLetters=sorted(LowerCaseLetters)    
UpperCaseLetters=sorted(UpperCaseLetters)
Punctuation=sorted(Punctuation)


# SingleFont=str(s)
# for char in "[ ' ] ":
#         SingleFont=SingleFont.replace(char, "")
# # print(SingleFont)
    
#LOWERCASE PROOFS

def ProofLowercase():
    nstring = FormattedString()
    ostring = FormattedString()
    ostring.fontSize(16)
    nstring.fontSize(16)
    
    if fontName in installedFonts():
        nstring.font(fontName)
        ostring.font(fontName)
    else:
        print('font %s not installed' % fontName)
    
    for k in range(len(LowerCaseLetters)):
        nstring.append("nn"+LowerCaseLetters[k]+"nn")
    for l in range(len(LowerCaseLetters)):
        ostring.append("oo"+LowerCaseLetters[l]+"oo")
    
    for i in range(len(LowerCaseLetters)):
        
        ospacing=FormattedString()
        
        ospacing.fontSize(startsize*textwaterfall)
        if fontName in installedFonts():
            ospacing.font(fontName)
        else:
            print('font %s not installed' % fontName)
        ospacing.append(str(LowerCaseLetters[i])+"\n")
        
        for j in reversed(range(textwaterfall)):
            if j ==0:
                currentfontsize=startsize/2
            if j>0:
                currentfontsize=j*startsize
                
            ospacing.fontSize(currentfontsize)
            ospacing.paragraphBottomSpacing(20)
                        
            if fontName in installedFonts():
                ospacing.font(fontName)
            else:
                print('font %s not installed' % fontName)
                
            otxt = "oo"+LowerCaseLetters[i]+"oo"
            ntxt = "nn"+LowerCaseLetters[i]+"nn"
            
            ospacing.align("left")
            ospacing.append(otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
        
        newPage('LetterLandscape')
        
        alltext=ospacing+"\n"+nstring+"\n"+ostring
        textBox(alltext, (margin,margin/2,width()-200,height()-margin*2))
        
        print(alltext)
    
def ProofUppercase():
    
    nstring = FormattedString()
    ostring = FormattedString()
    ostring.fontSize(14)
    nstring.fontSize(14)
    if fontName in installedFonts():
        nstring.font(fontName)
        ostring.font(fontName)
    else:
        print('font %s not installed' % fontName)
    
    for k in range(len(UpperCaseLetters)):
        nstring.append("HH"+UpperCaseLetters[k]+"HH")
    for l in range(len(UpperCaseLetters)):
        ostring.append("OO"+UpperCaseLetters[l]+"OO")
    
    for i in range(len(UpperCaseLetters)):
        
        ospacing=FormattedString()
        
        ospacing.fontSize(startsize*textwaterfall)
        if fontName in installedFonts():
            ospacing.font(fontName)
        else:
            print('font %s not installed' % fontName)
        ospacing.append(str(UpperCaseLetters[i])+"\n")
        
        for j in reversed(range(textwaterfall)):
            if j ==0:
                currentfontsize=startsize/2
            if j>0:
                currentfontsize=j*startsize
                
            ospacing.fontSize(currentfontsize)
            ospacing.paragraphBottomSpacing(20)
                        
            if fontName in installedFonts():
                ospacing.font(fontName)
            else:
                print('font %s not installed' % fontName)
                
            otxt = "OO"+UpperCaseLetters[i]+"OO"
            ntxt = "HH"+UpperCaseLetters[i]+"HH"
            
            ospacing.align("left")
            ospacing.append(otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
        
        newPage('LetterLandscape')
        
        alltext=ospacing+"\n"+nstring+"\n"+ostring
        textBox(alltext, (margin,margin/2,width()-180,height()-margin*2))
        
        print(alltext)
        
        
def ProofPunctuation():
    
    nstring = FormattedString()
    ostring = FormattedString()
    ostring.fontSize(14)
    nstring.fontSize(14)
    if fontName in installedFonts():
        nstring.font(fontName)
        ostring.font(fontName)
    else:
        print('font %s not installed' % fontName)
    
    for k in range(len(Punctuation)):
        nstring.append("HH"+Punctuation[k]+"HH")
    for l in range(len(Punctuation)):
        ostring.append("OO"+Punctuation[l]+"OO")
    
    for i in range(len(Punctuation)):
        
        ospacing=FormattedString()
        
        ospacing.fontSize(startsize*textwaterfall)
        if fontName in installedFonts():
            ospacing.font(fontName)
        else:
            print('font %s not installed' % fontName)
        ospacing.append(str(Punctuation[i])+"\n")
        
        for j in reversed(range(textwaterfall)):
            if j ==0:
                currentfontsize=startsize/2
            if j>0:
                currentfontsize=j*startsize
                
            ospacing.fontSize(currentfontsize)
            ospacing.paragraphBottomSpacing(20)
                        
            if fontName in installedFonts():
                ospacing.font(fontName)
            else:
                print('font %s not installed' % fontName)
                
            otxt = "OO"+Punctuation[i]+"OO"
            ntxt = "HH"+Punctuation[i]+"HH"
            
            ospacing.align("left")
            ospacing.append(otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
        
        newPage('LetterLandscape')
        
        alltext=ospacing+"\n"+nstring+"\n"+ostring
        textBox(alltext, (margin,margin/2,width()-180,height()-margin*2))
        
        print(alltext)
                
ProofUppercase()
