# Mengimpor fungsi-fungsi yang dibutuhkan dari modul lain
from data import muat_database, simpan_database, penjualan
from stock import tambah_produk, cek_stok_minimum, kurangi_stok, hapus_produk
from hitung import (
    hitung_nilai_inventaris_total,
    tambah_penjualan,
    hitung_total_harga,
    hitung_diskon,
    laporan_penjualan
)
def proses_penjualan_dan_update_stok():
    """
    Fungsi baru untuk memproses setiap item di antrean penjualan
    dan mengurangi stok di inventaris.
    """
    print("\nMemproses penjualan dan memperbarui stok...")
    # Kita menggunakan get_all_items() untuk melihat semua transaksi
    for trx in penjualan.get_all_items():
        kurangi_stok(trx['produk'], trx['jumlah'])

muat_database()
 # === FASE 1: MANAJEMEN INVENTARIS ===
print("\n=== KELOLA INVENTARIS ===")
jumlah_produk = int(input("Berapa produk yang ingin ditambahkan? (0 jika tidak ada) "))
for i in range(jumlah_produk):
    nama = input("Nama produk: ")
    stok = int(input("Stok awal: "))
    harga = int(input("Harga satuan: "))
    tambah_produk(nama, stok, harga)

# --- Blok Penghapusan Produk ---
hapus = input("\nApakah ada produk yang ingin dihapus? (y/n): ").lower()
if hapus == 'y':
    nama_hapus = input("Nama produk yang ingin dihapus: ")
    hapus_produk(nama_hapus)

# Langsung cek stok dan nilai inventaris setelah penambahan
cek_stok_minimum()
hitung_nilai_inventaris_total()

# === FASE 2: SIMULASI PENJUALAN ===
print("\n=== CATAT PENJUALAN ===")
jumlah_jual = int(input("Berapa transaksi penjualan yang ingin dicatat? (0 jika tidak ada) "))
for i in range(jumlah_jual):
    nama = input("Nama produk terjual: ")
    jumlah = int(input("Jumlah: "))
    harga = int(input("Harga satuan: "))
    tambah_penjualan(nama, jumlah, harga)

# Hanya hitung jika ada penjualan
if jumlah_jual > 0:
    total = hitung_total_harga()
    hitung_diskon(total)
        
laporan_penjualan()
proses_penjualan_dan_update_stok()
# Simpan semua perubahan ke file CSV sebelum aplikasi ditutup
simpan_database()


