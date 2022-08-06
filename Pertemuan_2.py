import numpy as np
# append: menambahkan angka ke dalam array
arr = np.arange(10)
print(np.append(arr, (10, 11, 12)))
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.append(arr2, [[7, 8, 9]], axis=0))  # menambah angka di kolom baru
print(np.append(arr2, [[1, 1, 1]], axis=0))  # menambah angka di kolom baru
print(np.append(arr2, [[0], [0]], axis=1))  # menambahkan angka di dalam tiap kolom
# concatenate: menggabungkan dua array
arr_a = np.array([[1, 2, 3],
                  [4, 5, 6]])
arr_b = np.array([[7, 8, 9],
                  [10, 11, 12]])
print(np.concatenate((arr_a, arr_b), axis=0))
print(np.concatenate((arr_a, arr_b), axis=1))
print(np.concatenate((arr_b, arr_a), axis=0))
print(np.concatenate((arr_b, arr_a), axis=1))
# sorting in numpy
from numpy import random
x = random.randint(1, 10, size=(10))
print(np.sort(x)) #dr kecil ke besar
print(np.sort(x)[::-1]) #dr besar ke kecil
# delete: menghapus angka dari array
y = np.array([[1, 2, 3], #0
              [4, 5, 6], #1
              [7, 8, 9]]) #2
print(np.delete(y, 1, axis=0)) #jangan lupa bahwa dalam bahasa pemograman semuanya berawal dari 0
print(np.delete(y, 2, axis=1)) #jangan lupa bahwa dalam bahasa pemograman semuanya berawal dari 0
# reshape
a = np.arange(10) # reshape cuma bisa direshape dalam bentuk perkalian yang hasilnya adalah jumlah angka awal
print(a.reshape(2,5)) # 2x5=10
# expanding dimensions
a_dim = np.expand_dims(a, axis=1) #menambah dimensi suatu array, data awal hanya 1-D namun skrg menjadi 2-D
a_dims = np.expand_dims(a, axis=0) #bentuk shape data akan bergantung dari axis
print(a_dim)
print(a_dims)
print(a_dim.reshape(2,5))
# access item memilih data yang kita mau tampilkan dari array
array = np.arange(10)
print(array)
print(array[4]) # jangan lupa, axis dimulai dari 0.
print(array[:4]) # mengambil angka 1 sampai 5 (jangan bingung karena axis dimulai dari 0)
print(array[3:]) # mengambil angka 4 sampai 5 (jangan bingung karena axis dimulai dari 0)
# selecting menuliskan angka dalam array yang memenuhi syarat
k = random.randint(1, 100, size=(20))
print(k)
print(k[k>45]) # menuliskan list angka yang lebih besar dari 45
print(k[k%2==0]) # % adalah lambang bagi,  jadi fungsi sebelah menuliskan angka kelipatan 2
# vstack vertikal stack, sama seperti concate axis = 0, namun disini tidak perlu menuliskan axis
a1 = np.array([[1,1],
              [2,2]])
a2 = np.array([[3,3],
              [4,4]])
a3 = np.vstack((a1,a2)) #pastikkan axis = 0 nya sama
print(a3)
#hstack horizontal stack, sama seperti concate axis = 1, namun disini tidak perlu menuliskan axis
b1 = np.array([[1,1],
              [2,2]])
b2 = np.array([[3,3],
              [4,4]])
b3 = np.hstack((b1,b2)) #pastikkan axis = 1 nya sama
print(b3)
#array operation melakukan operasi mtk dengan angka-angka di dalam array
a = np.array([1,2,3,4,5])
print(a.sum())
print(a[a.argmax()])
#masih belum bisa save dan load numpy penggunaan os dan csv