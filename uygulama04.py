Python 2.7.1 (r271:86832, Nov 27 2010, 18:30:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #1.uygulama

metin = "A��k bilim, ara�t�rma ��kt�lar�na ve s�re�lerine herkesin serbest�e eri�mesini, bunlar�n ortak kullan�m�n�, da��t�m�n� ve �retimini kolayla�t�ran bilim uygulamas�d�r."

metin = list(metin)
for i in range(20):
    print(metin[i],end="")
    
>>> #2.uygulama

liste = ["A��k Bilim", "A��k Eri�im", "A��k Lisans", "A��k E�itim", "A��k Veri", "A��k K�lt�r"]

for i in metin :
    print(i)
    
>>> #3.uygulama

sozluk = {�Elma� : �A�a�ta yeti�en bir t�r meyve� , �Salatal�k� : �Fidan �zerinde b�y�yen bir t�r sebze� }
arma = str(input("ne aramak istiyorsun?")
try :
    print(sozluk[arama])
except KeyError :
     print("Tekrar Deneyiniz")

SyntaxError: invalid syntax
>>> #3.uygulama

sozluk = {"Elma" : "A�a�ta yeti�en bir t�r meyve" , "Salatal�k" : "Fidan �zerinde b�y�yen bir t�r sebze" }
arma = str(input("ne aramak istiyorsun?")
try :
    print(sozluk[arama])
except KeyError :
     print("Tekrar Deneyiniz")
	   
>>> 
