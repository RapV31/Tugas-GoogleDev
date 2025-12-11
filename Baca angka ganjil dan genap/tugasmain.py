# 1. Membuka file data.txt dengan mode 'r' (read/baca)
try:
    with open('data.txt', 'r') as file:
        
        print("--- Hasil Pengecekan Angka ---")
        
        # 2. Membaca setiap baris di dalam file
        for baris in file:
            # Membersihkan spasi/enter (strip) dan mengubah string menjadi integer
            angka = int(baris.strip())
            
            # 3. Logika Ganjil atau Genap
            if angka % 2 == 0:
                print(f"Angka {angka} adalah GENAP")
            else:
                print(f"Angka {angka} adalah GANJIL")

except FileNotFoundError:
    print("Error: File 'data.txt' tidak ditemukan. Pastikan file ada di folder yang sama.")
except ValueError:
    print("Error: Ada baris di file yang bukan angka.")