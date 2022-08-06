import numpy as np
#soal 1
a = np.zeros((4,4))
print("array awal:\n", a)
a += np.arange(4)
print("Soal 1:\n", a)
#soal 2
x = np.arange(8).reshape((2, 4))
y = np.arange(8, 16).reshape((2, 4))
z = np.hstack((x,y))
print("array awal:\n", x, "\n", y)
print("Soal 2:\n", z)