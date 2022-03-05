def dosya_kopyala(eskidosya,yenidosya):
    with open(eskidosya) as file:
        icerik = file.read()
    with open(yenidosya,"w") as file:
        file.write(icerik)

# dosya_kopyala("m.txt","r.txt")

def ters_cevir(eskidosya,yenidosya):
    with open(eskidosya) as file:
        icerik = file.read()
    with open(yenidosya,"w") as file:
        file.write(icerik[::-1])

# ters_cevir("m.txt","ters.txt")

def detaylar(dosya):
    with open(dosya) as file:
        satırlar = file.readlines()

    sonuc = {
        "satır sayısı " : len(satırlar),
        "kelime sayısı " :  sum(len(satır.split(" ")) for satır in satırlar)  ,
        "karakter sayısı " :  sum(len(satır) for satır in satırlar)
    }
    return sonuc

# print(detaylar("m.txt"))

# 1-Kullanıcıdan aldığı ürün bilgisini (ad,fiyat) urunler.txt dosyasına kaydeden fonksiyon

def urunekle(ad,fiyat):
    with open("urunler.txt","a",encoding="UTF-8") as file:
        file.write(f"Ürün adı : {ad} Fiyat : {fiyat} \n")
    
# urunekle("Iphone",100)
# urunekle("Samsung",400)

# 2-Kullanıcıdan aldığı ürün bilgisini (ad,fiyat) urunler.txt dosyasına kaydeden fonksiyon

def bul_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate()

# bul_degistir("urunler.txt","adı","Adı")
