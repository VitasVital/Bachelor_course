import numpy as np
import matplotlib.pyplot as plt

with open('teapot.obj') as f:
    text = ''
    for i in f:
        text += i

    splitText = text.split()
    N = 1000
    resizeScale = 140
    relocateImage = N // 2
    color = np.array([255, 255, 255], dtype=np.uint8)
    img = np.zeros((N, N, 3), dtype=np.uint8)

    vText = []
    fText = []
    i = 0
    while splitText[i] != 'f':
        vText.append(splitText[i])
        i += 1
    fText = splitText[i:len(splitText)]

    centerX = 0
    centerY = 0
    vCount = 0
    for i in range(len(vText)):
        if vText[i] == 'v':
            centerX += float(vText[i + 1])
            centerY += float(vText[i + 2])
            vCount += 1
    centerX = centerX // vCount
    centerY = centerY // vCount


    def DrawLine(x0, y0, x1, y1):
        flag = False
        if max(float(x0), float(x1)) - min(float(x0), float(x1)) < abs(float(y1) - float(y0)):
            x0, y0, x1, y1 = y0, x0, y1, x1
            flag = True
        if float(x0) > float(x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x0 = int(float(x0) * resizeScale) + relocateImage
        y0 = int(float(y0) * resizeScale) + relocateImage
        x1 = int(float(x1) * resizeScale) + relocateImage
        y1 = int(float(y1) * resizeScale) + relocateImage
        delta = abs(y1 - y0)
        error = 0.0
        y = y0
        for x in range(x0, x1):
            if flag == False:
                img[-1 * x, y] = color
            else:
                img[-1 * y, x] = color
            error = error + abs(y1 - y0)
            if 2 * error >= abs(x1 - x0):
                y = y + np.sign(y1 - y0) * 1
                error = error - np.abs(x1 - x0)


    def Bresenham(A, B, C):
        DrawLine(A[0], A[1], B[0], B[1])
        DrawLine(A[0], A[1], C[0], C[1])
        DrawLine(C[0], C[1], B[0], B[1])

    def SearchCoordinates(a, b, c, vText):
        A = [vText[int(a) * 4 - 2], vText[int(a) * 4 - 3]]
        B = [vText[int(b) * 4 - 2], vText[int(b) * 4 - 3]]
        C = [vText[int(c) * 4 - 2], vText[int(c) * 4 - 3]]
        return [A, B, C]


    for i in range(len(fText)):
        if fText[i] == 'f':
            Coordinates = SearchCoordinates(fText[i + 1], fText[i + 2], fText[i + 3], vText)
            A = Coordinates[0]
            B = Coordinates[1]
            C = Coordinates[2]
            Bresenham(A, B, C)

    plt.figure()
    plt.imshow(img)
    plt.show()

    plt.imsave('teapot_image.png', img)
