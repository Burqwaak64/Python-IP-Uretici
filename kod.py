import geocoder
import random

print("Devam etmeden önce komuttaki uyarıları/bilgilendirmeleri okuduğunuzdan emin olun!")
country=input('Ülkenin İngilizce kısaltması » ')
city=input('Ülkenin içindeki şehrin İngilizce adı » ')
first = random.randint(1, 255)
second = random.randint(0, 255)
third = random.randint(0, 255)
fourth = random.randint(0, 255)
ipadress=f'{first}.{second}.{third}.{fourth}'
g=geocoder.ip(ipadress)
while (str(g.country)!=str(country) or str(g.city)!=str(city)):
    first = random.randint(1, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    fourth = random.randint(0, 255)
    ipadress=f'{first}.{second}.{third}.{fourth}'
    g=geocoder.ip(ipadress)
print(f"Komut başarıyla tamamlandı!\nÜretilen IP: {ipadress}")
