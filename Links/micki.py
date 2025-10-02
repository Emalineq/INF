# #uloha faktorial
# cislo=int(input("zadaj mi cislo: "))
# vysledok = 1
# for i in range(1,cislo+1):
#     vysledok= vysledok*i #vysledok *=1
#     # jano +=2 #jano = jano+2
#     # ema //=3 ema= ema //3 #celos=ciselne delenie 7/3=2
# print(vysledok)
# # import this


# # spocitaj od a po b
# a=int(input("zadaj a: "))
# b=int(input("zadaj b: "))
#
# vysledok=0
# for i in range (a,b+1):
#     vysledok+=i
# print(vysledok)


# # prvocislo ano nie
# z=int(input("zadaj mi cislo:"))
# delitele=0
# for cislo in range(2,z): #(2,int(z**0.5)+1):
#     if z % cislo == 0:
#         delitele+=1
# if delitele==0:
#
#         print("je to prvocislo")
# else:
#     print("ne je to prvocislo")

z=int(input("zadaj mi cislo:"))
sucet_cifier=0
while z!=0:
    cifra= z % 10
    sucet_cifier += cifra
    z=z//10 #oddrbe poslednu cislicu
print(sucet_cifier) #ucenie debug + f8


