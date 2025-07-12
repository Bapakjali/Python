def check_profanity(text):
    # Daftar kata-kata kasar
    profane_words = {"bodoh", "tolol", "goblok", "jancok", "babi", "anjing", "kontol", "memek", "sialan", "kampret", "bangsat", "asu", "brengsek", "ngentot", "perek", "pelacur", "pelacuran", "sundal", "pelacur", "monyet", "goblok", "bego", "kampungan", "kampung", "tolol", "bodoh", "brengsek", "sialan", "ngentot", "kontol", "memek", "jancok", "babi", "anjing", "asu", "perek", "pelacur", "sundal", "monyet"}
    
    # Mengubah teks menjadi huruf kecil dan memisahkan kata-kata
    words = text.lower().split()
    
    # Memeriksa apakah ada kata kasar dalam teks
    for word in words:
        if word in profane_words:
            return True, word  # Mengembalikan True dan kata kasar yang ditemukan
    
    return False, None  # Tidak ada kata kasar ditemukan

# Program utama
if __name__ == "__main__":
    print("Masukkan kalimat untuk memeriksa kata-kata kasar:")
    
    while True:
        user_input = input("\nMasukkan kalimat (atau ketik 'exit' untuk keluar): ")
        
        if user_input.lower() == "exit":
            print("Program dihentikan.")
            break
        
        has_profanity, found_word = check_profanity(user_input)
        
        if has_profanity:
            print(f"Kata kasar ditemukan: '{found_word}'")
        else:
            print("Tidak ada kata kasar ditemukan.")
