


class Human:
    def __init__(self, isim, soyisim, para):
        self.isim = isim
        self.soyisim = soyisim
        self.para = para
    def parayi_goruntule(self):
        return self.para

    def para_gonder(self, human, amount):
        if self.para < amount:
            # TODO: custom exception yaz.
            print("Para yeterli değil ! Hesabınızda {} tl var.".format(self.para))
            return
        self.para = self.para - amount  
        human.para += amount
        print("Paranız {} {}'a gönderildi !".format(human.isim, human.soyisim))

human1 = Human("İsmail", "Bayram", 100)
human2 = Human("Fatih", "Bayram", 100)
            

h1 = int(input("Lütfen bir insan seçin (1, 2) --> ")) - 1
h2 = int(input("Lütfen bir insan seçin (1, 2) --> ")) - 1

humans = [human1, human2]


print(humans[h1].isim, humans[h1].soyisim, humans[h1].para)
print(humans[h2].isim, humans[h2].soyisim, humans[h2].para)
 

amount = int(input("Ne kadar para göndermek istiyorsunuz ? --> "))

humans[h1].para_gonder(humans[h2], amount)
print("Gonderen Hesap Bakiyesi --> ", humans[h1].parayi_goruntule())
print("Alıcı Hesap Bakiyesi --> ", humans[h2].parayi_goruntule())

   
  



        


