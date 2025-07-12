def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def main():
    print("=== KONVERTER BILANGAN ROMAWI ===")
    print("Konversi bilangan bulat (1-3999) ke angka Romawi")
    print("Ketik 'keluar' untuk menghentikan program\n")
    
    while True:
        user_input = input("Masukkan bilangan: ")
        
        if user_input.lower() == 'keluar':
            print("Program dihentikan. Sampai jumpa!")
            break
            
        try:
            num = int(user_input)
            if num < 1 or num > 3999:
                print("Harap masukkan bilangan antara 1 sampai 3999\n")
                continue
                
            roman = int_to_roman(num)
            print(f"Hasil konversi: {num} = {roman}\n")
            
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat atau 'keluar'\n")

if __name__ == "__main__":
    main()
