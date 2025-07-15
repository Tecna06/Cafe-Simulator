# Menü ve fiyatlar
menu = {
    "Kahve": 15,
    "Çay": 10,
    "Kek": 20,
    "Sandviç": 25
}
siparisler = []  # Siparişleri tutacak liste

def menu_goster():
    print("---MENÜ---")
    for urun, fiyat in menu.items():
        print(f"{urun},{fiyat}TL")


def siparis_al():
    while True:
        secim = input("sipariş vermek istediğiniz ürünü yazın: veya çıkmak için Q:").title()
        if secim == "q":
            break

        if secim in menu:
            try:
                adet = int(input(f"{secim} kaç adet istersiniz? "))
                if adet > 0:
                    siparisler.append((secim, adet, menu[secim]))
                    print(f"{adet} adet {secim} siparişinize eklendi.")
                else:
                    print("Adet 1 veya daha fazla olmalı.")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        else:
            print("Menüde böyle bir ürün yok.")

def siparis_ozeti():
    print("\n----- Sipariş Özeti -----")
    toplam = 0
    for urun, adet, fiyat in siparisler:
        tutar = adet * fiyat
        toplam += tutar
        print(f"{urun} x {adet} = {tutar} TL")
    print(f"Toplam: {toplam} TL")

def main():
    print("Cafe Sipariş Sistemine Hoşgeldiniz!")
    menu_goster()
    siparis_al()
    siparis_ozeti()
    print("Afiyet olsun!")

if __name__ == "__main__":
    main()
