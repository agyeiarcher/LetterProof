letterwidth=792
letterheight=612

startsize=35
textwaterfall=3

margin=40

f=CurrentFont()

fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

baseletters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numletters=len(baseletters)

def ControlCharLowercase():
    for i in range(numletters):
        otxt = "oo"+baseletters[i]+"oo"
        ntxt = "nn"+baseletters[i]+"nn"
        
        ospacing=FormattedString()
        ospacing.paragraphBottomSpacing(30)
        ospacing.fontSize(startsize*textwaterfall)
        if fontName in installedFonts():
            ospacing.font(fontName)
        else:
            print('font %s not installed' % fontName)
        ospacing.append(str(baseletters[i]))
        
        for j in reversed(range(textwaterfall)):
            if j ==0:
                currentfontsize=startsize/2
            if j>0:
                currentfontsize=j*startsize
            ospacing.fontSize(currentfontsize)
            if fontName in installedFonts():
                ospacing.font(fontName)
            else:
                print('font %s not installed' % fontName)
            ospacing.paragraphBottomSpacing(30)
            ospacing.align("left")
            ospacing.append("\n"+otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
        newPage(612,792)
        textBox(ospacing, (margin,margin/2,width()-margin*2,height()-margin*2))
        

ControlCharLowercase()