# Sets, Tuples, dan Dictionary dalam Python

Di dalam folder ini, Anda akan menemukan contoh penggunaan sets, tuples, dan dictionary dalam bahasa pemrograman Python.

## Sets

Sets adalah struktur data yang digunakan untuk menyimpan kumpulan elemen unik tanpa urutan tertentu. Contoh di bawah ini menunjukkan penggunaan sets untuk menyimpan nama-nama buah.

### Contoh Kode

# Contoh penggunaan sets dalam Python

# Sets
buah_set = {"apel", "pisang", "jeruk", "apel"}  # Duplikat akan dihapus
print("Set buah:", buah_set)


## Tuples
Tuples adalah struktur data yang mirip dengan list, tetapi elemennya tidak dapat diubah setelah dibuat. Contoh di bawah ini menunjukkan penggunaan tuples untuk menyimpan angka-angka.

# Contoh penggunaan tuples dalam Python

# Tuples
tuple_angka = (1, 2, 3, 4, 5)
print("Tuple angka:", tuple_angka)

## Dictionary
Dictionary adalah struktur data yang digunakan untuk menyimpan pasangan key-value. Contoh di bawah ini menunjukkan penggunaan dictionary untuk menyimpan informasi siswa.

# Contoh penggunaan dictionary dalam Python

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

Cara Menjalankan Kode
Untuk menjalankan file sets_tuples_dict.py, buka terminal atau command prompt, lalu ketik:
`python sets_tuples_dict.py`