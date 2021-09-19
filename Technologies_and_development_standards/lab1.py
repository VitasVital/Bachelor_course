import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


operators = ['=', '[', '(']
f = open('program.txt', 'r')

l = [line.strip() for line in f]

for i in l:
    print(i)

for i in operators:
    print(i)