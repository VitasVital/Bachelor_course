import numpy as np
with open('voyna-i-mir-tom-1.txt') as f:
    text = ''
    for i in f:
        text += i
def Book():
    symbols = set(text)
    symbols = [x for x in symbols]

    print('Колличество уникальных символов = ', len(symbols))
    sizeText = len(text)
    print('Size text', sizeText)

    numberOfSymbols = []
    for i in range(len(symbols)):
        numberOfSymbols.append(0)
        for j in text:
            if symbols[i] == j:
                numberOfSymbols[i] += 1

    print('Symbols: ', symbols)
    print('Number of symbols = ', numberOfSymbols)

    probabilitySymbols = []
    for i in range(len(symbols)):
        probabilitySymbols.append(numberOfSymbols[i] / sizeText)
    print(probabilitySymbols)

    entropySymbols = 0
    for i in range(len(probabilitySymbols)):
        entropySymbols += probabilitySymbols[i] * np.log2(1 / probabilitySymbols[i])
    print('Entropy = ', entropySymbols)
    entropyText = entropySymbols * sizeText
    print('Entropy text = ', entropyText)

Book()

from PIL import Image, ImageDraw

def Img():
    img = Image.open('Bear.jpg')
    pixelsColor = []
    (width, height) = img.size
    img = img.load()
    for i in range(width):
        for j in range(height):
            pixelsColor.append(img[i, j])
    print('Number of pixels = ', len(pixelsColor))

    unicPixels = set(pixelsColor)
    print('Number of unique pixels = ', len(unicPixels))
    unicPixels = [x for x in unicPixels]

    numberOfPixels = []
    for i in range(len(unicPixels)):
        numberOfPixels.append(0)
        for j in pixelsColor:
            if unicPixels[i] == j:
                numberOfPixels[i] += 1

    probabilityPixels = []
    for i in range(len(unicPixels)):
        probabilityPixels.append(numberOfPixels[i] / len(pixelsColor))
    print('Probability pixels ', probabilityPixels)

    entropyPixels = 0
    for i in range(len(probabilityPixels)):
        entropyPixels += probabilityPixels[i] * np.log2(1 / probabilityPixels[i])
    print('Entropy pixel = ', entropyPixels)
    entropyImg = entropyPixels * len(pixelsColor)
    print('Entropy img = ', entropyImg)



Img()