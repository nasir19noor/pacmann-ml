class Belanja:
    roti = 3
    soda = 5
    selai = 2
    def jumlah_belanja(self):
        print("Jumlah Belanja")
        print(f"Roti = {self.roti}")
        print(f"Soda = {self.soda}")
        print(f"Selai = {self.selai}")

item_1 = Belanja()
item_1.jumlah_belanja()


Belanja().jumlah_belanja()
print(Belanja.roti)