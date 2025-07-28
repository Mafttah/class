class EvcilHayvan:
    """
    Bu sınıf, sanal bir evcil hayvanın özelliklerini ve davranışlarını tanımlar.
    """
    def __init__(self, isim, tur):
        # Evcil hayvanın başlangıç özellikleri
        self.isim = isim
        self.tur = tur
        self.enerji = 100 # Maksimum 100
        self.aclik = 0   # Maksimum 100 (0 = tok, 100 = çok aç)
        self.mutluluk = 80 # Maksimum 100
        print(f"\n{self.isim} adında bir {self.tur} aramıza katıldı!")

    def besle(self):
        """Evcil hayvanı besler, açlığını azaltır."""
        if self.aclik == 0:
            print(f"{self.isim} zaten tok. Daha fazla yiyemez.")
        else:
            self.aclik = max(0, self.aclik - 30) # Açlığı 0'ın altına düşürme
            print(f"{self.isim} beslendi. Açlığı şimdi {self.aclik}.")

    def oynat(self):
        """Evcil hayvanla oynar, enerjisini azaltır, mutluluğunu artırır."""
        if self.enerji < 20:
            print(f"{self.isim} çok yorgun! Onunla oynayamazsın. Uyutmalısın.")
        else:
            self.enerji = max(0, self.enerji - 20) # Enerjiyi 0'ın altına düşürme
            self.mutluluk = min(100, self.mutluluk + 15) # Mutluluğu 100'ün üzerine çıkarmama
            print(f"{self.isim} ile oynandı. Enerjisi {self.enerji}, Mutluluğu {self.mutluluk}.")

    def uyut(self):
        """Evcil hayvanı uyutur, enerjisini artırır."""
        if self.enerji == 100:
            print(f"{self.isim} zaten dinlenmiş durumda.")
        else:
            self.enerji = min(100, self.enerji + 40) # Enerjiyi 100'ün üzerine çıkarmama
            print(f"{self.isim} uyudu ve dinlendi. Enerjisi şimdi {self.enerji}.")

    def durum_goster(self):
        """Evcil hayvanın mevcut durumunu görüntüler."""
        print(f"\n--- {self.isim} ({self.tur}) Durumu ---")
        print(f"Enerji: {self.enerji}/100")
        print(f"Açlık: {self.aclik}/100")
        print(f"Mutluluk: {self.mutluluk}/100")
        print("------------------------------")

    def zaman_gecir(self):
        """Her eylemden sonra evcil hayvanın durumunu biraz değiştirir (hayatı simüle eder)."""
        self.aclik = min(100, self.aclik + 10) # Zamanla acıkır
        self.enerji = max(0, self.enerji - 5) # Zamanla yorulur
        self.mutluluk = max(0, self.mutluluk - 5) # Zamanla sıkılır

        # Durum uyarıları
        if self.aclik >= 70:
            print(f"Uyarı: {self.isim} çok aç! Onu beslemelisin.")
        if self.enerji <= 20 and self.enerji > 0: # 0'da zaten yorgun uyarısı veriliyor
            print(f"Uyarı: {self.isim} yoruluyor! Onu uyutmalısın.")
        if self.mutluluk <= 30 and self.mutluluk > 0: # 0'da zaten mutsuz uyarısı veriliyor
            print(f"Uyarı: {self.isim} mutsuz! Onunla oynamalısın.")
        if self.enerji == 0:
            print(f"Uyarı: {self.isim} bitkin düştü! Hemen uyutmalısın.")
        if self.mutluluk == 0:
            print(f"Uyarı: {self.isim} çok mutsuz! Acilen onunla oynamalısın.")

def ana_menu():
    """Kullanıcıya menüyü gösterir ve seçimini alır."""
    print("\n--- Evcil Hayvan Menüsü ---")
    print("1. Evcil Hayvanı Besle")
    print("2. Evcil Hayvanla Oyna")
    print("3. Evcil Hayvanı Uyut")
    print("4. Durumu Göster")
    print("5. Çıkış")
    print("----------------------------")
    while True:
        try:
            secim = int(input("Seçiminizi yapın (1-5): "))
            if 1 <= secim <= 5:
                return secim
            else:
                print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

# --- Programın Başlangıcı ---
# Programı çalıştırma anındaki __name__ ve __main__ yapısını anlamadım tekrar kontrol edelim. 
if __name__ == "__main__":
    print("Sanal Evcil Hayvanınız Uygulamasına Hoş Geldiniz!")

    # Evcil hayvanın adını ve türünü kullanıcıdan al
    evcil_hayvan_adi = input("Evcil hayvanınızın adını girin: ")
    evcil_hayvan_turu = input("Evcil hayvanınızın türünü girin (örn: Köpek, Kedi, Kuş): ")

    # Evcil hayvan nesnesini oluştur
    benim_evcil_hayvanim = EvcilHayvan(evcil_hayvan_adi, evcil_hayvan_turu)

    while True:
        secim = ana_menu()

        if secim == 1:
            benim_evcil_hayvanim.besle()
        elif secim == 2:
            benim_evcil_hayvanim.oynat()
        elif secim == 3:
            benim_evcil_hayvanim.uyut()
        elif secim == 4:
            benim_evcil_hayvanim.durum_goster()
        elif secim == 5:
            print(f"Hoşça kalın, {benim_evcil_hayvanim.isim} sizi özleyecek!")
            break # Döngüden çıkış

        # Her eylemden sonra zamanın geçmesini simüle et
        if secim != 4: # Durum göstermek zaman geçirmez
            benim_evcil_hayvanim.zaman_gecir()