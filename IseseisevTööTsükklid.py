from random import *

#while 1:
#    try:
#        mainnumber = int(input("Vali number 1-100:"))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if mainnumber<1 or mainnumber>100:
#    print("Vali õige number")
#else:
#    paaris = 0 
#    paaritu = 0 
#    for x in range(mainnumber):
#        print(int(x), end=" ")
#        if x % 2 == 0:
#             paaris += 1
#        else:
#             paaritu += 1
#        x = x // 10
#    print("Paaris numbrid:", paaris)
#    print("Paaritu numbrid:", paaritu)

#while 1:
#    try:
#        mainnumber = int(input("Vali number 1-100:"))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if mainnumber<1 or mainnumber>100:
#    print("Vali õige number")
#else:
#    paaris = 0 
#    paaritu = 0 
#    x = 0
#    while x!=mainnumber:    
#        print(int(x), end=" ")
#        if x % 2 == 0:
#             paaris += 1
#             x = x // 10
#             x +=1
#        else:
#             paaritu += 1
#             x = x // 10
#             x +=1

#    print("Paaris numbrid:", paaris)
#    print("Paaritu numbrid:", paaritu)





#oma ulesanne
#print("Tere tulemast parooli generatori!")
#while 1:
#    try:
#        answer = int(input("Mitu numbrid sa tahad sinul parooli? Vali number 1 - 10000:"))
#        break
#    except ValueError:
#        print()
#if answer<1 or answer>10000:
#    print("Vali number 1 - 10000")
#else:
#        for x in range(answer):
#            numbers = randint(0,10)
#            qwerty = choice(["q","w","e","r","t","y","a","s","d","f","g","h"])
#            random = choice ([qwerty,numbers])
#            print((random), end="")
#print("Head aega!")
#print ()

#print("Tere tulemast parooli generatori!")
#while 1:
#    try:
#        answer = int(input("Mitu numbrid sa tahad sinul parooli? Vali number 1 - 10000:"))
#        break
#    except ValueError:
#        print()
#if answer<1 or answer>10000:
#    print("Vali number 1 - 10000")
#else:
#        x=0
#        while x!=answer:
#            numbers = randint(0,10)
#            qwerty = choice(["q","w","e","r","t","y","a","s","d","f","g","h"])
#            random = choice ([qwerty,numbers])
#            x += 1
#            print((random), end="")
#print("Head aega!")
#print ()


#print("Tere tulemast parooli generatori!")
#while 1:
#    try:
#        answer = int(input("Mitu numbrid sa tahad sinul parooli? Vali number 1 - 10000:"))
#        break
#    except ValueError:
#        print()
#if answer<1 or answer>10000:
#    print("Vali number 1 - 10000")
#else:
#        x=0
#        while True:
#            if x!=answer:
#                numbers = randint(0,10)
#                qwerty = choice(["q","w","e","r","t","y","a","s","d","f","g","h"])
#                random = choice ([qwerty,numbers])
#                print((random), end="")
#                x +=1
#            else:
#                break      
#print("Head aega!")
#print ()




#Ülesanne 10
#x=1
#while x<=100:
#    if x%5==0:
#        print(x,end="")

#ülesanne 17
#try:
#    num_horiz=int(input("ruutude arv horisontaalselt: \n"))
#except:
#    print("Value Error")
#    num_horiz=randint(1,10000)
#try:
#    num_vert=int(input("ruutude arv vertikalselt: \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1,20)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print("0", end=" ")
#    print()