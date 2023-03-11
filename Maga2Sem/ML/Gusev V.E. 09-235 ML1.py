import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/top 100 streamed songs.csv').drop(columns=['id', 'name'])

training_samples = data.values[:80]
validation_sapmles = data.values[80:90]
test_samples = data.values[90:100]

def weight(input_y, design_matrix):
    return input_y.T @ design_matrix.T @ np.linalg.inv(design_matrix @ design_matrix.T)

def design_matrix(samples):
    return samples.T

def calculate_a(samples, w):
    return samples @ w.T

def calculate_RMSE(input_a, input_y):
    MSE = sum((input_a - input_y) ** 2) / len(input_y)
    RMSE = np.sqrt(MSE)
    return RMSE

training_y = data['duration'][:80]
test_y = data['duration'][80:90]
dm = design_matrix(training_samples)
w = weight(training_y, dm)
a = calculate_a(test_samples, w)
RMSE = calculate_RMSE(a, test_y)
print(training_y)
print(RMSE)