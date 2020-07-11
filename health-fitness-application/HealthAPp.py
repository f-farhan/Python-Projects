def BMI():
    gender = input("Choose your Gender\nPress 1 if Male or Press 2 if Female : ")
    age = input("Enter Age:")
    print("Enter Height(in ft.inch)")
    feet = input("Feet=")
    inch = input("Inch=")
    ft = float(feet)
    inch = float(inch)
    f1 = ft * 0.3048
    i1 = inch * 0.0254
    h = f1 + i1
    weight = input("Enter Weight(in kg):")
    w = float(weight)
    bmi = w / (h * h)
    print("Body Mass Index Status:")
    if bmi <= 16:
        print("Extremely Under Weight")
    elif 16 < bmi <= 18.5:
        print("Underweight")
    elif 18.6 < bmi <= 25:
        print("Normal Weight")
    elif 25.1 < bmi <= 30:
        print("Overweight")
    elif 30.1 < bmi <= 35:
        print("Obese class one")
    elif 35.1 < bmi <= 40:
        print("Overweight")
    elif bmi > 40:
        print("Morbid Obese")
    else:
        print("Wrong Information,Try Again")
    brmi = str(round(bmi, 2))
    print("Your Body Mass Index is:",brmi," ")



def Calorie():
    gender = input("Choose your Gender\nPress M if Male or Press F if Female : ")
    C = 0
    if gender == "M" or "m":
        age = input("Enter Age:")
        age = float(age)
        print("Enter Height(in ft.inch)")
        feet = input("Feet=")
        inch = input("Inch=")
        ft = float(feet)
        inch = float(inch)
        f1 = ft * 0.3048
        i1 = inch * 0.0254
        h = (f1 + i1) * 100
        weight = input("Enter Weight(in kg):")
        w = float(weight)
        bmr = 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * age)
        print("Choose your Physical Active Intensity:\n1.Sedentary\n2.Low Active\n3.Active\n4.Very Active")
        pa = input("press 1,2,3 or 4 for your PAI: ")
        if pa == "1":
            C = bmr * 1.2
        elif pa == "2":
            C = bmr * 1.375
        elif pa == "3":
            C = bmr * 1.55
        elif pa == "4":
            C = bmr * 1.725
        else:
            print("Wrong Input,Enter Again")
    elif gender == "F" or "f":
        age = input("Enter Age:")
        age = float(age)
        print("Enter Height(in ft.inch)")
        feet = input("Feet=")
        inch = input("Inch=")
        ft = float(feet)
        inch = float(inch)
        f1 = ft * 0.3048
        i1 = inch * 0.0254
        h = (f1 + i1) * 100
        weight = input("Enter Weight(in kg):")
        w = float(weight)
        bmr = 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * age)
        print("Choose your Physical Active Intensity:\n1.Sedentary\n2.Low Active\n3.Active\n4.Very Active")
        pa = input("press 1,2,3 or 4 for your Physical Active Intensity: ")
        if pa == "1":
            C = bmr * 1.2
        elif pa == "2":
            C = bmr * 1.375
        elif pa == "3":
            C = bmr * 1.55
        elif pa == "4":
            C = bmr * 1.725
        else:
            print("Wrong Input,Enter Again")
    else:
        print("Wrong Input")
    cal = str(round(C, 2))
    print("Your Daily Calorie Need is:",cal," Calories")



