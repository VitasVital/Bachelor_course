import json
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg.exe'

f = open('digits.json', 'r')
digits = json.load(f)
f.close()

# x = np.random.randint(50, 800, 10)
# x = np.sort(x)
# print(x)
# y = np.random.randint(50, 800, 10)
# print(y)
#
#d = 20 * np.random.rand(10) - 10

def set_color(img, x, y, color):
    img[x, y, :3] = color
    return img

N = 600
color = np.array([0, 255, 0], dtype=np.uint8)
img = np.zeros((N, N, 3), dtype=np.uint8)
frames = []
fig = plt.figure()

def DrawLine(x0, y0, x1, y1, img):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    flag = False
    if max(float(x0), float(x1)) - min(float(x0), float(x1)) < abs(float(y1) - float(y0)):
        x0, y0, x1, y1 = y0, x0, y1, x1
        flag = True
    if float(x0) > float(x1):
        x0, y0, x1, y1 = x1, y1, x0, y0
    delta = abs(y1 - y0)
    error = 0.0
    y = y0
    for x in range(x0, x1):
        if flag == False:
            #set_color(img, -1 * (x0 + x), y, color)
            img[x, y] = color
        else:
            #set_color(img, -1 * y, x0 + x, color)
            img[y, x] = color
        error = error + abs(y1 - y0)
        if 2 * error >= abs(x1 - x0):
            y = y + np.sign(y1 - y0) * 1
            error = error - np.abs(x1 - x0)

def deCasteljau(P, t, n):
    for i in range(1, n):
        for j in range(n - i):
            P[j][0] = (1 - t) * P[j][0] + t * P[j + 1][0]
            P[j][1] = (1 - t) * P[j][1] + t * P[j + 1][1]
    return P[0]

# for i in range(9):
#     m = np.array([[1, x[i], x[i] ** 2, x[i] ** 3],
#                   [1, x[i + 1], x[i + 1] ** 2, x[i + 1] ** 3],
#                   [0, 1, 2 * x[i], 3 * (x[i] ** 2)],
#                   [0, 1, 2 * x[i + 1], 3 * (x[i + 1] ** 2)]])
#
#     b = np.array([y[i], y[i + 1], d[i], d[i + 1]])
#     a = np.linalg.inv(m).dot(b)
#     for xi in range(x[i], x[i + 1], 1):
#         y1 = a[0] + a[1] * xi + a[2] * xi ** 2 + a[3] * xi ** 3
#         y2 = a[0] + a[1] * (xi + 1) + a[2] * (xi + 1) ** 2 + a[3] * (xi + 1) ** 3
#         DrawLine(y1, xi, y2, (xi + 1), img)

# def DrawSegment(coords):
#     x = []
#     y = []
#     for i in range(len(coords)):
#         x.append(int(coords[i][0]))
#         y.append(int(coords[i][1]))
#     for i in range(len(coords) - 1):
#         m = np.array([[1, x[i], x[i] ** 2, x[i] ** 3],
#                       [1, x[i + 1], x[i + 1] ** 2, x[i + 1] ** 3],
#                       [0, 1, 2 * x[i], 3 * (x[i] ** 2)],
#                       [0, 1, 2 * x[i + 1], 3 * (x[i + 1] ** 2)]])
#         for xi in range(x[i], x[i + 1], 1):
#             b = np.array([y[i], y[i + 1], d[i], d[i + 1]])
#             a = np.linalg.inv(m).dot(b)
#             y1 = a[0] + a[1] * xi + a[2] * xi ** 2 + a[3] * xi ** 3
#             y2 = a[0] + a[1] * (xi + 1) + a[2] * (xi + 1) ** 2 + a[3] * (xi + 1) ** 3
#             DrawLine(y1, xi, y2, (xi + 1), img)

digitNames = ['digit_0', 'digit_1', 'digit_2', 'digit_3', 'digit_4', 'digit_5', 'digit_6', 'digit_7', 'digit_8', 'digit_9']
segmentNames = ['segment_0', 'segment_1', 'segment_2', 'segment_3']
digits_copy = copy.deepcopy(digits)

