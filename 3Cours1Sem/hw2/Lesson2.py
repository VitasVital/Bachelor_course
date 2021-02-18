import numpy as np
import matplotlib.pyplot as plt
print(np.__version__)

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.figure()
plt.plot(x, y)
plt.show()
#доделать
#---------------

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.subplot(1, 2, 2)
plt.plot(x, z)
plt.show()

#------------------

N = 1024
color = np.array([255, 255, 255], dtype = np.uint8)
img = np.zeros((N, N, 3), dtype = np.uint8)
img[200:800, 200:800] = color

plt.figure()
plt.imshow(img)
plt.show()

plt.imsave('simple_image.png', img)