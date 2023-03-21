class Human:
    #built-in
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def talk(self,sentence):
        print(f"{self.name} : {sentence}")
    def walk(self):
        print("Human is walking..")   

# instance => örnek
human1 = Human("İskender")
human1.talk("Merhaba")
human1.walk()


