alinanNot = int(input("Notunuzu giriniz:"))
if alinanNot < 0 or alinanNot > 100 :
    print("gecersiz bir not degeri girdiniz!!!")
elif alinanNot<50 :
    print("Maalesef kaldiniz!!!")
else :
    print(" Tebrikler gectiniz")
mesaj = "notunuz {}'dir "
print(mesj.format(alinanNot))