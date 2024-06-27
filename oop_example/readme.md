# Pemrograman Berorientasi Objek (OOP) dalam Python

Di dalam folder ini, Anda akan menemukan contoh penggunaan Pemrograman Berorientasi Objek (OOP) dalam bahasa pemrograman Python.

## Konsep Dasar OOP

OOP adalah paradigma pemrograman yang menggunakan objek-objek dan hubungan antar objek untuk mendesain dan mengimplementasikan aplikasi. Di Python, objek adalah instance dari class.

### Contoh Kode

# Contoh penggunaan Pemrograman Berorientasi Objek (OOP) dalam Python

# Definisi sebuah class
class Kendaraan:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    
    def info(self):
        return f"Kendaraan ini adalah {self.merk} berwarna {self.warna}"

# Membuat objek dari class Kendaraan
mobil = Kendaraan("Toyota", "Hitam")
motor = Kendaraan("Honda", "Merah")

# Memanggil method info() dari objek
print(mobil.info())
print(motor.info())

Cara Menjalankan Kode
Untuk menjalankan file oop_example.py, buka terminal atau command prompt, lalu ketik:
`python oop_example.py`