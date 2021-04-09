alinanNot1 = int(input("1.Notunuzu giriniz :"))
alinanNot2 = int(input("2.Notunuzu giriniz :"))

if alinanNot1 < 0 or alinanNot1 > 100 or alinanNot2 < 0 or alinanNot2 > 100 :
    print("oyle bir not degeri bulunamadi!")
else :
    ortalama = (int(alinanNot1) + int(alinanNot2)) / 2
    if ortalama <= 100:
        YilSonuOrtalamasi =5
    if ortalama <= 85:
        YilSonuOrtalamasi =4
    if ortalama <= 70:
        YilSonuOrtalamasi =3
    if ortalama <= 55:
        YilSonuOrtalamasi =2
    if ortalama <= 45:
        YilSonuOrtalamasi =1

print("ortalamaniz :", ortalama)
print("karne Notunuz :",YilSonuOrtalamasi )