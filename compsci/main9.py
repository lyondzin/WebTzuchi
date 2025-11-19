# tebak angka
# import random,os,dan time
# buat variabel isinya random dari 1 sampe 10
# looping dimulai
# buat variabel input interger tebak
# jika variabel dibawah var random tebak maka
# outputnya tebakan terlalu tinggi
# jika variabel diatas var random tebak maka
# outputnya tebakan terlalu rendah
# jika tebak sama dengan var random
# outputnya tertebak! angkanya var random
# patahkan loopingnya


import random,os,time

a = random.randint(1, 10) 

while True:
    
    b = int(input("Masukkan angka tebakannya: "))

    if b < a:
        print("Tebakan terlalu rendah.")
    elif b > a:
        print("Tebakan terlalu tinggi.")
    else:
        print("Tebakanmu Benar!")
        time.sleep(2)
        os.system("cls")
        break 
