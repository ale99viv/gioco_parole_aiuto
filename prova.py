


def green_word(strG):
    
    with open("txt/prova.txt", "r") as file:

        lines = file.read().split("\n")

        for line in lines:
            count = 0
            line = line.strip()

            for l in strG:
                lettera = l[0]
                indd = l[1]
                
                try:
                    inexF = 0
                    for i in line:
                        if (i == lettera) and (int(indd) == inexF):
                            print(count)
                        else:
                            pass
                        inexF += 1

                except Exception as e:
                    pass

            if count == len(strG):
                print(line)


a= ["m0", "i3", "a4"]
green_word(a)