# Öğrenci sınıfı tanımlama
class Ogrenci:
    def __init__(self, ad, soyad, numara, sinif):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.sinif = sinif

# Öğrenci kaydı ekleme fonksiyonu
def ogrenci_ekle(ogrenci_listesi):
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    numara = input("Öğrencinin numarasını girin: ")
    sinif = input("Öğrencinin sınıfını girin: ")
    yeni_ogrenci = Ogrenci(ad, soyad, numara, sinif)
    ogrenci_listesi.append(yeni_ogrenci)
    print("Öğrenci kaydı başarıyla eklendi.")

# Ana program
ogrenci_listesi = []
while True:
    print("1 - Öğrenci kaydı ekle")
    print("2 - Öğrenci sil")
    print("3 - Tüm öğrencileri listele")
    print("4 - Çoklu sil")
    print("5 - Çıkış")
    secim = input("Yapmak istediğiniz işlemi seçin: ")
    if secim == "1":
        ogrenci_ekle(ogrenci_listesi)
    elif secim == "2":
        numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
        for ogrenci in ogrenci_listesi:
            if ogrenci.numara == numara:
                ogrenci_listesi.remove(ogrenci)
                print("Öğrenci kaydı başarıyla silindi.")
                break
        else:
            print("Belirttiğiniz numaraya sahip öğrenci bulunamadı.")
    elif secim == "3":
        if len(ogrenci_listesi) == 0:
            print("Kayıtlı öğrenci yok.")
        else:
            for ogrenci in ogrenci_listesi:
                print("Ad:", ogrenci.ad)
                print("Soyad:", ogrenci.soyad)
                print("Numara:", ogrenci.numara)
                print("Sınıf:", ogrenci.sinif)
                print("--------------------")
    elif secim == "4":
        numaralar = input("Silmek istediğiniz öğrencilerin numaralarını virgülle ayırarak girin: ")
        numaralar_listesi = numaralar.split(",")
        silinen_sayisi = 0
        for numara in numaralar_listesi:
            for ogrenci in ogrenci_listesi:
                if ogrenci.numara == numara:
                    ogrenci_listesi.remove(ogrenci)
                    silinen_sayisi += 1
                    break
        print(silinen_sayisi, "adet öğrenci kaydı başarıyla silindi.")
    elif secim == "5":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")