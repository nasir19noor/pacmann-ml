class Pekerja:
    domain = "nasir.id"
    def __init__(self, nama_depan, nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nama_lengkap = nama_depan + ' ' + nama_belakang
        self.email = nama_depan.lower() + '.' + nama_belakang.lower() + '@'+ self.domain   

people_1 = Pekerja("Nasir", "Noor")
print(people_1.nama_lengkap)
print(people_1.email)
    