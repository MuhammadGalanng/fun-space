def luas_segitiga():
  """Menghitung luas segitiga."""
  alas = int(input("Masukkan alas segitiga: "))
  tinggi = int(input("Masukkan tinggi segitiga: "))
  luas = alas * tinggi / 2
  print(f"Luas segitiga adalah: {luas}")

def luas_persegi_panjang():
  """Menghitung luas persegi panjang."""
  panjang = int(input("Masukkan panjang persegi panjang: "))
  lebar = int(input("Masukkan lebar persegi panjang: "))
  luas = panjang * lebar
  print(f"Luas persegi panjang adalah: {luas}")

# Menjalankan fungsi
luas_segitiga()
luas_persegi_panjang()
