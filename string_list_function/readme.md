# String, List, dan Function dalam Python

Di dalam folder ini, Anda akan menemukan contoh penggunaan string, list, dan function dalam bahasa pemrograman Python.

## String
String adalah tipe data yang digunakan untuk menyimpan teks. Dalam contoh ini, kami menggunakan beberapa operasi dasar pada string.

### Contoh Kode

# Contoh penggunaan string dalam Python

## String
nama = "Alice"
umur_str = "25"

# Menggunakan string methods
print("Panjang nama:", len(nama))
print("Huruf pertama:", nama[0])

## List
List adalah struktur data yang digunakan untuk menyimpan kumpulan elemen. Kami juga menunjukkan cara menambahkan item ke dalam list dan mengakses item dalam list.

Contoh Kode
# Contoh penggunaan list dalam Python

# List
buah = ["apel", "pisang", "jeruk"]

# Menambahkan item ke dalam list
buah.append("mangga")

# Mengakses item dalam list
print("Buah:", buah)

## Function
Function adalah blok kode yang dapat dipanggil untuk melakukan tugas tertentu. Fungsi hitung_kuadrat contohnya menghitung kuadrat dari suatu bilangan.

# Contoh penggunaan function dalam Python

# Function
def hitung_kuadrat(x):
    """Fungsi untuk menghitung kuadrat dari suatu bilangan."""
    return x ** 2

# Memanggil function
angka = 5
hasil_kuadrat = hitung_kuadrat(angka)
print("Hasil kuadrat dari", angka, "adalah", hasil_kuadrat)

Cara Menjalankan Kode
Untuk menjalankan file string_list_function.py, buka terminal atau command prompt, lalu ketik:
`python string_list_function.py`