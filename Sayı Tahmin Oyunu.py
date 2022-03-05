import random
import time

print("""
Sayı Tahmin Oyunu
1-1000 arasındaki sayıyı tahmin edin :)
""")

sayı = random.randint(1,1000)
tahmin_hakkı = 10

while True:
    tahmin = int(input("Bir sayı giriniz : "))

    if (tahmin > sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük sayı söyleyin...")
        tahmin_hakkı -= 1
    elif (tahmin < sayı):
        print("Bilgiler sorgularnıyor...")
        time.sleep(1)
        print("Daha büyük sayı söyleyin...")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgularnıyor...")
        time.sleep(1)
        print("Doğru bildiniz!",tahmin)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti...")
        time.sleep(1)
        print("Doğru sayı",sayı)
        break


