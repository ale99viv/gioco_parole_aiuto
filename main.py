import os
import random


def yello_word(strY):

    new = open("txt/gialle.txt", "w+")
    with open("txt/black.txt", "r") as file:

        lines = file.read().split("\n")

        for line in lines:
            count = 0
            for l in strY:
                lettera = l[0]
                indd = l[1]

                try:
                    if line.index(lettera) == indd:
                        pass
                    elif line.index(lettera) != int(indd):
                        count += 1
                except:
                    pass

            if count == len(strY):
                with open("txt/gialle.txt", "a") as g:
                    g.write("{}\n".format(line))


def black_word(strB):
    
    new = open("txt/black.txt", "w+")
    with open("txt/valid.txt", "r") as file:

        lines = file.read().split("\n")

        for line in lines:
            count = 0
            for l in strB:
                lettera = l[0]


                if lettera not in line:
                    count += 1 
                elif lettera in line:
                    pass

            if count == len(strB):
                with open("txt/black.txt", "a") as g:
                    g.write("{}\n".format(line))


def green_word(strG):
    
    new = open("txt/green.txt", "w+")
    with open("txt/gialle.txt", "r") as file:

        lines = file.read().split("\n")

        for line in lines:
            count = 0
            for l in strG:
                lettera = l[0]
                indd = l[1]

                try:
                    if line.index(lettera) == int(indd):
                        count += 1
                    elif line.index(lettera) != int(indd):
                        pass
                except Exception as e:
                    pass

            if count == len(strG):
                with open("txt/green.txt", "a") as g:
                    g.write("{}\n".format(line))




with open("txt/valid.txt", "r") as c:
    lines = c.read().split("\n")
    wordC = lines[random.randint(0, len(lines)-1)]

    for i in range(10):
        print(lines[random.randint(0, len(lines)-1)])




blackL = []
greenL = []
yellowL = []


while True:

    print("Lettere nere:\n", blackL)
    black = "s"
    while black != "0":
        black = input("Inserire lettere nere: ")
        if black != "0":
            blackL.append(black)

    black_word(blackL)

    yellow = "s"

    print("Lettere gialle:\n", yellowL)
    while yellow != "0":
        yellow = input("Inserire lettere gialle con index(es: a5), 0 to finish: ")
        if yellow != "0":
            yellowL.append(yellow)

    yello_word(yellowL)

    print("Lettere verdi:\n", greenL)
    green = "s"
    while green != "0":
        green = input("Inserire lettere verdi con index(es.): ")
        if green != "0":
            greenL.append(green)

    green_word(greenL)

    req = input("Cosa vuoi visualizzare random([b] [y] [g]): ")

    if req == "b":
        a = open("txt/black.txt", "r")
        lines = a.read().split("\n")
        
        for i in range(10):
            try:
                wordC = lines[random.randint(0, len(lines)-1)]
                print(wordC)
            except:
                pass
        a.close()

    if req == "g":
        a = open("txt/green.txt", "r")
        lines = a.read().split("\n")
        
        for i in range(10):
            try:
                wordC = lines[random.randint(0, len(lines)-1)]
                print(wordC)
            except:
                pass
        a.close()

    if req == "y":
        a = open("txt/gialle.txt", "r")
        lines = a.read().split("\n")
        
        for i in range(10):
            try:
                wordC = lines[random.randint(0, len(lines)-1)]
                print(wordC)
            except Exception as e:
                pass
        a.close()
