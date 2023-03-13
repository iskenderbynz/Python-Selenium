database = []

def newCreate():
    database.append(input("Ad soyad giriniz : "))
    menu()

def lists():
    for index, i in enumerate(database):
        print(index," - ", i) 
    menu()

def delete():
    bul = input("Silmek istediğiniz kaydı belirtiniz : ")
    database.remove(bul)
    menu()

def find():
    bul = input("Numarasını öğrenmek istediğiniz öğrenciyi yazınız : ")
    print(database.index(bul))
    menu()

def multipleDelete():
    deleteDb = []
    deleteDb = input("Toplu kayıt silmek için öğrenci numaralarını virgül (,) ile ayırarak belirtiniz.: ").split(",")
    i = 0
    while i < len(deleteDb):
        database.pop(int(deleteDb[i]))
        i = i + 1
    menu()

def menu():
    print("1 : Yeni öğrenci ekle")
    print("2 : Kayıtları listele")
    print("3 : Kayıt sil")
    print("4 : Toplu kayıt sil")
    print("5 : Öğrenci numarası öğren")
    islem = input("Yapmak istediğiniz işlemi belirtiniz : ")
    if islem == "1":
        newCreate()
    elif islem == "2":
        lists()
    elif islem == "3":
        delete()
    elif islem == "4":
        multipleDelete()
    elif islem == "5":
        find()
   
menu()

