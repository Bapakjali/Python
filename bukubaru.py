def show_genres(data):
    """Menampilkan semua genre yang tersedia"""
    all_genres = set()
    for genres in data.values():
        all_genres.update(genres)
    return sorted(all_genres)

def filter_books_by_genre(selected_genres, data):
    """Mengembalikan buku-buku yang memiliki minimal salah satu genre yang dipilih"""
    return {
        book: genres for book, genres in data.items() 
        if selected_genres & genres
    }

def recommend_books(data_filtered):
    """Menampilkan buku-buku yang telah difilter"""
    print("\nBuku-buku yang tersedia:")
    for i, book in enumerate(data_filtered.keys(), 1):
        print(f"{i}. {book}")
    
    while True:
        choice = input("\nPilih nomor buku untuk mendapatkan rekomendasi (atau 'exit' untuk keluar): ")
        
        if choice.lower() == 'exit':
            return
        
        try:
            book_index = int(choice) - 1
            selected_book = list(data_filtered.keys())[book_index]
            genres = data_filtered[selected_book]
            
            print(f"\nMenghasilkan rekomendasi untuk: {selected_book}")
            print(f"Genre buku ini: {', '.join(genres)}")
            
            similar_books = {}
            for book, g in data_filtered.items():
                if book != selected_book:
                    similarity = len(genres & g)
                    if similarity > 0:
                        similar_books[book] = similarity
            
            if not similar_books:
                print("Tidak ditemukan buku dengan genre yang mirip.")
                continue
                
            # Mengurutkan berdasarkan similarity tertinggi
            sorted_books = sorted(similar_books.items(), key=lambda x: x[1], reverse=True)
            
            print("\n3 Rekomendasi buku teratas:")
            for i, (book, score) in enumerate(sorted_books[:3], 1):
                print(f"{i}. {book} (Kesamaan genre: {score})")
                
        except (ValueError, IndexError):
            print("Input tidak valid. Masukkan nomor yang sesuai atau 'exit'.")

def main():
    # Data buku
    data_buku = {
        "AI for Beginners": {"AI", "ML", "Beginner"},
        "Deep Learning with Python": {"AI", "Deep Learning"},
        "Data Science Essentials": {"Data", "ML"},
        "AI and Ethics": {"AI", "Philosophy"},
        "Machine Learning Fundamentals": {"ML", "Beginner"},
        "Python Programming": {"Programming", "Beginner"},
    }
    
    print("=== Sistem Rekomendasi Buku ===")
    
    # Menampilkan semua genre yang tersedia
    available_genres = show_genres(data_buku)
    print("\nGenre yang tersedia:")
    for i, genre in enumerate(available_genres, 1):
        print(f"{i}. {genre}")
    
    # Memilih genre
    selected_genres = set()
    while True:
        choice = input("\nPilih nomor genre yang Anda minati (pisahkan dengan koma jika multiple, atau 'selesai'): ")
        
        if choice.lower() == 'selesai':
            break
            
        try:
            choices = [int(c.strip()) for c in choice.split(",")]
            for c in choices:
                if 1 <= c <= len(available_genres):
                    selected_genres.add(available_genres[c-1])
                else:
                    print(f"Nomor {c} tidak valid.")
            
            print("\nGenre terpilih:", ", ".join(selected_genres) if selected_genres else "Belum ada")
        except ValueError:
            print("Masukkan angka yang valid.")
    
    if not selected_genres:
        print("Anda belum memilih genre apapun. Sistem akan menampilkan semua buku.")
        data_filtered = data_buku
    else:
        print(f"\nMemfilter buku berdasarkan genre: {', '.join(selected_genres)}")
        data_filtered = filter_books_by_genre(selected_genres, data_buku)
    
    recommend_books(data_filtered)

if __name__ == "__main__":
    main()
