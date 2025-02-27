import math

def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def pangkat(a, b): return a ** b
def akar(x):
    if x < 0:
        return "Error: Tidak dapat menghitung akar kuadrat dari bilangan negatif."
    return math.sqrt(x)

def modulus(a, b): return a % b
def faktorial(x):
    if x < 0:
        return "Error: Faktorial hanya dapat dihitung untuk bilangan bulat positif."
    return math.factorial(int(x))

def logaritma(x):
    if x <= 0:
        return "Error: Logaritma hanya dapat dihitung untuk bilangan positif."
    return math.log10(x)

def sin_trig(x, mode): return math.sin(math.radians(x)) if mode == "deg" else math.sin(x)
def cos_trig(x, mode): return math.cos(math.radians(x)) if mode == "deg" else math.cos(x)
def tan_trig(x, mode): return math.tan(math.radians(x)) if mode == "deg" else math.tan(x)

def tampilkan_menu():
    print("\n" + "=" * 30)
    print("KALKULATOR ILMIAH")
    print("=" * 30)
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Pangkat (^)")
    print("6. Akar Kuadrat (√x)")
    print("7. Modulus (%)")
    print("8. Faktorial (x!)")
    print("9. Logaritma Basis 10 (log10)")
    print("10. Sinus (sin)")
    print("11. Cosinus (cos)")
    print("12. Tangen (tan)")
    print("13. Keluar")
    print("=" * 30)

def validasi_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Harap masukkan angka yang valid.")

def validasi_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Harap masukkan bilangan bulat yang valid.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-13): ").strip()

        if pilihan == "13":
            print("Terima kasih telah menggunakan kalkulator ini!")
            break

        if pilihan in ["1", "2", "3", "4", "5", "7"]:
            a = validasi_float("Masukkan angka pertama: ")
            b = validasi_float("Masukkan angka kedua: ")
        elif pilihan in ["6", "8", "9", "10", "11", "12"]:
            a = validasi_float("Masukkan angka: ")
        else:
            print("Error: Pilihan tidak valid. Harap pilih angka 1-13.")
            continue

        if pilihan == "1":
            print(f"Hasil: {a} + {b} = {tambah(a, b)}")
        elif pilihan == "2":
            print(f"Hasil: {a} - {b} = {kurang(a, b)}")
        elif pilihan == "3":
            print(f"Hasil: {a} × {b} = {kali(a, b)}")
        elif pilihan == "4":
            print(f"Hasil: {a} ÷ {b} = {bagi(a, b)}")
        elif pilihan == "5":
            print(f"Hasil: {a}^{b} = {pangkat(a, b)}")
        elif pilihan == "6":
            print(f"Hasil: √{a} = {akar(a)}")
        elif pilihan == "7":
            print(f"Hasil: {a} % {b} = {modulus(a, b)}")
        elif pilihan == "8":
            print(f"Hasil: {int(a)}! = {faktorial(a)}")
        elif pilihan == "9":
            print(f"Hasil: log10({a}) = {logaritma(a)}")
        elif pilihan in ["10", "11", "12"]:
            mode = input("Pilih mode (deg/rad): ").strip().lower()
            if mode not in ["deg", "rad"]:
                print("Error: Mode harus 'deg' atau 'rad'.")
                continue
            if pilihan == "10":
                print(f"Hasil: sin({a}) = {sin_trig(a, mode)}")
            elif pilihan == "11":
                print(f"Hasil: cos({a}) = {cos_trig(a, mode)}")
            elif pilihan == "12":
                print(f"Hasil: tan({a}) = {tan_trig(a, mode)}")

        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
