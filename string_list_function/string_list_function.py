# Contoh penggunaan string, list, dan function dalam Python

# String
nama = "Alice"
umur_str = "25"

# Menggunakan string methods
print("Panjang nama:", len(nama))
print("Huruf pertama:", nama[0])

# List
buah = ["apel", "pisang", "jeruk"]

# Menambahkan item ke dalam list
buah.append("mangga")

# Mengakses item dalam list
print("Buah:", buah)

# Function
def hitung_kuadrat(x):
    """Fungsi untuk menghitung kuadrat dari suatu bilangan."""
    return x ** 2

# Memanggil function
angka = 5
hasil_kuadrat = hitung_kuadrat(angka)
print("Hasil kuadrat dari", angka, "adalah", hasil_kuadrat)
