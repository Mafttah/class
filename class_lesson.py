# class
class Araba: # Class tanımlaması. class key word ile tanimliyoruz. 
    def __init__ (self, marka, model, yil, renk, beygir_gucu): # Constructor metodu. Bu metod sınıfın örneği oluşturulurken çağrılır.
        self.marka = marka # Ozellik (attribute)
        self.model = model
        self.yil = yil
        self.renk = renk
        self.beygir_gucu = beygir_gucu
    # Genel olarak bir class yapisi kendi cotstractor metotdu ile bu sekilde 

    def calistir(self):
        print(f"{self.marka} {self.model} calisti!")
    
    def durdur(self):
        print(f"{self.marka} {self.model} durdu!\n")
    
    def arac_bilgisi(self):
        # print(f"Marka: {self.marka}\nModel: {self.model} \nYil: {self.yil}\nRenk:{self.renk} \nMotor Gucu: {self.beygir_gucu} ")
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Yil: {self.yil}")
        print(f"Renk: {self.renk}")
        print(f"Motor Gucu: {self.beygir_gucu}\n")




#object
baris_araba = Araba("Tesla","Model Y","2024","Bordo","300ps")
zeynep_araba = Araba("Volvo","V40","2017","Beyaz","170ps")


# print(f"\nBaris Araba Marka: {baris_araba.marka}\n")
# print(f"Zeynep Araba Yil: {zeynep_araba.yil}\n")

# arac_model = baris_araba.model

# print(f"Baris arac modeli: {arac_model} Baris Arac Renk: {baris_araba.renk}")

# baris_araba.calistir()
# baris_araba.durdur()

# zeynep_araba.calistir()
# zeynep_araba.durdur()


baris_araba.arac_bilgisi()
zeynep_araba.arac_bilgisi()