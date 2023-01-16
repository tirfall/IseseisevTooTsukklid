from random import *
from string import *


#Ulesanne 8

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
#    for x in range(1,mainnumber+1):
#        print(int(x), end=" ")
#        if x % 2 == 0:
#             paaris += 1
#        else:
#             paaritu += 1
#        x = x // 10
#    print("Paaris numbrid:", paaris)
#    print("Paaritu numbrid:", paaritu)

#while True:
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
#    while x != mainnumber:
#        x = x + 1
#        print(int(x), end=" ")
#        if x % 2 == 0:
#             paaris += 1
#        else:
#             paaritu += 1
        
        
#print("Paaris numbrid:", paaris)
#print("Paaritu numbrid:", paaritu)
                   
        


#0 ulesanne


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

#ulesanne number 16
#ans = random.randint(1, 10)
#while True:
#    g = input ("Mis numbri ma arvasin? (1-10, mängu lõpetamiseks kirjutage *lõpp*) \n")
#    if g.lower() == "lõpp":
#        print("mäng on läbi!")
#        breakS
#    if not g.isnumeric():
#        print("Vale andmetüüp")
#        continue
#    if g == ans:
#        print("Õige!")
#        break
#    if g>10 or g<1:
#        print ("Vahemik on vale!")
#        continue
#    elif g !=ans:
#        print("Vale! Proovi veel korra!")
#        continue

#Ulesanne 3
#try:
#    f = int(input("Mitu ülesandeid sa tahad?"))
#    for d in range (0,f,1):
#        print(f"ülesanne{g}: ")
#        a = randint (1,50)
#        b = randint(1,50)
#        c = a + b
#        for i in range (o,5,1):
#            answer = int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print("See on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        g=g+1
#        print(f"Õige on {c} ")
#except:
#    print("See ei ole õige")


#Ulesanne 13
#print("arv", " ruut", " kuup")
#for i in range(1,11):
#    print(f" {i}  {i ** 2}  {i ** 3}")
#print("teine variant")

#Ulesanne 
#print("Guess letter - (From Aa to Zz)")
#letter = random.choice(string.ascii_letters)

#while True:
#    answ = str(input("Teie oletus: "))
#    if letter == answ:
#        print("Tubli!")
#        break
#    else: 
#        print("Proovi uuesti")

#Ulesanne 6
#print("Ülesanne 6 1")
#for i in range(0,5):
#    print("*"*5)
#for i in range(0,10):
#    print("*"*i)
#for i in range(0,10):
#    print("*"*(10-i)