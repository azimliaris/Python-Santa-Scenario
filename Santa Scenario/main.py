from Reindeer import Reindeer
from SleighScenario import SleighScenario

"""
    Hocam standart popülasyonu 30 000 olarak aldım çünkü geyiklere hız ataması yaparken anlamlı bir
sonuç çıksın diye. Ayrıca program geyiklerin oluşturulan senaryodaki mevcut durumlarının atamasını
yaparak başlıyor sonrasında ise geyikleri kızağa bağlarmışçasına SleighScenario sınıfının özellikleri
dolduruluyor ve bu sınıfa aktarılan parametrelerle sonucu döndürüyor.

Normal şartlar altında standart senaryoyu şu şekilde düşündüm ve bunun üzerinden değerleri verdim:
Tüm geyikler koşuyor. (8 geyik de ayakta)
Noel babanın kilosunda oynama yok.(Herhangi bir oynamada yüzde 20 artış ya da azalış gerçekleşiyor.)
Çocuk popülasyonunda beklenmedik bir artış yok.(Standart Popülasyon = 30 000)
Ayrıca bu normal şartlar ile 300 dakika içinde 30 000 hediye dağıtılabiliyor.(Dakikada 100 hediye totalde)

Dasher's speed 5, Dancer's speed 5, Prancer's speed 5, Vixen's speed 10
Comet's speed 10, Cupid's speed 15, Donder's speed 20, Blitzen's speed 30

(Bunları türkçe yazdım çünkü zaman kalmadı hocam kusura bakmayın.)

"""

#Geyikleri kızağa bağlayıp senaryoları başlatan fonksiyon.
def startScenario():
    nameList = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donder", "Blitzen"]
    injuredList = []
    totalSpeed = 0
    print("Creating the scenario\n")

    #Yaralı geyikleri kullanıcı belirler ve bir listeye kaydedilir
    for i in range(8):
        val = input("Is " + nameList[i] + " injured?(yes/no) ")
        print(val)
        if val.upper() == "YES":
            injuredList.append(nameList[i])
        elif val.upper() == "NO":
            pass
        else:
            raise SyntaxError('MEANNINGLESS WORDS!!!')
        nameList[i] = Reindeer(nameList[i], val)
        totalSpeed += nameList[i].speed

    #Noel babanın kilo durumuna karar verilir.
    santaKgStatus = input("What is Santa's kg status?(+/-/0) ")
    print(santaKgStatus)
    #Popülasyone karar verilir.
    houseNumber = input("Is children population default(30 000) or not?"
                        "(yes/give population more than 30 000) ")
    print(houseNumber)

    if houseNumber.upper() == "YES":
        print(SleighScenario(totalSpeed, santaKgStatus, injuredList))
    else:
        print(SleighScenario(totalSpeed, santaKgStatus, injuredList, houseNumber))


startScenario()
