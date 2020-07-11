def firstband5(f5):
    if f5 == "BLACK":
        return 0
    elif f5 == "BROWN":
        return 100
    elif f5 == "RED":
        return 200
    elif f5 == "ORANGE":
        return 300
    elif f5 == "YELLOW":
        return 400
    elif f5 == "GREEN":
        return 500
    elif f5 == "BLUE":
        return 600
    elif f5 == "VIOLET":
        return 700
    elif f5 == "GREY":
        return 800
    elif f5 == "WHITE":
        return 900
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()


def secondband5(s5):
    if s5 == "BLACK":
        return 0
    elif s5 == "BROWN":
        return 10
    elif s5 == "RED":
        return 20
    elif s5 == "ORANGE":
        return 30
    elif s5 == "YELLOW":
        return 40
    elif s5 == "GREEN":
        return 50
    elif s5 == "BLUE":
        return 60
    elif s5 == "VIOLET":
        return 70
    elif s5 == "GREY":
        return 80
    elif s5 == "WHITE":
        return 90
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()
def thirdband5(th5):
    if th5 == "BLACK":
        return 0
    elif th5 == "BROWN":
        return 1
    elif th5 == "RED":
        return 2
    elif th5 == "ORANGE":
        return 3
    elif th5 == "YELLOW":
        return 4
    elif th5 == "GREEN":
        return 5
    elif th5 == "BLUE":
        return 6
    elif th5 == "VIOLET":
        return 7
    elif th5 == "GREY":
        return 8
    elif th5 == "WHITE":
        return 9
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()

def multiplier5(m5):
    if m5 == "BLACK":
        return 1
    elif m5== "BROWN":
        return 10
    elif m5 == "RED":
        return 100
    elif m5 == "ORANGE":
        return 1000
    elif m5 == "YELLOW":
        return 10*1000
    elif m5 == "GREEN":
        return 100*1000
    elif m5 == "BLUE":
        return 1000*1000
    elif m5 == "VIOLET":
        return 10*1000*1000
    elif m5 == "GREY":
        return 100*1000*1000
    elif m5 == "WHITE":
        return 1000*1000*1000
    elif m5 == "GOLD":
        return 0.1
    elif m5 == "SILVER":
        return 0.01
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()

def tolerance5(t5):
    if t5 == "BROWN":
        print("+/- 1%")
    elif t5 == "RED":
        print("+/- 2%")
    elif t5 == "GREEN":
        print("+/- 0.5%")
    elif t5 == "BLUE":
        print("+/- 0.25%")
    elif t5 == "VIOLET":
        print("+/- 0.10%")
    elif t5 == "GREY":
        print("+/- 0.05%")
    elif t5 == "GOLD":
        print("+/- 5%")
    elif t5 == "SILVER":
        print("+/- 10%")
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()


def band5():
    a5 = input("1st Band of Color : ")
    w5 = firstband5(a5)
    b5 = input("2nd Band of Color : ")
    x5 = secondband5(b5)
    a45 = input("3rd Band of Color : ")
    w45 = thirdband5(a45)
    c5 = input("MULTIPLIER(4th Band) : ")
    y5 = multiplier5(c5)
    sum5 = w5 + x5 + w45
    return  sum5 * y5

def firstband(f):
    if f == "BLACK":
        return 0
    elif f == "BROWN":
        return 10
    elif f == "RED":
        return 20
    elif f == "ORANGE":
        return 30
    elif f == "YELLOW":
        return 40
    elif f == "GREEN":
        return 50
    elif f == "BLUE":
        return 60
    elif f == "VIOLET":
        return 70
    elif f == "GREY":
        return 80
    elif f == "WHITE":
        return 90
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()


def secondband(s):
    if s == "BLACK":
        return 0
    elif s == "BROWN":
        return 1
    elif s == "RED":
        return 2
    elif s == "ORANGE":
        return 3
    elif s == "YELLOW":
        return 4
    elif s == "GREEN":
        return 5
    elif s == "BLUE":
        return 6
    elif s == "VIOLET":
        return 7
    elif s == "GREY":
        return 8
    elif s == "WHITE":
        return 9
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()

