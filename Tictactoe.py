
#funktion################
def brett(felder):
    print("a",felder["a1"],"|",felder["a2"],"|",felder["a3"])
    print("b",felder["b1"],"|",felder["b2"],"|",felder["b3"])
    print("c",felder["c1"],"|",felder["c2"],"|",felder["c3"])
    print("  1   2   3")
#main#############
while True:
    #variablen######
    felder = {
        "a1": " ",
        "a2": " ",
        "a3": " ",
        "b1": " ",
        "b2": " ",
        "b3": " ",
        "c1": " ",
        "c2": " ",
        "c3": " "
    }
    player1icon = "X"
    player2icon = "O"
    player1icontest = "X"
    player2icontest = "O"
    killer = False
    unentscieden = 0
    koordinaten = ""
    player = True
    win = 0
    nochmalfrage = ""
    if killer == True:
        print("kill programm...")
        break
    brett(felder)
    print("Player one choose your icon (one token!)")
    player1icontest = input(">")
    if len(player1icontest) == 1:
        player1icon = player1icontest
        while True:
            print("Player two choose your icon (one token!)")
            player2icontest = input(">")
            if len(player2icontest) == 1:
                if player2icontest == player1icon:
                    print("This token has already the other player")
                else:
                    player2icon = player2icontest
                    break
            else:
                print("ONE TOKEN!!!")
        while unentscieden < 9:
            brett(felder)
            if unentscieden % 2 == 0:
                print("Player one: choose your field (ex: a1)")
                player = True
            else:
                print("Player two: choose your field (ex: a1)")
                player = False
            koordinaten = input(">")
            if koordinaten in felder:
                if felder[koordinaten] == " ":
                    if player == True:
                        felder[koordinaten] = player1icon
                    else:
                        felder[koordinaten] = player2icon
                    unentscieden = unentscieden + 1
                else:
                    print("Feld ist belegt")
            elif koordinaten == "kill":
                killer = True
                break
            else:
                print("diese koordinaten existieren nicht")
            if felder["a1"] == felder["a2"] == felder["a3"]:
                if felder["a1"] == player1icon:
                    win = 1
                    break
                elif felder["a1"] == player2icon:
                    win = 2
                    break
            if felder["b1"] == felder["b2"] == felder["b3"]:
                if felder["b1"] == player1icon:
                    win = 1
                    break
                elif felder["b1"] == player2icon:
                    win = 2
                    break
            if felder["c1"] == felder["c2"] == felder["c3"]:
                if felder["c1"] == player1icon:
                    win = 1
                    break
                elif felder["c1"] == player2icon:
                    win = 2
                    break
            if felder["a1"] == felder["b1"] == felder["c1"]:
                if felder["a1"] == player1icon:
                    win = 1
                    break
                elif felder["a1"] == player2icon:
                    win = 2
                    break
            if felder["a2"] == felder["b2"] == felder["c2"]:
                if felder["a2"] == player1icon:
                    win = 1
                    break
                elif felder["a2"] == player2icon:
                    win = 2
                    break
            if felder["a3"] == felder["b3"] == felder["c3"]:
                if felder["a3"] == player1icon:
                    win = 1
                    break
                elif felder["a3"] == player2icon:
                    win = 2
                    break
            if felder["a1"] == felder["b2"] == felder["c3"]:
                if felder["a1"] == player1icon:
                    win = 1
                    break
                elif felder["a1"] == player2icon:
                    win = 2
                    break
            if felder["c1"] == felder["b2"] == felder["a3"]:
                if felder["c1"] == player1icon:
                    win = 1
                    break
                elif felder["c1"] == player2icon:
                    win = 2
                    break
        if win == 1:
            brett(felder)
            print("Player one winns!!!")
        elif win == 2:
            brett(felder)
            print("Player two winns!!!")
        else:
            print("draw!")
    else:
        print("ONE TOKEN!!!")
    
#again############
    nochmalfrage = input("Play again? Y/n >")
    if nochmalfrage == "Y":
        print("")                                 
        print("")
    elif nochmalfrage == "n":
        break
    else:
        print("invailed input")
print("Programm ended")