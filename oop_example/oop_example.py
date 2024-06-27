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
