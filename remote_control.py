import random
import time


class Kumanda():

    def __init__(self, tv_durum="kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt", altyazı_durum="kapalı",
                 altyazı_dilleri=["türçe"], altyazı="Türkçe", dil_adları=["türkçe"], dil="türkçe"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.altyazı_durum = altyazı_durum
        self.altyazı_dilleri = altyazı_dilleri
        self.altyazı = altyazı
        self.dil_adları = dil_adları
        self.dil = dil

    def tv_aç(self):
        if self.tv_durum == "açık":
            print("televizyon zaten açık")

        else:
            print("televizyon açılıyor")
            self.tv_durum = "açık"

    def tv_kapa(self):
        if self.tv_durum == "kapalı":
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor")
            self.tv_durum = "kapalı"

    def ses_ayarları(self):
        while True:
            işlem = input("sesi azalt: <\nsesi artır: >\n(çıkmak için q ya bas):")
            if işlem == "q":
                print("çıkılıyor")
                break

            elif işlem == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("televizyon sesi:", self.tv_ses)

            elif işlem == ">":
                if self.tv_ses < 31:
                    self.tv_ses += 1
                    print("televizyon sesi:", self.tv_ses)

            else:
                print("ses güncellendi", self.tv_ses)

    def kanal_ekle(self, kanal_ismi):
        print("kanal eklniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şuanki kanal:", self.kanal)

    def altyazı_aç(self):
        if self.altyazı_durum == "açık":
            print("altyazı zaten açık")

        else:
            print("altyazı açılıyor")
            self.altyazı_durum = "açık"

    def altyazı_kapa(self):
        if self.altyazı_durum == "kapalı":
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapanıyor")
            self.altyazı_durum = "kapalı"

    def altyazı_ekle(self, altyazı_dili):
        print("altyazı ekleniyor")
        time.sleep(1)
        self.altyazı_dilleri.append(altyazı_dili)
        print("altyazı eklendi")

    def rastgele_altyazı(self):
        rastgele = random.randint(0, len(self.altyazı_dilleri) - 1)
        self.altyazı = self.altyazı_dilleri[rastgele]
        print("şuanki dil:", self.altyazı)

    def dil_ekle(self, dil_adı):
        print("dil ekleniyor")
        time.sleep(1)
        self.dil_adları.append(dil_adı)
        print("dil eklendi")

    def rastgele_dil(self):
        rastgele = random.randint(0, len(self.altyazı_dilleri) - 1)
        self.dil = self.dil_adları[rastgele]
        print("şuanki dil:", self.dil)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "tv durumu: {}\ntv ses: {}\nkanal listesi: {}\nkanal: {}\naltyazı durum: {}\naltyazı dilleri: {}\naltyazı: {}\ndil adları: {}\ndil: {}".format(
            self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal, self.altyazı_durum, self.altyazı_dilleri,
            self.altyazı, self.dil_adları, self.dil)


kumanda = Kumanda()

print("""
    *******************************

    1. TV AÇ

    2. TV KAPA

    3. SES AYARLARI

    4. KANAL EKLE

    5. KANAL SAYISI

    6. RASTGELE KANAL

    7. BİLGİLERİ GÖSTER

    8. ALTYAZI AÇ

    9. ALTYAZI KAPA

    10. ALTYAZI EKLE

    11. RASTGELE ALTYAZI

    12. DİL EKLE

    13. RASTGELE DİL

*****************************
    """)

while True:
    işlem = input("işlem numarası giriniz:")
    if işlem == "q":
        print("çıkılıyor")
        break
    elif işlem == "1":
        kumanda.tv_aç()

    elif işlem == "2":
        kumanda.tv_kapa()

    elif işlem == "3":
        kumanda.ses_ayarları()

    elif işlem == "4":
        kanal_isimleri = input("eklemek istediğiniz kanalları',' ile ayırarak yazınız:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem == "5":
        print(len(kumanda))

    elif işlem == "6":
        kumanda.rastgele_kanal()


    elif işlem == "7":
        print(kumanda)


    elif işlem == "8":
        kumanda.altyazı_aç()

    elif işlem == "9":
        kumanda.altyazı_kapa()


    elif işlem == "10":
        altyazı_isimleri = input("eklemek istediğiniz altyazıları ',' ile ayırarak yazınız:")
        altyazı_dilleri = altyazı_isimleri.split(",")
        for eklenecekler1 in altyazı_dilleri:
            kumanda.altyazı_ekle(eklenecekler1)

    elif işlem == "11":
        kumanda.rastgele_altyazı()

    elif işlem == "12":
        diller = input("eklemek istediğiniz dilleri ',' ile ayırarak yazınız:")
        dil_adları = diller.split(",")
        for eklenecekler2 in dil_adları:
            kumanda.dil_ekle(eklenecekler2)

    elif işlem == "13":
        kumanda.rastgele_dil()


    else:
        print("yanlış işlem numarası.")
