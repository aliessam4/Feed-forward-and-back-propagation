import numpy as np

np.random.seed(0)

x = np.array([1, 0])

W1 = np.random.uniform(-0.5, 0.5, (2, 2))
W2 = np.random.uniform(-0.5, 0.5, (2, 1))

b1 = 0.5
b2 = 0.7

z1 = np.dot(x, W1) + b1
a1 = np.tanh(z1)

z2 = np.dot(a1, W2) + b2
output = np.tanh(z2)

print("Network Output:")
print(output)