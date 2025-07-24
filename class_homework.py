MIN_DEGER = 0
MAX_DEGER = 100

class EvcilHayvan:
    def __init__(self, isim, tur, aclik, uyku, mutluluk, enerji):
        self.isim = isim
        self.tur = tur
        self.aclik = aclik
        self.uyku = uyku
        self.mutluluk = mutluluk
        self.enerji = enerji

    def aclik_kontrol(self):
        if self.aclik < 50:
            print(f"{self.isim} aç!")
        else:
            print(f"{self.isim} beslendi.")

    def oynat(self):
        if self.enerji < 50:
            print(f"{self.isim} çok yorgun!")
        else:
            self.enerji -= 20
            if self.enerji < MIN_DEGER:
                self.enerji = MIN_DEGER
            self.enerji += 15
            if self.enerji > MAX_DEGER:
                self.enerji = MAX_DEGER
            print(f"{self.isim} ile oynandı.\n")

    def mutluluk(self):
        if self.enerji < 50:
            print(f"{self.isim} az mutlu!")
        else:
            self.enerji += 10
            if self.enerji > MAX_DEGER:
                self.enerji = MAX_DEGER
            print(f"{self.isim} daha mutlu!\n")
        
    def uyku(self):
        if self.enerji < 50:
            print(f"{self.isim} uyuması lazım!")
        else:
            self.enerji -= 30
            if self.enerji < MIN_DEGER:
                self.enerji = MIN_DEGER
            self.enerji += 40
            if self.enerji > MAX_DEGER:
                self.enerji = MAX_DEGER
            print(f"{self.isim} uyudu ve dinlendi.\n")

    def enerji_kontrol(self):
        if self.enerji < 50:
            print(f"{self.isim} çok yorgun!")
        elif self.enerji <= 95:
            print(f"{self.isim} dinlenmesi lazım.")
        else:
            print(f"{self.isim} enerjisi yeterli.")

    def durum_goster(self):
        print(f"\n{self.isim} ->> Enerji: {self.enerji}, Açlık: {self.aclik}, Uyku: {self.uyku}, Mutluluk: {self.mutluluk}\n")


# Kullanıcıdan veri al
isim = input("\nEvcil hayvanınızın adını girin: ")
tur = input("Evcil hayvanınızın türünü girin (Kedi/Köpek/Kuş vb.): ")
aclik = int(input(f"{isim} için açlık seviyesini girin (0-100): "))
uyku = int(input(f"{isim} için uyku seviyesini girin (0-100): "))
mutluluk = int(input(f"{isim} için mutluluk seviyesini girin (0-100): "))
enerji = int(input(f"{isim} için enerji seviyesini girin (0-100): "))   

evcil_hayvan = EvcilHayvan(isim, tur, aclik, uyku, mutluluk, enerji)

# Menü
while True:
    print("\n1. Açlık Kontrolü")
    print("2. Uyku Kontrolü")
    print("3. Durumu Göster")
    print("4. Enerji Kontrolü")
    print("5. Oynat")
    print("6. Mutluluk")
    print("7. Çıkış")
    
    try:
        secim = int(input("Seçiminizi yapın (1-7): "))
    except ValueError:
        print("Lütfen 1 ile 7 arasında bir sayı girin.")
        continue

    if secim == 1:
        evcil_hayvan.aclik_kontrol()
    elif secim == 2:
        evcil_hayvan.uyku()
    elif secim == 3:
        evcil_hayvan.durum_goster()
    elif secim == 4:
        evcil_hayvan.enerji_kontrol()
    elif secim == 5:
        evcil_hayvan.oynat()
    elif secim == 6:
        evcil_hayvan.mutluluk()
    elif secim == 7:
        print("Çıkış yapılıyor")
        break
    else:
        print("Lütfen 1 ile 7 arasında geçerli bir seçim yapın.")