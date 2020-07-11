def theory(m):
    if m >= 80:
        return 4 * 3
    elif 75 <= m <= 79:
        return 3.75 * 3
    elif 70 <= m <= 74:
        return 3.50 * 3
    elif 65 <= m <= 69:
        return 3.25 * 3
    elif 60 <= m <= 64:
        return 3.00 * 3
    elif 55 <= m <= 59:
        return 2.75 * 3
    elif 50 <= m <= 54:
        return 2.50 * 3
    elif 45 <= m <= 49:
        return 2.25 * 3
    elif 40 <= m <= 44:
        return 2.00 * 3
    elif m < 40:
        return 0 * 3
    else:
        print("Wrong Input. Enter marks in number")


def lab(n):
    if n >= 80:
        return 4 * 1.5
    elif 75 <= n <= 79:
        return 3.75 * 1.5
    elif 70 <= n <= 74:
        return 3.50 * 1.5
    elif 65 <= n <= 69:
        return 3.25 * 1.5
    elif 60 <= n <= 64:
        return 3.00 * 1.5
    elif 55 <= n <= 59:
        return 2.75 * 1.5
    elif 50 <= n <= 54:
        return 2.50 * 1.5
    elif 45 <= n <= 49:
        return 2.25 * 1.5
    elif 40 <= n <= 44:
        return 2.00 * 1.5
    elif n < 40:
        return 0 * 1.5
    else:
        print("Wrong Input. Enter marks in number")


def thesis(t):
    if t == "A+" or "a+":
        return 4 * 6
    elif t == "A" or "a":
        return 3.75 * 6
    elif t == "A-" or "a-":
        return 3.50 * 6
    elif t == "B+" or "b+":
        return 3.25 * 6
    elif t == "B" or "b":
        return 3.00 * 6
    elif t == "B-" or "b-":
        return 2.75 * 6
    elif t == "C+" or "c+":
        return 2.50 * 6
    elif t == "C" or "c":
        return 2.25 * 6
    elif t == "D" or "d":
        return 2.00 * 6
    elif t == "F" or "f":
        return 0 * 6
    else:
        print("Wrong Input. Type Grade(A+,A,A-,B+,B,B-,C+,C,D,F")


def oneone():
    print("Enter Your Final Exam Marks : ")

    a11 = float(input("EEE 1101 Electrical Circuits 1 : "))
    dc11 = theory(a11)
    b11 = float(input("ME 1101 Mechanical Engineering Fundamentals : "))
    me11 = theory(b11)
    c11 = float(input("PHY 1105 Physics 1 : "))
    ph11 = theory(c11)
    d11 = float(input("MATH 1103 Mathematics 1 : "))
    mh11 = theory(d11)
    e11 = float(input("CHEM 1107 Chemistry : "))
    cm11 = theory(e11)

    th11 = dc11 + me11 + ph11 + mh11 + cm11

    w11 = float(input("EEE 1102 Electrical Circuits 1 LAB : "))
    dcl11 = lab(w11)
    x11 = float(input("PHY 1106 Physics 1 LAB : "))
    phl11 = lab(x11)
    y11 = float(input("CHEM 1108 Chemistry LAB : "))
    cml11 = lab(y11)
    z11 = float(input("ME 1102 Mechanical Engineering Fundamentals LAB : "))
    mel11 = lab(z11)
    lb11 = dcl11 + phl11 + cml11 + mel11

    m11 = th11 + lb11
    gpa(m11, 21)


def onetwo():
    print("Enter Your Final Exam Marks : ")

    a12 = float(input("EEE 1201 Electrical Circuits 2 : "))
    dc12 = theory(a12)
    b12 = float(input("CE 1201 Mechanics of Materials : "))
    me12 = theory(b12)
    c12 = float(input("PHY 1205 Physics 2 : "))
    ph12 = theory(c12)
    d12 = float(input("MATH 1203 Mathematics II : "))
    mh12 = theory(d12)
    e12 = float(input("MATH 1213 Mathematics III : "))
    cm12 = theory(e12)

    th12 = dc12 + me12 + ph12 + mh12 + cm12

    w12 = float(input("EEE 1202 Electrical Circuits 2 LAB : "))
    dcl12 = lab(w12)
    x12 = float(input("EEE 1210 Electrical Circuit Simulation LAB : "))
    phl12 = lab(x12)
    y12 = float(input("CE 1202 Engineering Drawing : "))
    cml12 = lab(y12)

    lb12 = dcl12 + phl12 + cml12

    m12 = th12 + lb12
    gpa(m12, 19.5)


