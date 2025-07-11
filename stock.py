# Mengimpor instance HashMap dari file data
from data import inventaris
from data import penjualan

def tambah_produk(nama_produk, stok, harga_satuan):
    """Menambahkan produk baru ke dalam inventaris HashMap."""
    inventaris.put(nama_produk, {"stok": stok, "harga": harga_satuan})
    print(f"{nama_produk} ditambahkan dengan stok {stok} dan harga Rp{harga_satuan}.")

def hapus_produk(nama_produk):
    """Menghapus produk dari inventaris HashMap."""
    if inventaris.delete(nama_produk):
        print(f"Produk '{nama_produk}' berhasil dihapus.")
    else:
        print(f"Gagal: Produk '{nama_produk}' tidak ditemukan.")
        
def kurangi_stok(nama_produk, jumlah):
    """
    Mengurangi stok produk dalam inventaris HashMap.
    Fungsi ini sekarang digunakan secara internal untuk memproses penjualan.
    """
    produk_data = inventaris.get(nama_produk)
    
    if produk_data: # Cek apakah produk ditemukan
        if produk_data["stok"] >= jumlah:
            # Kurangi stok dan perbarui data di HashMap
            produk_data["stok"] -= jumlah
            inventaris.put(nama_produk, produk_data)
            return True # Berhasil
        else:
            print(f"Peringatan: Stok {nama_produk} tidak cukup untuk penjualan.")
            return False # Gagal
    else:
        print(f"Peringatan: Produk {nama_produk} tidak ditemukan di inventaris untuk penjualan.")
        return False # Gagal

def cek_stok_minimum(batas=5):
    """Memeriksa produk dengan stok di bawah batas minimum dari HashMap."""
    print("\nProduk dengan stok di bawah batas minimum:")
    ada_stok_minimum = False
    # Iterasi melalui semua item di HashMap
    for key, value in inventaris.get_all_items():
        if value["stok"] < batas:
            print(f"- {key}: {value['stok']} unit")
            ada_stok_minimum = True
    if not ada_stok_minimum:
        print("Semua stok produk aman.")

