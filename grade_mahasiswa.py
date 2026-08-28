nama = input("nama mahasiswa: ")
Nilai = int(input("masukkan nilainya: "))

if (Nilai >= 90):
    print(f"Grade {nama} adalah A")
elif (Nilai >= 80):
    print(f"Grade {nama} adalah B")
elif (Nilai >= 70):
    print(f"Grade {nama} adalah C")
elif (Nilai >= 60):
    print(f"Grade {nama} adalah D-")
elif (Nilai < 60):
    print(f"Grade {nama} adalah E") 