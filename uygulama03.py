#sözlük kullanarak basit bir telefon rehberi uygulaması

telefon_rehberi = {"tokio" : "0542 465 56 58",
                   "rio": "0536 945 86 09",
                   "berlin" : "0553 741 37 55",
                   "professor"  : "0333 333 33 33"}

kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

cevap = "{} adlı kişinin telefon numarası: {}"

if kişi in telefon_rehberi:
    cevap = "{} adlı kişinin telefon numarası: {}"
    print(cevap.format(kişi, telefon_rehberi[kişi]))
else:
    print("Aradığınız kişi telefon rehberinde yok!")