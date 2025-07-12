def validate_password(password):
    # Kriteria Validasi password
    min_length = 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    forbidden_chars = {'.', '"', '(', ')', "'",}

    # Cek panjang password
    if len(password) < min_length:
        return False, "Password harus minimal 8 karakter"
    
    # Cek karakter dalam password
    for char in password:
        if char in forbidden_chars:
            return False, "Password tidak boleh mengandung karakter khusus seperti . \" ( ) '"
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in {'!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+'}:
            has_special = True
    
    # Cek apakah semua kriteria terpenuhi
    messages = []
    if not has_upper:
        messages.append("Password harus mengandung huruf kapital")
    if not has_lower:
        messages.append("Password harus mengandung huruf kecil")
    if not has_digit:
        messages.append("Password harus mengandung angka")
    
    if messages:
        return False, "\n".join(messages)
    else:
        return True, "Password valid"

# Program utama
if __name__ == "__main__":
    print("Masukkan password untuk validasi:")
    print("Kriteria: minimal 8 karakter, mengandung huruf kapital, huruf kecil, angka, dan tidak boleh mengandung karakter khusus seperti . \" ( ) '")

    while True:
        password = input("\nMasukkan password: ")

        if password.lower() == "exit":
            print("Program dihentikan.")
            break

        is_valid, message = validate_password(password)

        if is_valid:
            print("Password valid:", message)
            break
        else:
            print("Password tidak valid:", message)
            print("Silakan coba lagi.")
