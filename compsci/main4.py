def KTP() :
    limit: int = 122
    minimum: int = 17
    while True:
        umur = int(input("Masukkan umur anda: "))
        if umur >= minimum and umur <= limit:
            print("Anda sudah boleh membuat KTP")
        elif umur > limit:
            print("Tolong siapkan kain kafan")
        else:
            print("Anda belum boleh membuat KTP")

KTP()