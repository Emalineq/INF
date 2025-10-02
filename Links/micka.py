
import math
a= int(input("zadaj stranu a:"))
b= int(input("zadaj stranu b:"))
c= int(input("zadaj stranu c:"))

# trojuholníkova nerovnost
if a + b > c and a + c > b and b + c > a:
    print("Tieto strany, mozu tvorit trojuholnik.")

    # Obvod
    obvod = a + b + c
    print("obvod:", obvod)

    # Obsah (Heronov vzorec)
    s = obvod / 2
    obsah = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("obsah:", obsah)

    # Výšky
    if obsah > 0:  # aby sa nedelilo nulou
        va = 2 * obsah / a
        vb = 2 * obsah / b
        vc = 2 * obsah / c
        print("vyska na stranu a:", va)
        print("vyska na stranu b:", vb)
        print("vyska na stranu c:", vc)

    # Uhly
    alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
    beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
    gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))

    print("uhol alpha:", round(alpha, 2))
    print("uhol beta:", round(beta, 2))
    print("uhol gamma:", round(gamma, 2))
    # zaukruhlenie na 2 desatinne: round(daco,2)
    # Typ trojuholníka
    if a == b == c:
        print("trojuholnik je rovnostranny.")
    elif a == b or b == c or a == c:
        print("trojuholnik je rovnoramenny.")
    elif (round(alpha) == 90 or round(beta) == 90 or round(gamma) == 90):
        print("trojuholnik je pravouhly.")
    else:
        print("trojuholnik je roznostranni.")
    # round je zaokruhlenie

    # taznice
    ta = 0.5 * math.sqrt(2*b**2 + 2*c**2 - a**2)
    tb = 0.5 * math.sqrt(2*a**2 + 2*c**2 - b**2)
    tc = 0.5 * math.sqrt(2*a**2 + 2*b**2 - c**2)

    print("taznica na stranu a:", ta)
    print("taznica na stranu b:", tb)
    print("taznica na stranu c:", tc)

else:
    print("Tieto strany nemozu tvorit trojuholnik.")

if a < b and a < c:
    if b < c:
        print(a, b, c)
    else:
        print(a, c, b)

elif b < a and b < c:
    if a < c:
        print(b, a, c)
    else:
        print(b, c, a)

else:
    if a < b:
        print(c, a, b)
    else:
        print(c, b, a)

#nacitaj 3 cisla a zorad mi ich od najveacsieho po najmensie

