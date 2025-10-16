# # 1. ciferny sucet
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# sucet = 0
# while a > 0:
#     sucet += a % 10
#     a //= 10
# print("ciferny sucet je:", sucet)
#
# # 2. pocet parnych cifier
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# pocet = 0
# while a > 0:
#     cifra = a % 10
#     if cifra % 2 == 0:
#         pocet += 1
#     a //= 10
# print("pocet parnych cifier:", pocet)
#
# # 3. pocet cifier
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# if a == 0:
#     pocet = 1
# else:
#     pocet = 0
#     while a > 0:
#         pocet += 1
#         a //= 10
# print("pocet cifier:", pocet)
#
# # 4. vypis cislo odzadu
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# odzadu = 0
# while a > 0:
#     odzadu = odzadu * 10 + a % 10
#     a //= 10
# print("cislo odzadu:", odzadu)
#
# # 5. rozdelenie cisla na parne a neparne miesta (odzadu)
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# prve = 0
# druhe = 0
# moc1 = 1
# moc2 = 1
# i = 1
# while a > 0:
#     cifra = a % 10
#     if i % 2 == 0:
#         prve += cifra * moc1
#         moc1 *= 10
#     else:
#         druhe += cifra * moc2
#         moc2 *= 10
#     a //= 10
#     i += 1
# print("prve cislo odzadu:", prve)
# print("druhe cislo odzadu:", druhe)
#
# # 5a. otocenie aby boli v spravnom poradi
# x = prve
# spravne1 = 0
# while x > 0:
#     spravne1 = spravne1 * 10 + x % 10
#     x //= 10
#
# x = druhe
# spravne2 = 0
# while x > 0:
#     spravne2 = spravne2 * 10 + x % 10
#     x //= 10
#
# print("prve cislo spravne:", spravne1)
# print("druhe cislo spravne:", spravne2)
#
# # 6. stredna cifra alebo priemer dvoch strednych
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# b = a
# pocet = 0
# while b > 0:
#     pocet += 1
#     b //= 10
#
# if pocet % 2 == 1:
#     for i in range(pocet // 2):
#         a //= 10
#     print("stredna cifra je:", a % 10)
# else:
#     for i in range(pocet // 2 - 1):
#         a //= 10
#     c1 = a % 10
#     a //= 10
#     c2 = a % 10
#     priemer = (c1 + c2) / 2
#     print("priemer dvoch strednych cifier:", priemer)
#
# # 9. zisti ci je cislo symetricke
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# b = a
# odzadu = 0
# while b > 0:
#     odzadu = odzadu * 10 + b % 10
#     b //= 10
# if odzadu == a:
#     print("cislo je symetricke")
# else:
#     print("cislo nie je symetricke")
#
# # 12. vsetci delitelia
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# print("delitelia cisla:", end=" ")
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")
# print()
#
# # 13. collatzova postupnost
# a = int(input("zadaj cislo: "))
# if a < 0:
#     a = -a
# print("collatzova postupnost:", end=" ")
# while a != 1:
#     print(a, end=" ")
#     if a % 2 == 0:
#         a //= 2
#     else:
#         a = 3 * a + 1
# print(1)