# T = [i / 10 for i in range(10)]
# t = [i / 1000 for i in range(1000)]
# for dig in range(1, len(digitNames)):
#     for j in T:
#         img = np.zeros((N, N, 3), dtype=np.uint8)
#         P = []
#         for seg in range(len(segmentNames)):
#             control_points_coordsA = digits[digitNames[dig - 1]][segmentNames[seg]]
#             control_points_coordsB = digits[digitNames[dig]][segmentNames[seg]]
#             control_points_coordsC = control_points_coordsA
#             for i in range(len(control_points_coordsC)):
#                 control_points_coordsC[i][0] = control_points_coordsA[i][0] * (1 - j) + control_points_coordsB[i][0] * (j)
#                 control_points_coordsC[i][1] = control_points_coordsA[i][1] * (1 - j) + control_points_coordsB[i][1] * (j)
#             for i in t:
#                 rezP = deCasteljau(control_points_coordsC, i, 4)
#                 P.append(copy.copy(rezP))
#         for i in range(len(P)-1):
#             DrawLine(P[i][1], P[i][0], P[i + 1][1], P[i + 1][0], img)
#         im = plt.imshow(img)
#         frames.append([im])
#     digits = copy.deepcopy(digits_copy)

T = [i / 20 for i in range(20)]
t = [i / 1000 for i in range(1000)]
digits_line = []

# for dig in digitNames:
#     P = []
#     for seg in segmentNames:
#         for i in t:
#             control_points_coords = digits[dig][seg]
#             rezP = deCasteljau(control_points_coords, i, 4)
#             P.append(copy.copy(rezP))
#     digits_line.append(P)

def Make_digit_lines():
    digits_line.clear()
    for dig in range(len(digitNames)):
        P = []
        for seg in segmentNames:
            for i in t:
                control_points_coords = digits[digitNames[dig]][seg]
                rezP = deCasteljau(control_points_coords, i, 4)
                P.append(copy.copy(rezP))
        digits_line.append(P)
    P = []
    for seg in segmentNames:
        for i in t:
            control_points_coords = digits_copy['digit_0'][seg]
            rezP = deCasteljau(control_points_coords, i, 4)
            P.append(copy.copy(rezP))
    digits_line.append(P)

Make_digit_lines()

for i in range(len(digits_line) - 1):
    for j in T:
        img = np.zeros((N, N, 3), dtype=np.uint8)
        dig_A = digits_line[i]
        dig_B = digits_line[i + 1]
        dig_C = []
        for coords in range(len(dig_A)):
            control_points_coords_A = [dig_A[coords][0], dig_A[coords][1]]
            control_points_coords_B = [dig_B[coords][0], dig_B[coords][1]]
            control_points_coords_C = control_points_coords_A
            control_points_coords_C[0] = control_points_coords_A[0] * (1 - j) + control_points_coords_B[0] * (j)
            control_points_coords_C[1] = control_points_coords_A[1] * (1 - j) + control_points_coords_B[1] * (j)
            dig_C.append([control_points_coords_C[0], control_points_coords_C[1]])
        for draw in range(len(dig_C) - 1):
            DrawLine(dig_C[draw][1], dig_C[draw][0], dig_C[draw + 1][1], dig_C[draw + 1][0], img)
        im = plt.imshow(img)
        frames.append([im])



print('Frames creation finshed.')

ani = animation.ArtistAnimation(fig, frames, interval=40, blit=True, repeat_delay=0)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=1800)
ani.save('digits_animation.mp4', writer)
# ani.save('simple_animation.mp4')

# gif animation creation
ani = animation.ArtistAnimation(fig, frames, interval=40, blit=True, repeat_delay=0)
writer = PillowWriter(fps=24)
ani.save("digits_animation.gif", writer=writer)

plt.show()