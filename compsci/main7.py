# OS, Time
# OS = Ngaturin terminal
# Time = Ngaturin waktu untuk tampil

import time,os

angka = 0
while angka < 5:
    print("Level",angka)
    time.sleep(2) #menambahkan delay
    os.system("cls") #menghilangkan tampilan keatas
    angka = angka + 1