from data import inventaris, penjualan

def hitung_nilai_inventaris_total():
    """Menghitung total nilai dari semua barang di inventaris HashMap."""
    total = sum(value["stok"] * value["harga"] for _, value in inventaris.get_all_items())
    print(f"Total nilai inventaris: Rp{total}")

def tambah_penjualan(nama_produk, jumlah, harga_satuan):
    """Menambahkan transaksi penjualan ke dalam Queue."""
    penjualan.enqueue({"produk": nama_produk, "jumlah": jumlah, "harga": harga_satuan})

def hitung_total_harga():
    """Menghitung total harga dari semua transaksi di Queue."""
    total = sum(p["jumlah"] * p["harga"] for p in penjualan.get_all_items())
    print(f"Total harga: Rp{total}")
    return total

def hitung_diskon(total):
    """Menghitung diskon berdasarkan total belanja."""
    diskon = 0
    if total >= 50000:
        diskon = 0.1 * total
    print(f"Diskon: Rp{diskon}")
    return diskon

def laporan_penjualan():
    """Menampilkan laporan rinci dari semua transaksi di Queue."""
    print("\n=== Laporan Penjualan ===")
    if penjualan.is_empty():
        print("Tidak ada transaksi penjualan.")
        return
        
    for p in penjualan.get_all_items():
        print(f"- {p['produk']} x{p['jumlah']} Rp{p['harga']}")