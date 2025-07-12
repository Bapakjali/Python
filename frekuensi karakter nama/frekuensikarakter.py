def hitung_frekuensi(nama):
    # Inisialisasi dictionary untuk menyimpan frekuensi
    frekuensi = {}
    
    # Hitung frekuensi setiap karakter (case sensitive)
    for char in nama:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    
    return frekuensi

def tampilkan_hasil(frekuensi):
    print("\nHasil Perhitungan Frekuensi Karakter:")
    print("-----------------------------------")
    print("Karakter | Jumlah Kemunculan")
    print("-----------+-----------------")
    
    # Urutkan berdasarkan karakter
    for char in sorted(frekuensi.keys()):
        # Abaikan spasi saat menampilkan
        if char == ' ':
            print(f"(spasi)   | {frekuensi[char]}")
        else:
            print(f"{char:9} | {frekuensi[char]}")
    
    # Cari karakter yang paling sering muncul
    max_freq = max(frekuensi.values())
    most_common = [k for k, v in frekuensi.items() if v == max_freq]
    
    print("\nKarakter yang paling sering muncul:")
    for char in most_common:
        char_display = "(spasi)" if char == ' ' else char
        print(f"'{char_display}' muncul {max_freq} kali")

def main():
    nama = "Rahardian Ananda Putra"
    print(f"Menghitung frekuensi karakter untuk nama: \"{nama}\"")
    
    # Hitung frekuensi karakter
    frekuensi = hitung_frekuensi(nama)
    
    # Tampilkan hasil
    tampilkan_hasil(frekuensi)

if __name__ == "__main__":
    main()
