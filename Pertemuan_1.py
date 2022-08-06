import numpy as np #supaya g ush panjang2 nulis numpy.array
from numpy import random
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a+b) #print(a*b) gbs
a_array = np.array(a)
b_array = np.array(b)
print(a_array+b_array)
print(a_array*b_array)
x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x.shape) #menghitung "bentuk" rangkaian data
print(y.shape) #menghitung "bentuk" rangkaian data
print(y.size) #menghitung jumlah data
print(x.size) #menghitung jumlah data
print(type(y)) #tipe data adalah np.array
zeros_matrix1 = np.zeros(5) #membuat sebuah matrix isinya angka 0 dengan ukuran data 1-D
print(zeros_matrix1)
zeros_matrix2 = np.zeros((5,2)) #membuat sebuah matrix isinya angka 0 dengan ukuran data 2-D
print(zeros_matrix2)
zeros_matrix3 = np.zeros((2,3,4)) #membuat sebuah matrix isinya angka 0 dengan ukuran data 3-D
print(zeros_matrix3)
ones_matrix1 = np.ones(5) #membuat sebuah matrix isinya angka 1 dengan ukuran data 1-D
print(ones_matrix1)
ones_matrix2 = np.ones((5,2)) #membuat sebuah matrix isinya angka 1 dengan ukuran data 2-D
print(ones_matrix2)
ones_matrix3 = np.ones((2,3,4)) #membuat sebuah matrix isinya angka 1 dengan ukuran data 3-D
print(ones_matrix3)
a = np.arange(10) #mengurutkan angka 0-9
b = np.arange(10,20) #mengurutkan angka dari 10-19
c = np.arange(10,20,2) #mengurutkan angka dari 10-19 dengan kelipatan 2
print(a)
print(b)
print(c)
print(a + b) #menambahkan data array a dan b
print(type(c)) #tipe data hasil arange adalah array
print(type(a)) #tipe data hasil arange adalah array
print(type(b)) #tipe data hasil arange adalah array
print(np.linspace(0,10,5)) #mengurutkan angka dari 0-10, 5 data yang selisih dari tiap datanya sama)
print(np.linspace(0,10,2))
print(random.rand(3,4,5))
print(random.rand(2,3,4))
print(random.randint(2, 10, size=(4,5)))
