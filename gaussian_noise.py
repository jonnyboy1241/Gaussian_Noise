# python3 gaussian_noise.py x_min, x_max, num_points, std_dev

import numpy as np
import sys
import time




def generate_data(x_min, x_max, num_points, std_dev):
    # Make stuff very random
    np.random.seed(int(time.time()))

    # Generate Gaussian Noise, Mean is always 0
    noise = np.random.normal(0, float(std_dev), num_points)

    x = (x_max - x_min) * np.random.random_sample(num_points) + x_min

    # SPECIFIY BASE FUNCTION HERE
    y = (np.sin(3*x-np.pi/2)) + noise

    return x, y

# Allow script to run from command line
if __name__ == '__main__':
    x_min = np.float64(sys.argv[1])
    x_max = np.float64(sys.argv[2])
    num_points = np.int(sys.argv[3])
    std_dev = np.float64(sys.argv[4])

    x_values, y_values = generate_data(x_min, x_max, num_points, std_dev)

    for i in range(0, num_points):
        print(x_values[i], y_values[i])
