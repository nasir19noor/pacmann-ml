class Binatang():
    def __init__(self,nama):
        self.nama = nama

class Kucing(Binatang):
    pass

cat_1 = Kucing("Miki")

print(f"Nama : {cat_1.nama}")


class Kucing(Binatang):
    def __init__(self,nama, umur):
        Binatang.__init__(self, nama)
        self.umur = umur

hewan1 = Kucing("Miko", 5)
print(hewan1.umur)        
