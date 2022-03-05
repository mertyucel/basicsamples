import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt","a"],kanal = "Trt") -> None:
        
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Tv zaten açık")
        else:
            print("Tv açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapatılıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\n Sesi arttır: '>'\n Çıkış: 'çıkış'")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    print("Ses azaltılıyor...")
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses minumum düzeyde!")
                    
            elif (cevap == ">"):
                if (self.tv_ses != 32):
                    print("Ses arttırılıyor...")
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses maximum düzeyde!")
                    
            else:
                print("Ses güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi.")

    def rastgele_kanal(self):
        
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şaun ki kanal",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\n Kanal Listesi : {}\n Şuanki kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""

Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")

while True:
    islem = input("yapılacak işlemi giriniz...")

    if (islem == "q"):
        print("Çıkış yapılıyor...")
        break
    elif (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem == "3"):
        kumanda.ses_ayarları()   
    elif (islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):
        print("Kanal Sayısı:",len(kumanda))
    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem......")