def BV():
    gender = input("Choose your Gender\nPress M if Male or Press F if Female : ")
    bv = 0
    if gender == "M" or "m":
        age = input("Enter Age: ")
        age = float(age)
        print("Enter Height(in ft.inch)")
        feet = input("Feet=")
        inch = input("Inch=")
        ft = float(feet)
        inch = float(inch)
        f1 = ft * 0.3048
        i1 = inch * 0.0254
        h = (f1 + i1)
        weight = input("Enter Weight(in kg): ")
        w = float(weight)
        bv = (0.3699 * (h * h * h)) + (0.03219 * w) + 0.6041

    elif gender == "F" or "f":
        age = input("Enter Age: ")
        age = float(age)
        print("Enter Height(in ft.inch)")
        feet = input("Feet=")
        inch = input("Inch=")
        ft = float(feet)
        inch = float(inch)
        f1 = ft * 0.3048
        i1 = inch * 0.0254
        h = (f1 + i1)
        weight = input("Enter Weight(in kg):")
        w = float(weight)
        bv = (0.3561 * (h * h * h)) + (0.03308 * w) + 0.1833
    bfv = str(round(bv, 2))
    print("Your Blood Volume is:",bfv,"Litres")

def WI():
    age=input("Enter Age: ")
    age=float(age)
    weight=input("Enter weight(in kg): ")
    weight=float(weight)
    w= weight*2.20462
    b=0
    a= w/2.2
    if age<= 30:
        b=a*40
    elif 30<age<55:
         b=a*35
    elif age>55:
        b=a*30
    c= b/28.3
    result= c/33.8
    r = str(round(result, 2))
    print("Required Water Intake:", r, "Litres")

def BF():
    gender=input("Choose your Gender\nPress M if Male or Press F if Female : ")
    if gender== "M" or "m":
        weight=input("Weight(in kg) : ")
        w: float=float(weight)
        waist=input("Waist(in cm : ")
        wst=float(waist)
        lbm=(w*2.205*1.082)+(94.42)-(wst*0.393*4.15)
        bfw=(w*2.205)-(lbm)
        bfp=(bfw/(w*2.205))*100
        print(bfp)
        if 2<bfp<=5:
            print("BODY FAT STATUS: Essential Fat")
        elif 6<bfp<=13:
            print("BODY FAT STATUS: Athlete")
        elif 14 < bfp <= 17:
            print("BODY FAT STATUS: Fit")
        elif 18 < bfp <= 24:
            print("BODY FAT STATUS: Average")
        elif bfp>24:
            print("BODY FAT STATUS: Obese")
    elif gender=="F" or "f":
        w=float(input("Weight(in kg) : "))
        forearm = float(input("Forearm(in cm) : "))
        wrist = float(input("Wrist(in cm) : "))
        waist = float(input("Waist(in cm) : "))
        hip = float(input("Hip(in cm) : "))
        lbm=(w*2.205*0.732)+(8.987)+(wrist/3.140)-(waist*0.157)-(hip*0.249)+(forearm*0.43)
        bfw=(w*2.205)-(lbm)
        bfp=(bfw/(w*2.205))*100
        if 10 < bfp <= 13:
            print("BODY FAT STATUS: Essential Fat")
        elif 14 < bfp <= 20:
            print("BODY FAT STATUS: Athlete")
        elif 21 < bfp <= 24:
            print("BODY FAT STATUS: Fit")
        elif 25 < bfp <= 31:
            print("BODY FAT STATUS: Average")
        elif bfp > 31:
            print("BODY FAT STATUS: Obese")
    else:
       print("wrong input")


def Start():
    print("                   |HEALTH & FITNESS|\n                 ______________________ ")
    print(
        "                  1.Body Mass Index\n                  2.Calories\n                  3.Blood Volume\n                  4.Water Intake\n                  5.Body Fat ")
    opt=input("Choose your option : ")
    if opt=="1":
        BMI()
    elif opt=="2":
         Calorie()
    elif opt=="3":
        BV()
    elif opt=="4":
        WI()
    elif opt=="5":
        BF()
    else:
        print("Wront Input. Press 1,2,3 or 4")
Start()
i=0;
while i<1:
    print("______________________________________________")
    print("1.Main Menu\n2.Close Program")
    end = input("press 1 for main menu or 2 for closing application: ")
    if end == "1":
        i=0
        Start()
    elif end == "2":
        i=2
        print("thankyou")
    else:
        print("Wrong Input,try again")
print("HEALTH & FITNESS Application developed by Faisal Farhan")