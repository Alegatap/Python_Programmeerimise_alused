import random
from datetime import *
# #1. Juku
# # Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# # Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# # Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.

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

# # Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# # Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# # Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.
print()
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

# # Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# # Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# # Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi?
# # Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
print()
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

# # Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. 
# # Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.
print()
try:
    hind=round(float(input("sissesta toote hind: ")),2)
    if hind > 700: print(f"teie on 30% soodus, hind on {hind-hind*0.3}€")
    else: print(f"hind on {hind}€")
except: print("sissesta hind numbriga")

# # Küsi toatemperatuur ja teata, kas see on üle 18 kraadi (soovitatav toasoojus talvel).
# # Temperatuur võib olla ka negatiivne või kümnendarv, seega kontrolli sisendit try/except abil.
print()
try:
    temperatuur=int(input("Mis toatemperatuur on? "))
    if temperatuur >= 18: print("temperatuur on okay")
    else: print("tee temperatuur soojem!")
except: print("sissesta ainult täisarvud")

# # Küsi inimese pikkus sentimeetrites ja teata, kas ta on lühike, keskmise pikkusega või pikk.
# # Piirid pane ise paika ja kirjuta need programmi alguses kommentaarina.
# # küsi lisaks sugu. Meestele ja naistele kehtivad erinevad piirid. Tingimusplokid võivad olla üksteise sees.
# # Sugu võib sisestada mis tahes kujul (M, m, mees, MEES). Programm peab selle ära tundma.
# # Kui sugu on sisestatud valesti, kuva veateade.
print()
sugu=input("sisseta oma sugu: ")
if sugu.lower() == "m" or "mees" or "n" or "naine":             #See on alati "True", ei tea miks. Kui sa kirjutad, et sugu on "1", ta ei teha ELSE
     try:
         pikkus=int(input("sissesta teie pikkus(cm): "))
         if sugu == "m" or "mees":
             if pikkus < 150: print("sa oled lühike pikkus")
             elif 150 <= pikkus < 180: print("sa oled keskmine pikkus")
             else: print("sa oled pikk pikkus")
         else:
             if pikkus < 140: print("sa oled lühike pikkus")
             elif 140 <= pikkus < 170: print("sa oled keskmine pikkus")
             else: print("sa oled pikk pikkus")
     except: print("sissesta teie pikkus numbriga")
else: print("vale sugu")


# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.
# Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
# Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
# Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
print()
tooted=["piim","sai","leib","vorst"]
kogusumma=0
tsekk=""
for toit in tooted:
    valik=input(f"Kas tahate osta {toit}?").lower()
    if valik == "jah":
        toote_hind=round(random.uniform(0.5, 3), 2)
        print(f"{toit} hind on {toote_hind}€")
        try:
            kogus=int(input("Kui palju tooted sa tahab osta? "))
            lõpphind=round(toote_hind*kogus,2)
            print(f"lõpphind on {lõpphind}€")
            kogusumma=round(kogusumma+lõpphind,2)
            tsekk=tsekk + f"{toit} {kogus}tk  {lõpphind}€\n"
        except: print("Sa kirjutasid hind vale formaatis, lähme edasi")
    else: print(f"{toit} ei taha")
if kogusumma>0:
    print(tsekk)
    print(f"kõik tooted kogu maksavad {kogusumma}€")
else: print("ei ostnud midagi")
# Kasutaja sisestab nelinurga nelja külje pikkused. Programm teatab, kas tegemist saab olla ruuduga (kõik küljed on võrdsed).
# Kontrolli ka, et kõik pikkused on positiivsed.
# Koosta programmi kohta plokkskeem ja salvesta see PNG-pildina programmiga samasse kausta.
print()
try:
    kulg1=float(input("sissesta esimene kulg: "))
    kulg2=float(input("sissesta teine kulg: "))
    kulg3=float(input("sissesta kolmas kulg: "))
    kulg4=float(input("sissesta neljas kulg: "))
    if kulg1 < 0 or kulg2 < 0 or kulg3 < 0 or kulg4 < 0:
        print("ära kirjutada negatiivne arved")
    else:
        if kulg1 == kulg2  == kulg3 == kulg4:
            print("see on ruut")
        else: print("see ei ole ruut")
except: print("sissesta ")

