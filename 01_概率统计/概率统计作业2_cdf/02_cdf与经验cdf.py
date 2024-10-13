import numpy as np
from matplotlib import pyplot as plt
import random
from math import log

def empirical_cdf(data):
    x = np.sort(data)
    n = len(x)
    y = np.arange(1, n+1) / n
    return x, y

def plot_empirical_cdf(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Samples')
    plt.ylabel('Empirical CDF')
    plt.title('Empirical CDF Plot')
    plt.show()

# 逆变换采样
samples = [random.uniform(0, 1) for i in range(100000)]
b, u = 0.5, 2

for sample in samples:
    if sample < 1/2:
        sample = u + b*log(sample*2)
    else:
        sample = u - 2*log(2 - sample*2)

# 绘制经验cdf
x, y = empirical_cdf(samples)
plot_empirical_cdf(x, y)
