import csv
import os

# --- Implementasi Struktur Data HashMap ---
class HashMap:
    def __init__(self, size=10): #Slot untuk memudahkan organisir data
        self.size = size
        self.buckets = [[] for _ in range(size)]

# Fungsi internal untuk menghitung "alamat" atau indeks di mana data akan disimpan
    def _get_hash(self, key):
        return hash(key) % self.size #operator modulus agar rentang index valid

# Fungsi untuk memasukkan atau memperbarui data
    def put(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # Meriksa apakah bucket di indeks tersebut masih kosong
        if not self.buckets[key_hash]:
            self.buckets[key_hash].append(key_value)
            return True
        else:
            for pair in self.buckets[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.buckets[key_hash].append(key_value)
            return True
        
# Fungsi untuk mengambil value berdasarkan key
    def get(self, key):
        key_hash = self._get_hash(key)
        # Menggunakan nama variabel baru: self.buckets
        if self.buckets[key_hash]:
            for pair in self.buckets[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
# Fungsi untuk menghapus item berdasarkan key
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.buckets[key_hash]:
            for i, pair in enumerate(self.buckets[key_hash]):
                if pair[0] == key:
                    self.buckets[key_hash].pop(i)
                    return True # Berhasil dihapus
        return False # Gagal (key tidak ditemukan)
    
# Fungsi untuk mengambil semua data di hashmap
    def get_all_items(self):
        all_items = []
        # Menggunakan nama variabel baru: self.buckets
        for bucket in self.buckets:
            for pair in bucket:
                all_items.append(pair)
        return all_items

# --- Implementasi Struktur Data Queue ---
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items
# --- Inisiasi Struktur Data Global ---
inventaris = HashMap()
penjualan = Queue()

# --- Fungsi untuk Interaksi dengan Database CSV ---

def muat_database():
    """Memuat data dari file CSV ke dalam struktur data di memori."""
    if os.path.exists('inventaris.csv'):
        with open('inventaris.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventaris.put(
                    row['nama_produk'],
                    {'stok': int(row['stok']), 'harga': int(row['harga'])}
                )
    
    if os.path.exists('penjualan.csv'):
        with open('penjualan.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                penjualan.enqueue(
                    {'produk': row['produk'], 'jumlah': int(row['jumlah']), 'harga': int(row['harga'])}
                )
    print("Database berhasil dimuat.")

def simpan_database():
    """Menyimpan data dari memori ke file CSV."""
    with open('inventaris.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nama_produk', 'stok', 'harga'])
        for key, value in inventaris.get_all_items():
            writer.writerow([key, value['stok'], value['harga']])

    with open('penjualan.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['produk', 'jumlah', 'harga'])
        for item in penjualan.get_all_items():
            writer.writerow([item['produk'], item['jumlah'], item['harga']])
    
    print("Perubahan berhasil disimpan ke database.")