def multiplier(m):
    if m == "BLACK":
        return 1
    elif m == "BROWN":
        return 10
    elif m == "RED":
        return 100
    elif m == "ORANGE":
        return 1000
    elif m == "YELLOW":
        return 10*1000
    elif m == "GREEN":
        return 100*1000
    elif m == "BLUE":
        return 1000*1000
    elif m == "VIOLET":
        return 10*1000*1000
    elif m == "GREY":
        return 100*1000*1000
    elif m == "WHITE":
        return 1000*1000*1000
    elif m == "GOLD":
        return 0.1
    elif m == "SILVER":
        return 0.01
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()

def tolerance(t):
    if t == "BROWN":
        print("+/- 1%")
    elif t == "RED":
        print("+/- 2%")
    elif t == "GREEN":
        print("+/- 0.5%")
    elif t == "BLUE":
        print("+/- 0.25%")
    elif t == "VIOLET":
        print("+/- 0.10%")
    elif t == "GREY":
        print("+/- 0.05%")
    elif t == "GOLD":
        print("+/- 5%")
    elif t == "SILVER":
        print("+/- 10%")
    else:
        print("Wrong Color Input. Type in BLOCK LETTER.")
        start()


def band4():
    a4= input("1st Band of Color : ")
    w4= firstband(a4)
    b4= input("2nd Band of Color : ")
    x4= secondband(b4)
    c4 = input("MULTIPLIER(3rd Band) : ")
    y4= multiplier(c4)
    sum = w4 + x4
    return  sum * y4




def resband4(rs4):
    if 0 < rs4 < 1000:
        print("", rs4, "ohm")
    elif 1000<= rs4 <1000*1000:
        print("", rs4 / 1000, "Kohm")
    elif 1000*1000 <= rs4 < 1000*1000*1000:
        print("", rs4 / (1000 * 1000), "Mohm")
    elif rs4 >= 1000 * 1000 * 1000:
        print("", rs4 / (1000 * 1000 * 1000), "Gohm")
    else:
        print("", rs4, "ohm")

def start():
    print("            _________________________         ")
    print("             Choose Band                      ")
    print("             1.4 Band                      ")
    print("             2.5 Band                      ")
    inp = input("")
    print("Enter Color Names in BLOCK LETTER=>")
    if inp== "1":
        s4 = band4()
        d4 = input("Tolerance(4th Band) : ")
        print("Tolerance: ")
        t4= tolerance(d4)
        print("Resistor : ")
        s4a = resband4(s4)
        
    elif inp== "2":
        ss5 = band5()
        d45 = input("Tolerance(4th Band) : ")
        print("Tolerance: ")
        t45 = tolerance5(d45)
        print("Resistor : ")
        s5a = resband4(ss5)

    else:
        print("WRONG INPUT. Press '1' for 4 Band Resistance or '2' for 5 Band Resistance")


print("             Resistance Color Code            ")
print("______________________________________________\n")
print("Colour Bands=>")
print("Color          1st Band          2nd Band          3rd Band          Multiplier          Tolerance           ")
print("-------------------------------------------------------------------------------------------------------------")
print("Black             0                  0                0                 1   Ohm                              ")
print("Brown             1                  1                1                 10  Ohm             +/- 1%           ")
print("Red               2                  2                2                 100 Ohm             +/- 2%           ")
print("Orange            3                  3                3                  1  K-Ohm                            ")
print("Yellow            4                  4                4                 10  K-Ohm                            ")
print("Green             5                  5                5                 100 K-Ohm           +/- 0.5%         ")
print("Blue              6                  6                6                  1  M-Ohm           +/- 0.25%        ")
print("Violet            7                  7                7                 10  M-Ohm           +/- 0.10%        ")
print("Grey              8                  8                8                 100 M-Ohm           +/- 0.05%        ")
print("White             9                  9                9                  1  G-Ohm           +/- 0.5%         ")
print("Gold                                                                    0.1  Ohm            +/- 5%           ")
print("Silver                                                                 0.01 G-Ohm           +/- 5%           ")
    
start()
i=0;
while i<1:
    print("______________________________________________")
    print("1.Calculate Again\n2.Close Program")
    end = input("press 1 for main menu or 2 for closing application: ")
    if end == "1":
        i=0
        start()
    elif end == "2":
        i=2
        print("thankyou")
    else:
        print("Wrong Input,try again")
print("Resistance Color Code Calculator developed by Faisal Farhan")







