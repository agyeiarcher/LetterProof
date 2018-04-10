from string import *

startsize=35
textwaterfall=3

margin=40

f=CurrentFont()
s=f.selection

fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

SingleFont=str(s)

for char in "[ ' ] ":
        SingleFont=SingleFont.replace(char, "")

print(SingleFont)

# print(SingleFont)

def ControlCharSelected():
    
    nstring = FormattedString()
    ostring = FormattedString()
    ostring.fontSize(14)
    nstring.fontSize(14)
    
    if SingleFont in ascii_uppercase:
        ncontrols="HH"
        ocontrols="OO"
    elif SingleFont in ascii_lowercase:
        ncontrols="nn"
        ocontrols="oo"
        
    if fontName in installedFonts():
        nstring.font(fontName)
        ostring.font(fontName)
    else:
        print('font %s not installed' % fontName)
        
    nstring.append(ncontrols+SingleFont+ncontrols)
    ostring.append(ocontrols+SingleFont+ocontrols)        
    
    ospacing=FormattedString()
        
    ospacing.fontSize(startsize*textwaterfall)
    if fontName in installedFonts():
        ospacing.font(fontName)
    else:
        print('font %s not installed' % fontName)
    
    ospacing.append(SingleFont+"\n")
    
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
            
        otxt = ocontrols+SingleFont+ocontrols
        ntxt = ncontrols+SingleFont+ncontrols
        
        ospacing.align("left")
        ospacing.append(otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
    
    newPage('LetterLandscape')
    
    alltext=ospacing+"\n"+nstring+"\n"+ostring
    textBox(alltext, (margin,margin/2,width()-margin*4,height()-margin*2))
    printImage()
        
ControlCharSelected()
