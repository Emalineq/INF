# # uloha 1
# for i in range (1,11):
#     print(i, end=", ")
#     # end pridavam aby som tam dala nie 4 5 iny riadok ale 4, 5, ten ist7 riadok

# # uloha 2
# # a)
# n=int(input("zadaj n:"))
# for i in range(1,n+1):
#     print(i)
# # b)
# n=int(input("zadaj n:"))
# for i in range(1,n+1):
#     print(i,end=", ")

# # uloha 3
# n=int(input("zadaj n:"))
# for i in range(5,n+1,2):
#     print(i)

# # uloha 4
# n=int(input("zadaj n:"))
# for i in range(1,n+1):
#     print(i,i*i)

# # uloha 5
# a=int(input("<odkial>:"))
# b=int(input("<pokial>:"))
# for i in range (a,b+1):
#     print(1,round(i**0.5,2))
# # 30najprv co netreba zaokruhlit,round(co treba, na kolko miest)

# # uloha 6
# for x in range (1,21):
#    if x !=3:
#         y = (x ** 2 - 1) / (x - 3)
#         print("x=",x,"y=",round(y,1))
#    else:
#        print("x=",x,"funkcia nie je definovana")
# # 35 podmienka pre x aby nebolo 0 a,36/ nie //lebo to len pri celocislovom deleni 37 oddelit "text" od cisel

# # uloha 7
# n=int(input("zadaj n:"))
# for i in range(1,n+1):
#     if i % 3==0:
#         print(i,end=",")

# # uloha 8
# for i in range(2,21,2):
#     print(i)

# # uloha 9
# z=int(input("zaciatok:"))
# k=int(input("koniec:"))
# if z!= 0:
#     for i in range(z,k,):
#         print(i)

# # uloha 10
# n=int(input("zadaj n:"))
# for i in range(n,0,-1):
#     print(i)

# # uloha 11
# n =int(input('zadaj n:'))
# for i in range(0,n+1):
#     if i % 4 ==0 and i % 7 ==0:
#         print(i)

# # uloha 12
# n=int(input("zadaj n:"))
# vysledok=0
# for i in range(1,n+1):
#     vysledok+=i
# print(vysledok)

# # uloha 13
# n=int(input("zadaj n:"))
# vysledok=0
# for i in range(2,n+1,2):
#     vysledok+=i
# print(vysledok)
#
# # uloha 14
# a=int(input("<odkial>:"))
# b=int(input("<pokial>:"))
# vysledok=0
# for i in range(a,b+1):
#     if i%8==0:
#        vysledok+=1
# print("cisla co delitelne dvomi su:", vysledok)






