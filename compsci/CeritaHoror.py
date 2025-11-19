# nested = bersarang
# di dalam if / elif / else ada conditional

print("Malam itu di 12 PPLG 1, kamu  sendirian ngerjain tugas.")
print("Lampu berkedip dan terdengar suara langkah dari lorong.")
print("1. Mengecek keluar kelas")
print("2. Bersembunyi di bawah meja")
choice = int(input("= "))

if choice == 1:
    print("Kamu keluar kelas, lorong gelap dan dingin.")
    print("Tiba-tiba ada bayangan tinggi di ujung lorong.")
    print("1. Mendekati bayangan itu")
    print("2. Terus mundur pelan-pelan")
    choice = int(input("= "))
    
    if choice == 1:
        print("Ketika kamu mendekat, bayangan itu berubah menjadi sosok berwujud kabut.")
        print("Dia berbisik namamu…")
        print("1. Menjawab 'iya?'")
        print("2. Lari balik ke kelas")
        choice = int(input("= "))
        
        if choice == 1:
            print("Kabut itu mendekat dan memperlihatkan wajahmu sendiri.")
            print("'Aku adalah kamu yang tidak pernah pulang,' katanya.")
            print("Kamu pingsan seketika dan terbangun di UKS.")
        elif choice == 2:
            print("Kamu berlari secepat mungkin.")
            print("Saat menutup pintu kelas, kabut itu menabrak pintu dan menghilang.")
            print("Kamu selamat untuk sementara.")
    
    elif choice == 2:
        print("Kamu mundur pelan tapi lantai tiba-tiba berderit keras.")
        print("Bayangan itu melihatmu dan mendekat cepat.")
        print("1. Mengambil sapu untuk melawan")
        print("2. Menutup mata dan berharap hilang")
        choice = int(input("= "))

        if choice == 1:
            print("Kamu mengayunkan sapu, ternyata bayangan itu hanya jaket yang tergantung.")
            print("Tepat setelah kamu lega ada tangan dingin yang menyentuh bahumu dari belakang.")
        elif choice == 2:
            print("Saat kamu buka mata, bayangannya hilang.")
            print("Tapi kini kamu sedang berdiri di lapangan tanpa tahu bagaimana kamu berpindah ke sana.")
            print("Angin berbisik namamu…")

elif choice == 2:
    print("Kamu sembunyi di bawah meja, berharap suara langkah itu pergi.")
    print("Namun suara itu berhenti tepat di depan kelas.")
    print("1. Mengintip dari bawah meja")
    print("2. Tetap diam")
    choice = int(input("= "))

    if choice == 1:
        print("Kamu mengintip dan melihat kaki seseorang… tanpa bayangan.")
        print("1. Berteriak minta tolong")
        print("2. Merangkak pelan ke pintu belakang")
        choice = int(input("= "))

        if choice == 1:
            print("Sosok itu membungkuk dan menatap balik ke bawah meja.")
            print("Ia tersenyum terlalu lebar.")
            print("Kamu langsung pingsan.")
        elif choice == 2:
            print("Kamu berhasil ke pintu belakang.")
            print("Saat membuka pintu sosok itu sudah menunggu di baliknya.")
            print("DIaa berkata, 'Giliranmu jaga sekolah malam ini.'")

    elif choice == 2:
        print("Kamu tetap diam, menahan napas.")
        print("Suara langkah itu pergi tapi digantiin suara seret di langit-langit kelas.")
        print("Kamu menatap ke atas. Ada wajah pucat menatapmu terbalik dari langit-langit.")
        print("Kamu langsung pingsan.")
