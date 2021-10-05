print("welcome")
input1 = input("continuati? da / nu: ")
w = 0
if w : 
    file = open("istoric.txt", "w")
while input1 == "da":
    try:
        nr1 = float(input("primul nr: "))
        operatie = input("operatie: (plus, minus, inmultit, impartit, ridicare, rest, radical, procent, baza): ")
        if operatie == 'plus':
            try:
                nr2 = (float(input("adunat cu: ")))
                rez = float(nr1 + nr2)
                print("rezultat = ", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred plus")
        elif operatie == 'minus':
            try:
                nr2 = (float(input("minus nr: ")))
                rez = float(nr1 - nr2)
                print("rezultat =", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred minus")
        elif operatie == 'inmultit':
            try:
                nr2 = (float(input("inmultit cu: ")))
                rez = float(nr1 * nr2)
                print("rezultat =", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred inmultit")
        elif operatie == 'impartit':
            try:
                nr2 = (float(input("impartit la: ")))
                rez = nr1 / nr2
                print("rezultat =", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except ZeroDivisionError:
                print('impartire la 0, reincercati')
            except :
                print("Error occurred impartit")
        elif operatie == 'ridicare':
            try:
                nr2 = (float(input("la puterea: ")))
                rez = float(nr1 ** nr2)
                print("rezultat =", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred ridicare")
        elif operatie == 'rest':
            try:
                nr2 = (float(input("numarul 2: ")))
                rez = nr1 // nr2
                rest = nr1%nr2
                print("rezultat =", rez, "rest:", rest)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + 'rest:' + str(rest) + '\n')
                input1 = input("continuati? da / nu: ")
            except ZeroDivisionError:
                print('impartire la 0, reincercati')
            except :
                print("Error occurred rest")
        elif operatie == 'radical':
            try:
                nr2 = (float(input("de ordinul: ")))
                rez = nr1**(1/nr2)
                print("rezultat =", rez)
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '\n')
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred radical")
        elif operatie == 'procent':
            try:
                nr2 = (float(input("procent din: ")))
                rez = nr1*100/nr2
                print("rezultat =", rez, "%")
                if w :
                    file.write(str(nr1) + operatie + str(nr2) + "=" + str(rez) + '%' + '\n')                
                input1 = input("continuati? da / nu: ")
            except :
                print("Error occurred procent")        
        elif operatie == 'baza': #trebuie trecut prin baza 10 inainte de conversia in alta baza 
            try:
                baza = (int(input("baza in care e scris nr1: ")))
                nr2 = (int(input("baza in care se transforma: ")))
                if (baza < 10 and nr2 < baza) or (baza == 2 and nr2 != 10):                    
                    print('trebuie trecut prin baza 10 inainte de conversia in alta baza ')
                    input1 = input("continuati? da / nu: ")
                else :
                    rez = 0
                    buff = nr1
                    i = 0
                    while buff > 0 :
                        rez = rez + (buff%nr2)*(baza**i)
                        buff = buff // nr2
                        i = i+1
                    print("rezultat =", rez) 
                    if w :
                        file.write(str(nr1) + operatie + str(baza) + "in baza" + str(nr2) + "=" + str(rez) + '\n')  
                    input1 = input("continuati? da / nu: ")                              
            except :
                print("Error occurred baza") 
    except :
        print("Error occurred main")  
        input1 = input("continuati? da / nu: ")
if w :
    file.close() 
