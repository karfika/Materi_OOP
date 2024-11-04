# Class Parent

class Hewan :
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "Hewan ini memiliki suara."
    
# Class Child
class Kucing(Hewan):
    def __init__(self, nama, warna_bulu):
        super().__init__(nama)   # Memanggil konstruktor dari Class Parent
        self.warna_bulu = warna_bulu

    def suara(self):
        return "Meoww"  # Override metode suara dari Class Parent
    
# Class Child
class Anjing(Hewan):
    def __init__(self, nama, umur):
        super().__init__(nama)
        self.umur = umur

    def suara(self):
        return "Guk guk"  # Override metode suara dari Class Parent
    

# Objek 
kucing1 = Kucing("Kitty", "Putih")

anjing1 = Anjing("Buddy", 4)

# Menampilkan informasi kucing
print(f"{kucing1.nama} berwarna {kucing1.warna_bulu} dan suaranya '{kucing1.suara()}'.")

# Menampilkan informasi anjing
print(f"{anjing1.nama} berumur {anjing1.umur} tahun dan suaranya '{anjing1.suara()}'.")