def twoone():
    print("Enter Your Final Exam Marks : ")

    a21 = float(input("EEE 2103 Electronics I : "))
    dc21 = theory(a21)
    b21 = float(input("EEE 2105 Energy Conversion I : "))
    me21 = theory(b21)
    c21 = float(input("EEE 2109 Programming Language : "))
    ph21 = theory(c21)
    d21 = float(input("MATH 2103 Mathematics IV : "))
    mh21 = theory(d21)
    e21 = float(input("HUM 2109 English & Sociology : "))
    cm21 = theory(e21)

    th21 = dc21 + me21 + ph21 + mh21 + cm21

    w21 = float(input("EEE 2104 Electronics I LAB : "))
    dcl21 = lab(w21)
    x21 = float(input("EEE 2106 Energy Conversion I LAB : "))
    phl21 = lab(x21)
    y21 = float(input("EEE 2110 Programming Language LAB : "))
    cml21 = lab(y21)
    z21 = float(input("HUM 2110 Developing English Skills LAB : "))
    mel21 = lab(z21)
    lb21 = dcl21 + phl21 + cml21 + mel21

    m21 = th21 + lb21
    gpa(m21, 21)


def twotwo():
    print("Enter Your Final Exam Marks : ")

    a22 = float(input("EEE 2203 Electronics II : "))
    dc22 = theory(a22)
    b22 = float(input("EEE 2205 Energy Conversion II : "))
    me22 = theory(b22)
    c22 = float(input("EEE 2211 Measurement & Instrumentation : "))
    ph22 = theory(c22)
    d22 = float(input("MATH 2203 Mathematics V : "))
    mh22 = theory(d22)
    e22 = float(input("HUM 2209 Accounting & Economics : "))
    cm22 = theory(e22)

    th22 = dc22 + me22 + ph22 + mh22 + cm22

    w22 = float(input("EEE 2204 Electronics II LAB : "))
    dcl22 = lab(w22)
    x22 = float(input("EEE 2206 Energy Conversion II LAB : "))
    phl22 = lab(x22)
    y22 = float(input("EEE 2210 Electronic Circuit Simulation Lab : "))
    cml22 = lab(y22)
    z22 = float(input("EEE 2212 Measurement & Instrumentation LAB : "))
    mel22 = lab(z22)
    lb22 = dcl22 + phl22 + cml22 + mel22

    m22 = th22 + lb22
    gpa(m22, 21)


def threeone():
    print("Enter Your Final Exam Marks : ")

    a31 = float(input("EEE 3103 Digital Electronics I : "))
    dc31 = theory(a31)
    b31 = float(input("EEE 3107 Signals & Linear Systems : "))
    me31 = theory(b31)
    c31 = float(input("EEE 3113 Electrical Properties of Materials : "))
    ph31 = theory(c31)
    d31 = float(input("EEE 3117 Electromagnetics : "))
    mh31 = theory(d31)
    e31 = float(input("HUM 3109 Industrial Management : "))
    cm31 = theory(e31)

    th31 = dc31 + me31 + ph31 + mh31 + cm31

    w31 = float(input("EEE 3104 Digital Electronics I LAB : "))
    dcl31 = lab(w31)
    x31 = float(input("EEE 3110 Numerical Technique LAB : "))
    phl31 = lab(x31)
    y31 = float(input("EEE 3100 Electrical Service Design : "))
    cml31 = lab(y31)

    lb31 = dcl31 + phl31 + cml31

    m31 = th31 + lb31
    gpa(m31, 19.5)


