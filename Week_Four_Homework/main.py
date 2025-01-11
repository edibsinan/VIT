# main.py

'''
KütüphaneProjesi

- main.py                    # Ana dosya, kullanici etkilesimi burada olacak
- kitap_transactions.py      # Kitap islemleri (kitap ekleme, odunc verme vb.)
- member_Transactions.py     # Uye islemleri (uye ekleme, listeleme vb.)
- zaman.py                   # Zaman hesaplama,
- uye.json                   # Uye verileri burada tutulacak
- kitaplar.json              # Kitap verileri burada tutulacak
- taksi.json                 # Odunc alinan kitaplarin takibini yapar)
'''

import os
import json
from kullanici_islemleri import uye_ekle, uye_sil, uye_arama, uye_durum,uyeleri_listele, kitap_odunc_ver, kitap_iade,kitap_takibi
from kitap_islemleri import kitap_ekle, kitap_sil, kitap_ara, kitaplari_listele
from zaman import mevcut_tarih, iade_tarihi
# import cagirma seklini sor 

def uye_paneli():
    while True:
        print("\nUYELIK ISLEMLERI")
        print("1. Uyeler")
        print("2. Uye Ekleme")
        print("3. Uye Ara")
        print("4. Uye Sil")
        print("5. Kitap Odunc Verme")
        print("6. Kitap Iade")
        print("7. Kitap Takibi")
        print("0. CIKIS")
        
        secim = input("Lutfen giris yapmak istediginiz secimin kodunu giriniz: ")

        if secim == "1":
            print("Uyeler listelenecek...")
            uyeleri_listele()
        elif secim == "2":
            isim = input("Üye ismini giriniz: ").upper()
            telefon = input("Üye telefon numarasını giriniz: ")
            uye_ekle(isim, telefon)  # İsim ve telefon parametrelerini geçir
        elif secim == "3":
            uye_id = int(input("Aramak istediğiniz üyenin ID numarasını giriniz: "))
            uye_arama(uye_id)
        elif secim == "4":
            uye_sil()
        elif secim == "5":
            kitap_adi = input("Ödünç verilecek kitabın adını giriniz: ").upper()
            uye_isim = input("Üyenin adını giriniz: ").upper()
            kitap_odunc_ver(kitap_adi, uye_isim)
        elif secim == "6":
            kitap_adi = input("Geri alınacak kitabın adını giriniz: ").upper()
            uye_isim = input("Üyenin adını giriniz: ").upper()
            kitap_iade(kitap_adi, uye_isim)
        elif secim == "7":
            kitap_takibi()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")






def kitap_paneli():
    while True:
        print("\nKITAP ISLEMLERI")
        print("1. Kitapları Listele")
        print("2. Kitap Ekleme")
        print("3. Kitap Ara")
        print("4. Kitap Sil")
        print("0. Ana Menüye Dön")

        secim = input("Lütfen seçim yapınız: ")

        if secim == "1":
            kitaplari_listele()
        elif secim == "2":  # Kitap ekleme seçeneği
            kitap_adi = input("Kitap adını giriniz: ").upper()
            yazar = input("Yazar adını giriniz: ").upper()
            yil = input("Basım yılını giriniz: ")
            kitap_ekle(kitap_adi, yazar, yil)  # Parametreleri burada iletin
        elif secim == "3":
            kitap_adi = input("Aramak istediğiniz kitabın adını giriniz: ").upper()
            kitap_ara(kitap_adi)
        elif secim == "4":
            kitap_sil()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim!")




def main():
    while True:
        print("\nHALK KUTUPHANESINE HOSGELDİNİZ")
        print("1. Uyelik Islemleri")
        print("2. Kitap Islemleri")
        print("0. CIKIS")

        secim = input("Lutfen giris yapmak istediginiz secimin kodunu giriniz: ")

        if secim == "1":
            uye_paneli()
        elif secim == "2":
            kitap_paneli()
        elif secim == "0":
            print("Cikiliyor...")
            break
        else:
            print("Gecersiz secim!")

if __name__ == "__main__":
    main()