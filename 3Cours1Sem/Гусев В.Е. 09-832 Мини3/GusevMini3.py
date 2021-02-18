import numpy as np
from PIL import Image, ImageDraw
import heapq
from collections import Counter
from collections import namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

img = Image.open('picture.png')
pixelsColor = []
(width, height) = img.size
img = img.load()
for i in range(width):
    for j in range(height):
        pixelsColor.append(img[i, j])
print('Number of pixels = ', len(pixelsColor))

X = []
for i in range(256):
    X.append(img[128, i])
print('Center pixels ', X)

for i in range(len(X)):
    X[i] = round(X[i]/20) * 20
print('Pixels after round ', X)

unic_pixels = list(set(X))
print('Unic pixels ', unic_pixels)
frequency_symbol = []
for i in unic_pixels:
    count = 0
    for j in X:
        if i == j:
            count += 1
    frequency_symbol.append(count)
print('Frequency symbols', frequency_symbol)

code = huffman_encode(X)
encoded = "".join(code[ch] for ch in X)
print('Len code = ', len(code))
print('Len of the encoded string = ', len(encoded))
for ch in sorted(code):
    print("{}: {}".format(ch, code[ch]))
print('Encoded digital sequence ', encoded)

average_len_of_Huffman_code = 0
for i in code:
    average_len_of_Huffman_code += len(code[i])
average_len_of_Huffman_code = average_len_of_Huffman_code / len(code)
print('The average length of Huffman code = ', average_len_of_Huffman_code)

entropy = 0
probabilityPixels = [frequency_symbol[i]/256 for i in range(len(frequency_symbol))]
print('Probability pixels ', probabilityPixels)

for i in probabilityPixels:
    entropy += i * np.log2(1 / i)
print('Entropy ', entropy)

coding_efficiency = entropy / average_len_of_Huffman_code
print('Coding efficiency = ', coding_efficiency)