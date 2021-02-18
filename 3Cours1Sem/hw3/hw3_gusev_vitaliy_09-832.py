import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'

def bVec():
    b = np.array([0, 0])
    return b

def shiftMatr(vec):
    mtr = np.array([[1, 0, vec[0]], [0, 1, vec[1]], [0, 0, 1]])
    return mtr

def rotMatr(ang):
    mtr = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
    return mtr

# def rotMatr(ang):
#     mtr = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
#     return mtr

def to_proj_coords(x):
    r,c = x.shape
    x = np.concatenate([x, np.ones((1,c))], axis = 0)
    return x

def to_cart_coords(x):
    x = x[:-1]/x[-1]
    return x

def set_color(img, x, y, color):
    img[x, y, :3] = color
    return img

text = ''

with open('teapot.obj') as f:
    for i in f:
        text += i

splitText = text.split()
N = 1000
resizeScale = 40
relocateImage = N // 2
red = 255
green = 0
blue = 0
color = np.array([red, green, blue], dtype=np.uint8)
framesCount = 100  # frames count
frames = []
fig = plt.figure()


vText = []
fText = []
i = 0
while splitText[i] != 'f':
    vText.append(splitText[i])
    i += 1
fText = splitText[i:len(splitText)]


def DrawLine(x0, y0, x1, y1, img):
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
            set_color(img, -1 * x, y, color)
        else:
            set_color(img, -1 * y, x, color)
        error = error + abs(y1 - y0)
        if 2 * error >= abs(x1 - x0):
            y = y + np.sign(y1 - y0) * 1
            error = error - np.abs(x1 - x0)


def Bresenham(A, B, C, img):
    DrawLine(A[0], A[1], B[0], B[1], img)
    DrawLine(A[0], A[1], C[0], C[1], img)
    DrawLine(C[0], C[1], B[0], B[1], img)

def SearchCoordinates(a, b, c, vText):
    A = [float(vText[int(a) * 4 - 2]), float(vText[int(a) * 4 - 3])]
    B = [float(vText[int(b) * 4 - 2]), float(vText[int(b) * 4 - 3])]
    C = [float(vText[int(c) * 4 - 2]), float(vText[int(c) * 4 - 3])]
    return [A, B, C]

centerX = 0
centerY = 0
vCount = 0
for i in range(len(vText)):
    if vText[i] == 'v':
        centerX += float(vText[i + 1])
        centerY += float(vText[i + 2])
        vCount += 1
centerX = int(centerX // vCount)
centerY = int(centerY // vCount)
center = [centerX, centerY]

for i in range(len(vText)):
    if vText[i] == 'v':
        vText[i + 1] = float(vText[i + 1]) - centerX
        vText[i + 2] = float(vText[i + 2]) - centerY

centerImg = [-N // 2, -N // 2]

def DrawImage():
    img = np.zeros((N, N, 3), dtype=np.uint8)

    for i in range(len(vText)):
        if vText[i] == 'v':
            rotV = [float(vText[i + 1]), float(vText[i + 2]), 1]
            ang = 2 * np.pi / rotFrames
            rotV = rotMatr(ang) @ rotV
            vText[i + 1] = rotV[0]
            vText[i + 2] = rotV[1]

    # draw line
    for i in range(len(fText)):
        if fText[i] == 'f':
            Coordinates = SearchCoordinates(fText[i + 1], fText[i + 2], fText[i + 3], vText)
            A = Coordinates[0]
            B = Coordinates[1]
            C = Coordinates[2]
            Bresenham(A, B, C, img)
    im = plt.imshow(img)
    frames.append([im])

rotCount = 0
parityRotation = False
rotFrames = 40
for j in range(framesCount):
    if rotCount == rotFrames and parityRotation == False:
        rotCount = 0
        parityRotation = True
    elif rotCount == rotFrames and parityRotation == True:
        rotCount = 0
        parityRotation = False
    if parityRotation == False:
        red -= 5
        green += 5
        resizeScale += 1
    else:
        red += 5
        green -= 5
        resizeScale -= 1
    color = np.array([red, green, blue], dtype=np.uint8)
    DrawImage()
    rotCount += 1

print('Frames creation finshed.')

ani = animation.ArtistAnimation(fig, frames, interval=40, blit=True, repeat_delay=0)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=1800)
ani.save('teapot.mp4', writer)
# ani.save('simple_animation.mp4')

# gif animation creation
ani = animation.ArtistAnimation(fig, frames, interval=40, blit=True, repeat_delay=0)
writer = PillowWriter(fps=24)
ani.save("teapot.gif", writer=writer)

plt.show()