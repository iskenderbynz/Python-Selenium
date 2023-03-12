
#Python da veri tiplerini aşağıdaki şekilde listeleyebiliriz.

#String (Metin) Veri Tipleri → str

#Numerik (Sayısal) Veri Tipleri → int, float, complex

#Sequence (sıralama) Veri Tipleri → list, tuple, range

#Mapping (haritalama) Veri Tipleri → dict

#Set Veri Tipleri → set, frozenset

#Boolean Veri Tipleri → bool

#Binary Veri Tipleri → bytes, bytearray, memoryview

#---------------------------------------------------------------------------

#Eğitim Başlığı  - string 
#Yazar - string 
#Eğitim Tamamlanma Durumu - int 

#---------------------------------------------------------------------------



kurslar = ["Kurs 1", "Kurs 2", "Kurs 3"]
sorgu = input("Anahtar kelime giriniz..")
kayitDurum = False

for i in kurslar:
    if i.startswith(sorgu):
        kayitDurum = True
        break
    else:
        kayitDurum = False

if kayitDurum == True:
    print("****Uygun kayıtlar aşağıda listelenmiştir****")
    for i in kurslar:
        if i.startswith(sorgu):
            print(i)
else:
    print("Kayıt Bulunamadı.")   


  




