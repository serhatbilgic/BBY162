erkekismi= input("Bir erkek ismi giriniz:")
kadınismi= input("Bir bayan ismi giriniz:")
dize= int(input("Dize sayısı giriniz...Maksimum 10 mısra yazdırılabilir.."))


sarkı = ["Giden her sevgilinin ardından "," " + kadınismi+ " " ,"Hep biz olduk el sallayan ","Haykırsak duyarlar mı sesimizi? ","Hangi sevdadan galip çıktık ki? " ," " + erkekismi+ " ", "Boşuna çekilmedi bunca çile "," " + kadınismi+ " ", "İçiyoruz gündüz gece ", " " + erkekismi+ " ", "Haykırdık ama duymadı hiç kimse ","Peşindeyiz heryerde… "," " + erkekismi+" ", "Zaten aşklar hep yalan dolan "," "+ erkekismi+" ","Sonu hep acı hüsran "]


for olusturulacak_sarkı in sarkı[:dize]:
    print(olusturulacak_sarkı)

if dize > 10:
    print("En az 10 tane dize giriniz...")




