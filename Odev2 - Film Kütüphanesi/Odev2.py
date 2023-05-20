import json


class Film:
    def __init__(self, isim, tur, yonetmen):
        self.isim = isim
        self.tur = tur
        self.yonetmen = yonetmen

    def to_dict(self):
        return {
            'isim': self.isim,
            'tur': self.tur,
            'yonetmen': self.yonetmen
        }


class FilmKutuphanesi:
    def __init__(self, dosya):
        self.dosya = dosya

    def film_ekle(self):
        film_isim = input("Film ismini girin: ")
        film_tur = input("Film türünü girin: ")
        film_yonetmen = input("Film yönetmenini girin: ")

        film = Film(film_isim, film_tur, film_yonetmen)
        film_dict = film.to_dict()

        with open(self.dosya, 'a') as dosya:
            json.dump(film_dict, dosya)
            dosya.write('\n')
        print("Film Kayit Edildi. ")

    def film_ara(self, aranan_isim):
        with open(self.dosya, 'r') as dosya:
            for satir in dosya:
                film_dict = json.loads(satir)
                film = Film(**film_dict)
                if film.isim == aranan_isim:
                    print("Film Bulundu:")
                    print("İsim:", film.isim)
                    print("Tür:", film.tur)
                    print("Yönetmen:", film.yonetmen)
                    return

        print("Film Bulunamadı.")


film_kutuphanesi = FilmKutuphanesi('filmler.json')

while True:
    print("1. Film Ekle")
    print("2. Film Ara")
    print("3. Çıkış")

    secim = input("Seçiminizi yapın (1-3): ")

    if secim == '1':
        film_kutuphanesi.film_ekle()
    elif secim == '2':
        aranan_isim = input("Aranacak film ismini girin: ")
        film_kutuphanesi.film_ara(aranan_isim)
    elif secim == '3':
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")