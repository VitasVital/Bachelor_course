from numpy import *

with open('hw2/teapot.obj') as f:
    text = ''
    for i in f:
        text += i

    vCount = 0
    for i in text:
        if i == 'v':
            vCount += 1
    print('Number of vertices = ', vCount)

    fCount = 0
    for i in text:
        if i == 'f':
            fCount += 1
    print('Number of sides = ', fCount)

    print('Total number of vertices and sides = ', vCount + fCount)

    # --------------------------------------------------------------------------------

    splitText = text.split()
    xMin = splitText[1]
    xMax = splitText[1]
    yMin = splitText[2]
    yMax = splitText[2]
    zMin = splitText[3]
    zMax = splitText[3]
    for i in range(len(splitText)):
        if splitText[i] == 'v':
            if float(splitText[i + 1]) > float(xMax):
                xMax = splitText[i + 1]
            if float(splitText[i + 1]) < float(xMin):
                xMin = splitText[i + 1]

            if float(splitText[i + 2]) > float(yMax):
                yMax = splitText[i + 2]
            if float(splitText[i + 2]) < float(yMin):
                yMin = splitText[i + 2]

            if float(splitText[i + 3]) > float(zMax):
                zMax = splitText[i + 3]
            if float(splitText[i + 3]) < float(zMin):
                zMin = splitText[i + 3]

    print("\nxMin = ", xMin, "\nxMax = ", xMax, "\nyMin = ", yMin,
          "\nyMax = ", yMax, "\nzMin = ", zMin, "\nzMax = ", zMax)

    # ----------------------------------------------------------------------------------------------

    def AreaTriangle(a, b, c):
        AB = [float(b[0]) - float(a[0]), float(b[1]) - float(a[1]), float(b[2]) - float(a[2])]
        AC = [float(c[0]) - float(a[0]), float(c[1]) - float(a[1]), float(c[2]) - float(a[2])]
        ABxAC = [float(AB[1]) * float(AC[2]) - float(AB[2]) * float(AC[1]),
                 float(AB[0]) * float(AC[2]) - float(AB[2]) * float(AC[0]),
                 float(AB[0]) * float(AC[1]) - float(AB[1]) * float(AC[0])]
        S = 1 / 2 * sqrt(ABxAC[0] ** 2 + ABxAC[1] ** 2 + ABxAC[2] ** 2)
        return S


    def SearchCoordinates(a, b, c, vText):
        A = [vText[int(a) * 4 - 3], vText[int(a) * 4 - 2], vText[int(a) * 4 - 1]]
        B = [vText[int(b) * 4 - 3], vText[int(b) * 4 - 2], vText[int(b) * 4 - 1]]
        C = [vText[int(c) * 4 - 3], vText[int(c) * 4 - 2], vText[int(c) * 4 - 1]]
        return [A, B, C]


    vText = []
    fText = []
    S = 0
    i = 0
    while splitText[i] != 'f':
        vText.append(splitText[i])
        i += 1
    fText = splitText[i:len(splitText)]
    for i in range(len(fText)):
        if fText[i] == 'f':
            Coordinates = SearchCoordinates(fText[i + 1], fText[i + 2], fText[i + 3], vText)
            A = Coordinates[0]
            B = Coordinates[1]
            C = Coordinates[2]
            S += AreaTriangle(A, B, C)
    print('\nTeapot area = ', S)