def threetwo():
    print("Enter Your Final Exam Marks : ")

    a32 = float(input("EEE 3203 Solid State Devices : "))
    dc32 = theory(a32)
    b32 = float(input("EEE 3205 Power System I : "))
    me32 = theory(b32)
    c32 = float(input("EEE 3207 Communication Theory : "))
    ph32 = theory(c32)
    d32 = float(input("EEE 3209 Microprocessor,Interfacing & System Design : "))
    mh32 = theory(d32)
    e32 = float(input("EEE 3217 Digital Signal Processing I : "))
    cm32 = theory(e32)

    th32 = dc32 + me32 + ph32 + mh32 + cm32

    w32 = float(input("EEE 3208 Communication Theory LAB : "))
    dcl32 = lab(w32)
    x32 = float(input("EEE 3210 Microprocessor,Interfacing & System Design LAB : "))
    phl32 = lab(x32)
    y32 = float(input("EEE 3218 Digital Signal Processing I LAB : "))
    cml32 = lab(y32)

    lb32 = dcl32 + phl32 + cml32

    m32 = th32 + lb32
    gpa(m32, 19.5)


def fourone():
    print("Enter Your Final Exam Marks : ")

    a41 = float(input("EEE 4105 Control System 1 : "))
    dc41 = theory(a41)
    b41 = float(input("EEE 41** Elective I : "))
    me41 = theory(b41)
    c41 = float(input("EEE 41** Elective II : "))
    ph41 = theory(c41)
    d41 = float(input("EEE 41** Elective III : "))
    mh41 = theory(d41)
    e41 = float(input("EEE 41** Elective IV : "))
    cm41 = theory(e41)

    th41 = dc41 + me41 + ph41 + mh41 + cm41

    w41 = float(input("EEE 4105 Control System 1 LAB : "))
    dcl41 = lab(w41)
    x41 = float(input("EEE 41** Elective I LAB : "))
    phl41 = lab(x41)
    y41 = float(input("EEE 41** Elective II LAB : "))
    cml41 = lab(y41)

    lb41 = dcl41 + phl41 + cml41

    m41 = th41 + lb41
    gpa(m41, 19.5)


def fourtwo():
    print("Enter Your Final Exam Marks : ")

    a42 = float(input("HUM 4229 Society,Ethics & Technology : "))
    dc42 = theory(a42)
    b42 = float(input("EEE 42** Elective V : "))
    me42 = theory(b42)
    c42 = float(input("EEE 42** Elective VI : "))
    ph42 = theory(c42)
    d42 = float(input("EEE 42** Elective VII : "))
    mh42 = theory(d42)
    e42 = float(input("EEE 42** Elective VIII : "))
    cm42 = theory(e42)

    th42 = dc42 + me42 + ph42 + mh42 + cm42

    w42 = float(input("EEE 42** Elective VI LAB : "))
    dcl42 = lab(w42)
    x42 = float(input("EEE 42** Elective VIII LAB : "))
    phl42 = lab(x42)
    thes = input("Project & Thesis GRADE : ")
    thes42 = thesis(thes)
    lb42 = dcl42 + phl42 + thes42

    m42 = th42 + lb42
    gpa(m42, 24)


def gpa(total, credit):
    grade = total / credit
    grader = str(round(grade, 2))
    print("Your GPA:", grader, " ")


def Start():
    print(
        "                   |GPA Calculator for EEE Department(AUST)|\n                 ____________________________________________ \n")
    print("                          Department of EEE\n ")
    print(
        "1. 1st Year 1st Semester\n2. 1st Year 2nd Semester\n3. 2nd Year 1st Semester\n4. 2nd Year 2nd Semester\n5. 3rd Year 1st Semester\n6. 3rd Year 2nd Semester\n7. 4th Year 1st Semester\n8. 4th Year 2nd Semester ")
    opt = input("Choose your Semester :  ")
    if opt == "1":
        oneone()
    elif opt == "2":
        onetwo()
    elif opt == "3":
        twoone()
    elif opt == "4":
        twotwo()
    elif opt == "5":
        threeone()
    elif opt == "6":
        threetwo()
    elif opt == "7":
        fourone()
    elif opt == "8":
        fourtwo()
    else:
        print("Wront Input. Press 1/2/3/4/5/6/7/8 according to your semester")


Start()
i = 0;
while i < 1:
    print("______________________________________________")
    print("1.Main Menu\n2.Close Program")
    end = input("press 1 for main menu or 2 for closing application: ")
    if end == "1":
        i = 0
        Start()
    elif end == "2":
        i = 2
        print("thankyou")
    else:
        print("Wrong Input,try again")
print("GPA Calculator developed by Faisal Farhan")








