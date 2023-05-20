def kullanici_kayit():
    kullanici_bilgi = {}
    kullanici_adi = input("Kullanici adını girin")
    kullanici_sifre = input("Kullanici sifresini girin")
    kullanici_bilgi["kullanici_adi"] = kullanici_adi
    kullanici_bilgi["kullanici_sifre"] = kullanici_sifre
    with open("kullanici_bilgileri.txt", "a") as f:
        f.write(kullanici_bilgi["kullanici_adi"]+"," +
                kullanici_bilgi["kullanici_sifre"]+"\n")
    print("kullanıcı kayıt edildi")


def giris():
    Check_kullanici_adi = input("Kullanici adını girin")
    Check_kullanici_sifre = input("Kullanici sifresini girin")
    with open("kullanici_bilgileri.txt", 'r') as file:
        for line in file:
            Kayitli_kullanici_adi, Kayitli_kullanici_sifre = line.strip().split(",")
            if (Kayitli_kullanici_adi == Check_kullanici_adi and Kayitli_kullanici_sifre == Check_kullanici_sifre):
                return True
    return False


while True:
    secim = int(input("1-Kayıt,2-Giriş,3-Çıkış"))

    if secim == 1:
        kullanici_kayit()

    elif secim == 2:
        if (giris()):
            print("Giris Basarili")
        else:
            print("Giris Basarisiz")
    elif secim == 3:
        print("Çıkış yapılıyor")
        break
    else:
        print("Yanlış seçim yaptınız")
