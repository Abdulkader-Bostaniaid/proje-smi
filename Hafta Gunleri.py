sayi = int(input("1-7 arasinda bir sayi giriniz :"))
if sayi >= 1 and sayi<= 7 :
    if sayi ==1 :
        print("pazartesi")
    if sayi ==2 :
        print("sali")
    if sayi == 3:
        print("carsamba")
    if sayi == 4:
        print("persembe")
    if sayi == 5:
        print("cuma")
    if sayi == 6:
        print("cumartesi")
    if sayi == 7:
        print("pazar")
else:
    print("gecersiz bir deger girdini!!!")