# Kasutaja sisestab kaks arvu. Seejärel küsib programm, millist tehet ta soovib (+, -, *, /), ja kuvab tulemuse.
# Kui sisestatakse tundmatu tehtemärk, kuva veateade.
# Nulliga jagamise korral kuva arusaadav teade, mitte veateade Pythonist.
print()
try:
    arv1=float(input("sissesta esimene arv: "))
    arv2=float(input("sissesta teine arv: "))
    tehet=input("mida sa tahab teha?(+, -, *, /) ")
    if tehet == "+":
        vastus=arv1+arv2
    elif tehet == "-":
        vastus=arv1-arv2
    elif tehet == "*":
        vastus=arv1*arv2
    elif tehet == "/":
        vastus=arv1/arv2
    else: print("ei tea mida sa tahad teha")
    # vastus=eval("arv1, tehet, arv2")
    print(f"teie tegevus: {arv1} {tehet} {arv2} = {vastus}")
except: print("sisseta ainult numbrid")

# Kasutaja sisestab oma sünniaasta. Programm arvutab, mitu aastat ta sel aastal saab, ja ütleb, 
# kas tegemist on juubeliga (vanus jagub 10-ga). Kui ei ole, ütle, mitu aastat on järgmise juubelini.
# Vihje: jooksva aasta saad date.today().year abil, jäägi % abil.
# Plokkskeemi pole vaja.
print()
tana=date.today().year
try:
    sunniaasta=int(input("Sissesta oma sünniaasta: "))
    vanus=tana-sunniaasta
    juubeliga= (sunniaasta-tana) % 10
    if juubeliga == 0:
        print(f"teie on juubelin, sa oled {vanus} aastat vana")
    else: print(f"Sa oled {vanus} aastat vana, {juubeliga} aastat kuni juubeliga")
except: print("sisseta sünniaasta taisarvudega")

# # Kasutaja sisestab toote hinna. Kui hind on kuni 10 eurot, saab ta 10% allahindlust.
# # Üle 10 euro maksvad tooted saavad 20% allahindlust. Kuva toote lõplik hind kahe komakohaga.
# # Plokkskeemi pole vaja.
print()
try:
    hind=round(float(input("sissesta toote hind: ")),2)
    lõpphind=0
    if 10 > hind:
        lõpphind=round(hind*0.9,2)
    else:
        lõpphind=round(hind*0.8,2)
    print(f"Toote lõplik hind on {lõpphind}€")
except: print("palun sissesta hind numbriga")

# # Loo programm, mis kontrollib, kas kandideerija sobib meeskonda.
# # Meeskonda võetakse ainult 16–18-aastaseid mehi.
# # Küsi kõigepealt sugu.
# # Kui kandideerija on naissoost, siis vanust üldse ei küsita ja programm teatab kohe, et ta ei sobi.
# # Meessoost kandideerijalt küsi vanus ja kontrolli, kas see jääb vahemikku 16–18.
print()
print("kontrollime, et te sobite meeskonda")
sugu=input("Mis on teie sugu?(M/N): ").lower()
if sugu != "m":
    print("Te ei sobite")
else:
    try:    
        vanus=int(input("Kui vana te olete? "))
        if 16 <= vanus <= 18:
            print("Te sobite")
        else:
            print("Te ei sobite")
    except: print("sissesta ainult täisarv")

# On vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. 
# Programm küsib inimeste arvu ja ühe bussi kohtade arvu ning arvutab:
# mitu bussi on vaja, et kõik inimesed kohale saaksid;
# mitu inimest on viimases bussis, kui kõik eelmised bussid on täiesti täis.
# Kontrolli, et mõlemad sisestatud arvud on positiivsed täisarvud.
# Vihje: kasuta täisarvulist jagamist // ja jääki %. Mõtle, mis juhtub, kui inimesed mahuvad bussidesse täpselt ära.
print()
try:
    buskoht=int(input("kui palju kohad bussi? "))
    inimesed=int(input("Kui palju inimesed? "))

    if inimesed <= 0:
        print("sa ei pea kedagi transportima")
    else:
        if inimesed % buskoht > 0:
            print(f"Sa kasutab {inimesed//buskoht+1} bussi, viimases bussis on {inimesed % buskoht} inimesed")
        else:
            print(f"Sa kasutab {inimesed//buskoht} bussi, viimases bussis on {buskoht} inimesed")
except: print("sissesta ainult taisarv")

