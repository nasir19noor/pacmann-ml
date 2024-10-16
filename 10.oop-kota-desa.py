class Pelanggan:
    def __init__(self, kota, desa):
        self.kota = kota
        self.desa = desa
        self.kota_desa = f"{kota}, {desa}"

people_3 = Pelanggan("Jember", "Andongsari")
print(people_3.kota_desa)        
    