#Aplikasi hitung luas segitiga pak qibar
#Code Owner: Evan Fersadi

def count_triangle_wide(base, height):
    """Menghitung luas segitiga berdasarkan alas dan tinggi."""
    return 0.5 * base * height

def take_input():
    while True:
     prompt: int = input("Masukkan alas dan tinggi segitiga (pisahkan dengan koma): ")  
     prompt: str = prompt.split(",")
     base_and_height: int = list(map(int, prompt))
     wide = count_triangle_wide(base_and_height[0], base_and_height[1])
     print ("Luas segitiga adalah: ", wide)

take_input()