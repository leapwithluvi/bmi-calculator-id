# Program Penghitungan BMI

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("---------------------------------------------")

berat_badan = input("Masukkan berat badan anda (kg) : ")
berat_badan = int(berat_badan)
tinggi_badan = input("Masukkan tinggi badan (meter) : ")
tinggi_badan = float(tinggi_badan)

print("---------------------------------------------")

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal["bawah"] = 18.5*(tinggi_badan**2)
berat_badan_ideal["atas"] = 25*(tinggi_badan**2)

print(f"Nilai BMI anda adalah : {bmi:.2f} kg/m^2")
print("Nilai normal BMI adalah : 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat badan ideal anda adalah dalam rentang "
      f"{berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")

print("---------------------------------------------")
print("Terima Kasih telah menggunakan program ini :>")