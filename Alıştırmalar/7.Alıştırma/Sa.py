population = 9
land_area = 1

# a. Nüfus 10.000.000'dan azsa nüfusu yazdır
if population < 10000000:
    print("Nüfus:", population)

# b. Nüfus 10.000.000 ile 35.000.000 arasında ise nüfusu yazdır
if 10000000 <= population <= 35000000:
    print("Nüfus:", population)

# c. Arazi yoğunluğu 100'den büyükse "Yoğun nüfuslu" yazdır
population_density = population / land_area  # Arazi yoğunluğunu hesapla
if population_density > 100:
    print("Yoğun nüfuslu")

# d. Arazi yoğunluğu 100'den büyükse “Yoğun nüfuslu”, aksi takdirde “Seyrek nüfuslu” yazdır
if population_density > 100:
    print("Yoğun nüfuslu")
else:
    print("Seyrek nüfuslu")