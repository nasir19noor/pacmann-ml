class Mobil:
    def __init__(self, kecepatan, jarak):
        self.kecepatan = kecepatan
        self.jarak = jarak
car_1 = Mobil(40, 120)
car_2 = Mobil(60, 200)

print(f"jarak = {car_1.jarak}")

for idx, car in enumerate([car_1, car_2]):
    num_car = idx+1

    print(f"Object Car {num_car}")
    print(f"Kecepatan Car {num_car}: {car.kecepatan}")
    print(f"Jarak Car {num_car}: {car.jarak}")

