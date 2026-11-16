# 1. Juku
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
from math import pi


nimi=input("Sissesta teie nimi: ")
if nimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if nimi.isupper():
        print("Ära karju, Juku!")
    try:
        vanus=int(input("Kui vana sa oled? "))
        if 0 <= vanus < 6:
            Pilet="tasuta"
        elif 6 <= vanus < 14:
            Pilet="Lastepilet"
        elif 15 <= vanus < 65:
            Pilet="täispilet"
        elif 65 <= vanus < 120:
            Pilet="Sooduspilet"
    except:
        print("Sissesta vanus numbriga!")
    try:
        print(f"Jutku vanus on {vanus} aastat, ta ostab {Pilet}")
    except:
       print("viga andmetes.")
else:
    print("täna kinno ei minda")

# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

pinginaabrid=["Denis", "Anna", "Dima", "Sasha"]
nimi1=input("Sissesta esimene nimi: ")
nimi2=input("Sissesta teine nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
    else: print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
else: print ("Sissesta nimed")

valik=input("Kas soovid otsida nimede algustähtede järgi? ").lower()
otsing=False
if valik == "jah":
    algustäht=input("sissesta algustäht: ").capitalize()
    for nimi in pinginaabrid:
        if nimi.startswith(algustäht):
            print(f"{nimi} algab tähtega {algustäht}.")
            otsing=True
    if not otsing: print(f"nimi mis algab tähtega {algustäht} ei leitud")
else: print("otsingut ei tehta.")

# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi?
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
try:
    toa_pikkus=float(input("sissesta toa pikkus: "))
    toa_laius=float(input("sissesta toa laius: "))
    pindala=round(toa_laius*toa_pikkus,1)
    print(f"Teie ruumi pindala on {pindala} meetri")
    valik=input("Kas tahate teha remont? (jah/ei) ").lower()
    if valik == "jah":
        try:
            hind=round(float(input("Kui palju ruutmetri maksab? ")),2)
            remont_hind=round(hind*pindala,2)
            valik=input("Kas teeme remondi ise? (jah/ei) ").lower()
            if valik == "ei":
                hind_too=round(float(input("Kui palju töö maksab iga meetri? ")),2)
                remont_ja_too=round((hind_too+hind)*pindala,2)
                print(f"remont maksab {remont_hind}€,iga meeter professionaali abi maksab {hind_too}€, remont maksab {remont_ja_too}€")
            elif valik == "jah":
                print(f"remont maksab {remont_hind}€")
            else:
                print("Kirjuta ainult jah või ei")
        except: print("Palun sissesta meetri hind")
    else: print("Sa ei taha remonti teha")
except: print("Palun sissesta ainult numbrid")

# Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. 
# Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.
try:
    hind=float(input("sissesta toote hind: "))
    if hind > 700: print(f"teie on 30% soodus, hind on {hind-hind*0.3}")
    else: print(f"hind on {hind}")
except: print("sissesta hind numbriga")
