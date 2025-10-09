cislo=int(input("zadaj cislo:"))
vysledok=0
moc_des=1
while cislo!=0:
    zvysok = cislo%2
    vysledok += zvysok*moc_des
    moc_des *= 10
    cislo //=2
#     cislo= mocnina//2
print(vysledok)
