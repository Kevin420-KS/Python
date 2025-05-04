import re
from fractions import Fraction

def tampilkan_pangkat(pangkat_str):
    """Tampilkan 3^3 sebagai 3 x 3 x 3"""
    base, exp = map(int, pangkat_str.split("^"))
    bentuk = " x ".join([str(base)] * exp)
    hasil = base ** exp
    return bentuk, hasil

def tampilkan_langkah(expr_input):
    langkah = []
    expr = expr_input.replace(",", ".").replace("x", "*").replace(":", "/")
    expr_eval = expr

    # Persen ke pecahan
    persen_match = re.findall(r'(\d+(?:\.\d+)?|\d+,\d+)%', expr_input)
    for match in persen_match:
        persen = match.replace(",", ".")
        bentuk = f"{persen}/100"
        expr_eval = expr_eval.replace(f"{match}%", f"({bentuk})")
        langkah.append(f"Ubah {match}% menjadi bentuk pecahan: {bentuk}")

    # Pangkat seperti 3^3
    pangkat_match = re.findall(r'(\d+)\^(\d+)', expr_input)
    for base, exp in pangkat_match:
        bentuk, hasil = tampilkan_pangkat(f"{base}^{exp}")
        langkah.append(f"Ubah {base}^{exp} menjadi: {bentuk} = {hasil}")
        expr_eval = expr_eval.replace(f"{base}^{exp}", str(hasil))

    # Pecahan ke desimal
    pecahan_match = re.findall(r'(\d+/\d+)', expr_eval)
    for p in pecahan_match:
        val = float(Fraction(p))
        langkah.append(f"Ubah pecahan {p} menjadi desimal: {val}")
        expr_eval = expr_eval.replace(p, str(val))

    return expr_eval, langkah

def evaluate_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return f"Terjadi kesalahan saat evaluasi: {e}"

def kalkulator():
    print("\n=== KALKULATOR PROTOTYPE ===")
    print("Pilih jenis operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (x)")
    print("4. Pembagian (:)")
    pilihan = input("Masukkan nomor operasi (1-4): ")

    if pilihan not in {"1", "2", "3", "4"}:
        print("Pilihan tidak valid.")
        return

    print("\nMasukkan ekspresi yang ingin dihitung.")
    print("Gunakan simbol berikut:")
    print(" - Pangkat: ^ (misal: 2^3)")
    print(" - Desimal: , (misal: 3,5)")
    print(" - Persen: % (misal: 50%)")
    print(" - Pecahan: / (misal: 1/2)\n")

    expr_input = input("Masukkan ekspresi: ")

    expr_eval, langkah = tampilkan_langkah(expr_input)
    hasil = evaluate_expression(expr_eval)

    print("\n=== TAHAP PENYELESAIAN ===")
    print(f"Ekspresi awal: {expr_input}")
    for i, l in enumerate(langkah, start=1):
        print(f"{i}. {l}")
    print(f"{len(langkah)+1}. Menjadi: {expr_eval}")
    print(f"{len(langkah)+2}. Hasil akhir: {hasil}\n")

def main():
    while True:
        kalkulator()
        lanjut = input("Apakah Anda ingin menghitung soal lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("\nTerima kasih telah menggunakan kalkulator prototype kami.")
            break

if __name__ == "__main__":
    main()
