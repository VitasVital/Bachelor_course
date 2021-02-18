import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'

text = ''

with open('african_head.obj') as f:
    for i in f:
        text += i

splitText = text.split()
N = 1024
color = np.array([255, 255, 255], dtype=np.uint8)
img1 = np.zeros((N, N, 3), dtype=np.uint8)
img2 = np.zeros((N, N, 3), dtype=np.uint8)

A = np.array([2, 2, 2])
B = np.array([-2, -2, 0])
AB = np.array([A[0] - B[0], A[1] - B[1], A[2] - B[2]])


gamma = np.array([A[0] - B[0], A[1] - B[1], A[2] - B[2]])
gamma_norm = 1 / np.linalg.norm(gamma)
gamma = gamma * gamma_norm

beta = np.array([0, 1, 0]) - gamma[1] * gamma
beta_norm = 1 / np.linalg.norm(beta)
beta = beta * beta_norm

alpha = np.cross(beta, gamma)

rotation_matrix = np.array([[alpha[0], beta[0], gamma[0], 0],
                           [alpha[1], beta[1], gamma[1], 0],
                           [alpha[2], beta[2], gamma[2], 0],
                           [0, 0, 0, 1]])

print(rotation_matrix)

print(gamma)
print(beta)
print(alpha)

def bVec():
    b = np.array([0, 0])
    return b

def shiftMatr(c):
    mtr = np.array([[1, 0, 0, c[0]],
                    [0, 1, 0, c[1]],
                    [0, 0, 1, c[2]],
                    [0, 0, 0, 1]])
    return mtr

def rotMatrOx(ang):
    mtr = np.array([[1, 0, 0, 0],
                    [0, np.cos(ang), -np.sin(ang), 0],
                    [0, np.sin(ang), np.cos(ang), 0],
                    [0, 0, 0, 1]])
    return mtr

def rotMatrOy(ang):
    mtr = np.array([[np.cos(ang), 0, np.sin(ang), 0],
                    [0, 1, 0, 0],
                    [-np.sin(ang), 0, np.cos(ang), 0],
                    [0, 0, 0, 1]])
    return mtr

