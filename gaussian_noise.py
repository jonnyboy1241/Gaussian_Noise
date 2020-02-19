# python3 gaussian_noise.py x_min, x_max, num_points, std_dev, function

import numpy as np, time, sys

# Make stuff very random
np.random.seed(int(time.time()))

x_min = np.float64(sys.argv[1])
x_max = np.float64(sys.argv[2])
num_points = np.int(sys.argv[3])
std_dev = np.float64(sys.argv[4])

# Generate Gaussian Noise, Mean is always 0
noise = np.random.normal(0, float(std_dev), num_points)

x_values = (x_max - x_min) * np.random.random_sample(num_points) + x_min

# SPECIFIY BASE FUNCTION HERE
y_values = 2 * x_values**2 + 3 * x_values + 4

for i in range(0, num_points):
    print(x_values[i], y_values[i])
