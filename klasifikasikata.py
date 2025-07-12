def deteksi_emosi(kalimat):
    # Daftar kata kunci untuk setiap emosi
    emosi = {
        "Positive": ["senang", "gembira", "bahagia", "ceria", "senyum", "tertawa", "terhibur", "tertarik", "terpesona", "terinspirasi", "terpukau", "terharu", "terbawa suasana", "menyenangkan", "menghibur", "menggembirakan", "membahagiakan", "menarik", "tertarik", "terpesona", "terinspirasi", "terpukau", "terharu", "terbawa suasana"],
        "Angry": ["marah", "kesal", "jengkel", "geram", "kesal", "menyebalkan"," menyakitkan", "sial", "sialan", "sialnya", "anjing", "babi", "bodoh", "tolol", "brengsek", "kampret", "kontol", "memek", "perek", "pelacur", "pelacuran", "pelacurannya", "pelacurmu", "pelacurku", "pelacuranmu", "pelacurku", "pelacuran", "pelacuran itu", "pelacuran yang", "pelacuran di", "pelacuran dengan", "lacur"],
        "Sad": ["sedih", "kecewa", "menangis", "merasa hampa", "kehilangan", "putus asa", "menyedihkan", "menderita", "terpuruk", "terluka", "tersakiti", "terluka hati", "terluka jiwa", "terluka batin", "terluka perasaan"],
        "Fear": ["takut", "cemas", "khawatir", "gelisah", "cemas", "was-was", "bingung", "terkejut", "tercengang", "terheran-heran", "terpana", "terpukau", "terpesona", "tertarik", "tertarik dengan", "tertarik pada"],
        "Disgust": ["menjijikkan", "menjijikkan", "menjijikkan sekali", "menjijikkan banget", "menjijikkan sekali", "ewh", "yuck", "menjijikkan", "menjijikkan sekali", "menjijikkan banget"]
    }
    
    # Mengubah kalimat menjadi huruf kecil dan memisahkan kata-kata
    kata_kata = kalimat.lower().split()
    
    # Mendeteksi emosi berdasarkan kata kunci
    for emosi_kategori, kata_kunci in emosi.items():
        if any(kata in kata_kata for kata in kata_kunci):
            return emosi_kategori
    
    return "Neutral"  # Jika tidak ada kata kunci yang cocok

def main():
    print("=== DETEKSI EMOSI KALIMAT ===")
    print("Masukkan kalimat untuk mendeteksi emosi (ketik 'keluar' untuk berhenti)\n")
    
    while True:
        kalimat = input("Masukkan kalimat: ")
        
        if kalimat.lower() == 'keluar':
            print("Program dihentikan. Terima kasih!")
            break
        
        emosi = deteksi_emosi(kalimat)
        print(f"Emosi yang terdeteksi: {emosi}\n")

if __name__ == "__main__":
    main()