def rotMatrOz(ang):
    mtr = np.array([[np.cos(ang), -np.sin(ang), 0, 0],
                    [np.sin(ang), np.cos(ang), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return mtr

def resScale(res):
    mtr = np.array([[res[0], 0, 0, 0],
                    [0, res[1], 0, 0],
                    [0, 0, res[2], 0],
                    [0, 0, 0, 1]])
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

def Mproj(r, I, t, b, f, n):
    M = np.array([[2 / (r - I), 0, 0, -(r + I) / (r - I)],
                  [0, 2 / (t - b), 0, -(t + b) / (t - b)],
                  [0, 0, -2 / (f - n), -(f + n) / (f - n)],
                  [0, 0, 0, 1]])
    return M

def get_barycentric_coords(x, y, A, B, C):
    T = np.array([[A[0], B[0], C[0]],
                  [A[1], B[1], C[1]],
                  [1, 1, 1]])
    X = np.array([x, y, 1])
    V = np.linalg.inv(T) @ X.T
    return V

def normalize(Vec):
    Norm = np.linalg.norm(Vec)
    Vec = Vec * (1 / Norm)
    return Vec

vText = []
vtText = []
vnText = []
fText = []
i = 0
for i in range(len(splitText)):
    if splitText[i] == 'v':
        vText.append([float(splitText[i + 1]), float(splitText[i + 2]), float(splitText[i + 3])])
    if splitText[i] == 'vt':
        vtText.append([float(splitText[i + 1]), float(splitText[i + 2]), float(splitText[i + 3])])
    if splitText[i] == 'vn':
        vnText.append([float(splitText[i + 1]), float(splitText[i + 2]), float(splitText[i + 3])])
    if splitText[i] == 'f':
        fText.append([splitText[i + 1], splitText[i + 2], splitText[i + 3]])

centerX = 0
centerY = 0
centerZ = 0
maxCoord = abs(vText[0][1])
minCoord = abs(vText[0][1])
maxCoordX = abs(vText[0][1])
minCoordX = abs(vText[0][1])
maxCoordY = abs(vText[0][1])
minCoordY = abs(vText[0][1])
maxCoordZ = abs(vText[0][1])
minCoordZ = abs(vText[0][1])
for i in vText:
    centerX += i[0]
    centerY += i[1]
    centerZ += i[2]
    maxCoord = max(maxCoord, abs(i[0]), abs(i[1]), abs(i[2]))
    minCoord = min(minCoord, abs(i[0]), abs(i[1]), abs(i[2]))
    maxCoordX = max(maxCoordX, abs(i[0]))
    minCoordX = min(minCoordX, abs(i[0]))
    maxCoordY = max(maxCoordY, abs(i[1]))
    minCoordY = min(minCoordY, abs(i[1]))
    maxCoordZ = max(maxCoordZ, abs(i[2]))
    minCoordZ = min(minCoordZ, abs(i[2]))
centerX = int(centerX // len(vText))
centerY = int(centerY // len(vText))
centerZ = int(centerZ // len(vText))
lenX = maxCoordX - minCoordX
lenY = maxCoordY - minCoordY
lenZ = maxCoordZ - minCoordZ
center = [centerX, centerY, centerZ]
print('Center ', center)
print(maxCoord, ' ', minCoord)
print(maxCoordX, ' ', minCoordX)
print(maxCoordY, ' ', minCoordY)
print(maxCoordZ, ' ', minCoordZ)
print(lenX)
print(lenY)
print(lenZ)


for i in vText:
    coords = np.array([i[0], i[1], i[2], 1])

    angX = np.pi * 5 / 180
    angY = np.pi * 10 / 180
    angZ = np.pi * 15 / 180

    shift = [-1, 0, -2]
    res = [0.8, 0.8, 0.8]

    rotMatr = np.array(rotMatrOx(angX) @ rotMatrOy(angY) @ rotMatrOz(angZ))
    coords = np.array(shiftMatr(shift) @ rotMatr @ resScale(res)) @ coords

    Mw2c = rotation_matrix.T @ shiftMatr(A)
    coords = Mw2c @ coords

    coords = Mproj(maxCoordX, minCoordX, maxCoordY, minCoordY, maxCoordZ, minCoordZ) @ coords

    shift = [N // 2, N // 2, N // 2]
    res = [N // 5, N // 5, N // 5]
    coords = (shiftMatr(shift) @ resScale(res)) @ coords

    i[0] = coords[0]
    i[1] = coords[1]
    #i[2] = coords[2]


def DrawLine(x0, y0, x1, y1):
    flag = False
    if max(x0, x1) - min(x0, x1) < abs(y1 - y0):
        x0, y0, x1, y1 = y0, x0, y1, x1
        flag = True
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    delta = abs(y1 - y0)
    error = 0.0
    y = y0
    for x in range(x0, x1):
        if flag == False:
            img1[-1 * x, y] = color
        else:
            img1[-1 * y, x] = color
        error = error + abs(y1 - y0)
        if 2 * error >= abs(x1 - x0):
            y = y + np.sign(y1 - y0) * 1
            error = error - np.abs(x1 - x0)


def Bresenham(A, B, C):
    DrawLine(A[1], A[0], B[1], B[0])
    DrawLine(A[1], A[0], C[1], C[0])
    DrawLine(C[1], C[0], B[1], B[0])


fvText = []
fvtText = []
fvnText = []
for i in fText:
    vs = []
    vts = []
    vns = []
    countSlash = 0
    firstJ = 0
    for q in range(3):
        for j in range(len(i[q])):
            if i[q][j] == '/' and countSlash == 0:
                vs.append(i[q][:j])
                firstJ = j
                countSlash += 1
                continue
            if i[q][j] == '/' and countSlash == 1:
                vts.append(i[q][firstJ + 1:j])
                vns.append(i[q][j + 1:])
                countSlash += 1
        countSlash = 0
        firstJ = 0
    fvText.append(vs)
    fvtText.append(vts)
    fvnText.append(vns)

# def z_bufer():
#     z_buf = np.array(img.shape)
#     z_buf = np.ones(N, N)
#     for i in fvText:
#         A = vText[int(i[0]) - 1]
#         B = vText[int(i[1]) - 1]
#         C = vText[int(i[2]) - 1]
#
#     return 0

z_buf = np.ones((N, N))
def Rasterization(A, B, C):
    xmin = int(min(A[0], B[0], C[0]))
    xmax = int(max(A[0], B[0], C[0])) + 1
    ymin = int(min(A[1], B[1], C[1]))
    ymax = int(max(A[1], B[1], C[1])) + 1
    Norm = np.cross((B - A), (C - B))
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            V = get_barycentric_coords(x, y, A, B, C)
            if V[0] > 0 and V[1] > 0 and V[2] > 0:
                z = V[0] * A[2] + V[1] * B[2] + V[2] * C[2]
                if z < z_buf[N - y - 1, x]:
                    Vec = np.array([x, y, z])
                    color = np.dot(normalize(Vec) - normalize(A), Norm) * 255
                    img2[N - y - 1, x] = color
                    z_buf[N - y - 1, x] = z


for i in fvText:
    A = np.array(vText[int(i[0]) - 1])
    B = np.array(vText[int(i[1]) - 1])
    C = np.array(vText[int(i[2]) - 1])
    Rasterization(A, B, C)


for i in fvText:
    A = vText[int(i[0]) - 1]
    B = vText[int(i[1]) - 1]
    C = vText[int(i[2]) - 1]
    Bresenham(A, B, C)

plt.figure()
plt.imshow(img1)
plt.show()

plt.figure()
plt.imshow(img2)
plt.show()

plt.imsave('african_head1.png', img1)
plt.imsave('african_head2.png', img2)