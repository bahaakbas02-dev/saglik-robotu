print("""
Sağlık Robotuna Hoşgeldiniz!
    
      -1 Ateşlenme
      -2 Boğaz Ağrısı
      -3 Soğuk Algınlığı
      -4 Burun Akıntısı
      -5 Mide Bulantısı
      -6 Alerji
      -7 Baş Dönmesi
      -8 Vitamin Eksikliği
      -9 Uykusuzluk
      -10 Diyabet
      -11 İshal
      -12 Kabız
      -13 Tansiyon
      -14 Göz Yanması
      -15 Burun Tıkanıklığı
      -16 Karaciğer Yağlanması
      -17 Nabız
      -18 Mide Yanması  
      -19 Kolestrol
      -20 Demir Eksikliği
""")

secim = int(input("Hastalığın Numarasını Giriniz: ").strip())

if secim == 1:
    print("Sizin İçin Gerekli Olan İlaç Calpol")

elif secim == 2:
    print("Sizin İçin Gerekli Olan İlaç Majezik")

elif secim == 3:
    print("Sizin İçin Gerekli Olan İlaç İburamin Zero")

elif secim == 4:
    print("Size Gerekli Olan İlaç Sterimar Stop & Protect")

elif secim == 5:
    print("Size Gerekli Olan İlaç Buscovan ve Granisetron")

elif secim == 6:
    print("Size Gerekli Olan İlaç Zytrec")

elif secim == 7:
    print("Size Gerekli Olan İlaç Dramamine")   

elif secim == 8:
    print("Size Gerekli Olan İlaç Feramat")

elif secim == 9:
    print("Size Gerekli Olan İlaç Ambien")

elif secim == 10:
    print("Size Gerekli Olan İlaç Glifor")

elif secim == 11:
    print("Size Gerekli Olan İlaç Raxerin")

elif secim == 12:
    print("Size Gerekli Olan İlaç DulceSoft")

elif secim == 13:
    print("Size Gerekli Olan İlaç Benipin")

elif secim == 14:
    print("Size Gerekli Olan İlaç Tobrex")  

elif secim == 15:
    print("Size Gerekli Olan İlaç Sinomarin")

elif secim == 16:
    print("Size Gerekli Olan İlaç Nutraxin")

elif secim == 17:
    print("Size Gerekli Olan İlaç Atropin")            

elif secim == 18:
    print("Size Gerekli Olan İlaç Acidpass")

elif secim == 19:
    print("Size Gerekli Olan İlaç Rosuvastatin")

elif secim == 20:
    print("Size Gerekli Olan İlaç Feritin") 

else:
    print("Hata! İlaç bulunuamadı.")   

input("Çıkmak İçin Enter'a basın...")    
