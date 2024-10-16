class Segitiga:
    def __init__(self,alas,tinggi,tipe):
        self.alas = alas
        self.tinggi = tinggi
        self.tipe = tipe

triangle_1 = Segitiga(10, 20, 'Siku-Siku')
triangle_2 = Segitiga(5, 8, 'Sama Kaki')   

print(triangle_1.alas)

class SegitigaSikuSiku:
    tipe = "Siku-Siku"
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi

triangle_3 = SegitigaSikuSiku(alas = 7, tinggi = 9)
print(triangle_3.tipe)