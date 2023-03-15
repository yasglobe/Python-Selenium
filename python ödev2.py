ogrenciListesi = ["Yusuf UĞUR", "Ahmet TAN", "Işık UFUK"]  # Liste görünümü
print(ogrenciListesi)
print("")
print("")
print("")

print("****************")


# Öğrenci ekleme:

ogrenciEkle = input("Lütfen eklemek istediğiniz İsim ve Soyisimi giriniz:")

ogrenciListesi.append(ogrenciEkle)
print(ogrenciListesi)
print("")
print("")
print("")

print("**************")

# Listeden öğrenci silme

ogrencisil = input("Lütfen silmek istediğiniz İsim ve Soyisimi giriniz:")
ogrenciListesi.remove(ogrencisil)
print(ogrenciListesi)
print("")
print("")
print("")
print("*************")

# Listeye birden fazla isim ekleme

cokluEkleme = []

kisisayisi = int(input("Kaç İsim eklemek istiyorsunuz?"))
for i in range(kisisayisi):
    a = input("Eklenecek kişileri sıra ile giriniz.")
    cokluEkleme.append(a)

ogrenciListesi.extend(cokluEkleme)
print(ogrenciListesi)
print(type(ogrenciListesi))
print("")
print("")
print("")

print("***********************")

# Öğrenci Listesini sıralar


n = 0
while n < len(ogrenciListesi):
    print(n+1,". isim:",ogrenciListesi[n])
    n += 1
print("")
print("")
print("")
print("********************")

# Öğrenci numarasını bulma

bul = input("Öğrenmek istdiğiniz öğrencinin adını giriniz:")
for j in range(len(ogrenciListesi)):
    if bul == ogrenciListesi[j]:
        print(bul,"İsimli öğrencinin numarası",j)
    
print("")
print("")
print("")
print("*************")

# Silinecek öğrenciler

kisisayisi = int(input("Kaç isim silmek istiyorsunuz?"))

for i in range(kisisayisi):
    isim = input("Silmek istediğiniz isim?")
    for n in ogrenciListesi:
        if n == isim:
            ogrenciListesi.remove(isim)

print(ogrenciListesi)
print("")
print("")


n = 0
while n < len(ogrenciListesi):
    print(n+1,". isim:",ogrenciListesi[n])
    n += 1
print("")
print("")
print("")

print("Liste başarı ile tamamlanmıştır.")





