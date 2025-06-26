"""
PROGRAM RERATA
Nama : Elsa Aiziyah
NIM  : 21305144025
Kelas: Matematika E

Input: integer atau float
Output: rerata
"""
print("="*90)
a = "PROGRAM RERATA".center(90)
print(a)
print("="*90)
print("Catatan: Gunakan '.' untuk menuliskan desimal.")
def rerata():
    jumlah = 0
    banyak = 0
    banyak, jumlah = mulai(banyak, jumlah)

    try: 
        print(f"Rata-rata:  {round(jumlah/banyak,3)}")
        print(f"Banyak nilai yang telah dimasukkan adalah {banyak}")
    except ZeroDivisionError:
        print("Rata-ratanya tidak dapat dihitung karena belum memasukkan nilai. \nSilahkan masukan nilai lalu mulai kembali.")
def mulai(banyak, jumlah):
    lanjut = True
    while lanjut == True:
        nilai = input(f"Masukkan nilai ke-{banyak+1}: ")       
        if nilai == "":
            lanjut = False
        elif cek(nilai) == True:
            banyak += 1
            jumlah += float(nilai)
        else:
            print(f"{nilai} bukan nilai")
    return banyak, jumlah

def cek(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
rerata()