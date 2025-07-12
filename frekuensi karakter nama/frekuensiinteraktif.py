from typing import Dict

def hitung_frekuensi(nama: str) -> Dict[str, int]:
    """
    Hitung frekuensi kemunculan setiap karakter dalam string.

    Args:
        nama (str): Teks input yang akan dihitung frekuensi karakternya.

    Returns:
        Dict[str, int]: Kamus yang berisi karakter sebagai kunci dan jumlah kemunculan sebagai nilai.
    """
    frekuensi = {}
    for char in nama:
        frekuensi[char] = frekuensi.get(char, 0) + 1
    return frekuensi

def main() -> None:
    """
    Program utama untuk menghitung dan menampilkan frekuensi karakter dari input pengguna.
    Program akan terus meminta input hingga pengguna mengetik 'selesai'.
    """
    print("\n=== PROGRAM FREKUENSI KARAKTER ===")
    print("Hitung jumlah kemunculan setiap karakter dalam teks\n")
    
    while True:
        nama = input("Masukkan teks (atau ketik 'selesai' untuk keluar): ").strip()
        
        if not nama:
            print("Input tidak boleh kosong. Silakan coba lagi.")
            continue
        
        if nama.lower() == 'selesai':
            print("\nTerima kasih telah menggunakan program ini!")
            break
            
        print("\n🔄 Menghitung frekuensi karakter...")
        
        frekuensi = hitung_frekuensi(nama)
        
        print("\nBerikut hasilnya:")
        print("-----------------------------")
        print(" Karakter | Jumlah Kemunculan")
        print("----------+------------------")
        
        # Urutkan berdasarkan jumlah kemunculan (descending)
        for char, count in sorted(frekuensi.items(), key=lambda x: x[1], reverse=True):
            char_display = "(spasi)" if char == " " else char
            print(f"  {char_display:<7} | {count}")
            
        # Tampilkan karakter yang paling sering muncul
        max_count = max(frekuensi.values())
        most_chars = [k for k, v in frekuensi.items() if v == max_count]
        
        print("\n🔥 Karakter paling sering muncul:")
        for char in most_chars:
            char_display = "(spasi)" if char == " " else char
            print(f"  '{char_display}' muncul {max_count} kali")
        
        print("\n" + "=" * 30 + "\n")

if __name__ == "__main__":
    main()
