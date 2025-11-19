import os,random,time

a = random.randint(1,9)
b = random.randint(10,99)
c = random.randint(100,999)

while True:
    os.system("cls")
    print('''Selamat Datang di Math QUIZ
          1.Easy
          2.Medium
          3.Hard''')
    print(f"{a} + {b}")
    jawab = int(input('jawabannya berapa?'))

    if jawab == a+b:
        os.system("cls")
        print("benar")
        print(f"hasilnya adalah = {a+b}")
        break
    else:
        os.system("cls")
        print("jawaban anda salah!")
        print("coba lagi!")
        time.sleep(2)
        continue
