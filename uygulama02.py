a = input("saniye girin:")
print ("yıl:",int(int(a)/31104400))
b = int(a)%31104400
print ("ay:",int(int(b)/2592000))
c = int(b)%2592000
print ("gün:",int(int(c)/86400))
d = int(c)%86400
print ("saat:",int(int(d)/3600))
e = int(d)%3600
print ("dakika:",int(int(e)/60))
g = int(e)%60
print ("saniye:",g)