# Contoh penggunaan sets, tuples, dan dictionary dalam Python

# Sets
buah_set = {"apel", "pisang", "jeruk", "apel"}  # Duplikat akan dihapus
print("Set buah:", buah_set)

# Tuples
tuple_angka = (1, 2, 3, 4, 5)
print("Tuple angka:", tuple_angka)

# Dictionary
siswa = {
    "nama": "John Doe",
    "umur": 25,
    "kelas": "12A",
    "nilai": {"matematika": 85, "bahasa_inggris": 78, "sains": 90}
}

# Mengakses nilai dalam dictionary
print("Nama siswa:", siswa["nama"])
print("Umur siswa:", siswa["umur"])
print("Nilai matematika:", siswa["nilai"]["matematika"])
