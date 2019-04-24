Python 2.7.1 (r271:86832, Nov 27 2010, 18:30:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #1.uygulama

metin = "Açýk bilim, araþtýrma çýktýlarýna ve süreçlerine herkesin serbestçe eriþmesini, bunlarýn ortak kullanýmýný, daðýtýmýný ve üretimini kolaylaþtýran bilim uygulamasýdýr."

metin = list(metin)
for i in range(20):
    print(metin[i],end="")
    
>>> #2.uygulama

liste = ["Açýk Bilim", "Açýk Eriþim", "Açýk Lisans", "Açýk Eðitim", "Açýk Veri", "Açýk Kültür"]

for i in metin :
    print(i)
    
>>> #3.uygulama

sozluk = {“Elma” : “Aðaçta yetiþen bir tür meyve” , “Salatalýk” : “Fidan üzerinde büyüyen bir tür sebze” }
arma = str(input("ne aramak istiyorsun?")
try :
    print(sozluk[arama])
except KeyError :
     print("Tekrar Deneyiniz")

SyntaxError: invalid syntax
>>> #3.uygulama

sozluk = {"Elma" : "Aðaçta yetiþen bir tür meyve" , "Salatalýk" : "Fidan üzerinde büyüyen bir tür sebze" }
arma = str(input("ne aramak istiyorsun?")
try :
    print(sozluk[arama])
except KeyError :
     print("Tekrar Deneyiniz")
	   
>>> 
