import ccroland_SimpleCalc1 as SC  # SC = Simple Calc (add, subtract, mult, divide, and floor division)
import ccroland_SimpleCalc2 as AC  # AC = Advanced Calc (root, gcd, lcm, power)
import ccroland_SimpleCalc3 as TC  # TC = Trig Calc (sine, cosine, tangent)


def print_Header():
    print("Carliana Roland")
    print("COMP163")
    print("mTest Suite")


def MenuError():
    print("Invalid selection ")


def Menu1():
    print("A) Add: ")
    print("S) Subtract: ")
    print("M) Multi: ")
    print("D) Div: ")
    print("F) Floor Division: ")
    print("R) Root: ")
    print("G) GCD: ")
    print("L) LCM: ")
    print("P) Power: ")
    print("SS) Sine: ")
    print("C) Cosine: ")
    print("T) Tangent: ")
    print("Q) Quit: ")


print_Header()


MenuItems = ("A", "S", "M", "D", "F", "R", "G", "L", "P", "SS", "C", "T", "Q")
while True:
    Menu1()
    Selection = input("Menu: ").upper()
    if Selection not in MenuItems:
        print(MenuError())
    if Selection == "Q":
        break
# The trig calc functions are only limited to one parameter and all require float inputs.
    if Selection == "SS":
        val = float(input("Enter number here: "))  # parameters only take float inputs
        print((f'calcSin: The Sine of {val} expect {TC.calcSin(val)} got: ' + str(TC.calcSin(val)) +
               " : " + ("Pass" if TC.calcSin(val) == TC.calcSin(val) else "Fail")))  # TC alies is the module the
        # function afterwards is in
    elif Selection == "C":
        val = float(input("Enter number here: "))
        print((f'calcCosine: The Cosine of {val} expect {TC.calcCosine(val)} got: ' + str(TC.calcCosine(val)) +
               " : " + ("Pass" if TC.calcCosine(val) == TC.calcCosine(val) else "Fail")))
    elif Selection == "T":
        val = float(input("Enter number here: "))
        print((f'calcTan: The Tan of {val} expect {TC.calcTan(val)} got: ' + str(TC.calcTan(val)) +
               " : " + ("Pass" if TC.calcTan(val) == TC.calcTan(val) else "Fail")))
# The simple calc functions below take two parameters and all require float inputs
    if Selection == "A":
        op1 = float(input("Enter number: "))
        op2 = float(input("Enter number: "))
        print((f'calcAdd: The sum of {op1} and {op2} expect {SC.calcAdd(op1, op2)} got: ' + str(SC.calcAdd(op1, op2))
               + " : " + ("Pass" if SC.calcAdd(op1, op2) == SC.calcAdd(op1, op2) else "Fail")))  # SC alies is the modul
        # e the function afterwards is in
    elif Selection == "S":
        op1 = float(input("Enter number: "))
        op2 = float(input("Enter number: "))
        print((f'calcSub: The difference of {op1} and {op2} expect {SC.calcSub(op1, op2)} got: ' +
               str(SC.calcSub(op1, op2)) + " : " + ("Pass" if SC.calcSub(op1, op2) == SC.calcSub(op1, op2) else "Fail"))
              )
    elif Selection == "M":
        op1 = float(input("Enter number: "))
        op2 = float(input("Enter number: "))
        print((f'calcMult: The product of {op1} and {op2} expect {SC.calcMult(op1, op2)} got: ' +
        str(SC.calcMult(op1, op2)) + " : " + ("Pass" if SC.calcMult(op1, op2) == SC.calcMult(op1, op2)
                                              else "Fail")))
    elif Selection == "D":
        op1 = float(input("Enter number: "))
        op2 = float(input("Enter number: "))
        print((f'calcDiv: The product of {op1} and {op2} expect {SC.calcDiv(op1, op2)} got: ' +
               str(SC.calcDiv(op1, op2)) + " : " + ("Pass" if SC.calcDiv(op1, op2) == SC.calcDiv(op1, op2) else "Fail"))
              )
    elif Selection == "F":
        op1 = float(input("Enter number: "))
        op2 = float(input("Enter number: "))
        print((f'calcFloorDiv: The product of {op1} and {op2} expect {(SC.calcFloorDiv(op1, op2))} got: ' +
               str(SC.calcFloorDiv(op1, op2)) + " : " + ("Pass" if SC.calcFloorDiv(op1, op2) == SC.calcFloorDiv(op1, op2
                                                                                                                )
                                                         else "Fail")))
# The advanced functions below take two parameters and each require their own input types whether a float or integer
    if Selection == "R":
        op1 = float(input("Enter number: "))
        op2 = int(input("Enter root number: "))
        print((f'calcRoot: The root of {op1} and {op2} expect {AC.calcRoot(op1, op2)} got: ' +
               str(AC.calcRoot(op1, op2)) + " : " + ("Pass" if AC.calcRoot(op1, op2) == AC.calcRoot(op1, op2) else
                                                     "Fail")))  # AC alies is the module the function afterwards is in
    elif Selection == "G":
        op1 = int(input("Enter number: "))
        op2 = int(input("Enter number: "))
        print((f'calcGCD: The GCD of {op1} and {op2} expect {AC.calcGCD(op1, op2)} got: ' + str(AC.calcGCD(op1, op2)) +
               " : " + ("Pass" if AC.calcGCD(op1, op2) == AC.calcGCD(op1, op2) else "Fail")))
    elif Selection == "L":
        op1 = int(input("Enter number: "))
        op2 = int(input("Enter number: "))
        print((f'calcLCM: The LCM of {op1} and {op2} expect {AC.calcLCM(op1, op2)} got: ' + str(AC.calcLCM(op1, op2)) +
               " : " + ("Pass" if AC.calcLCM(op1, op2) == AC.calcLCM(op1, op2) else "Fail")))
    elif Selection == "P":
        op1 = int(input("Enter number: "))
        op2 = int(input("Enter power number: "))
        print((f'calcPow: The power of {op1} and {op2} expect {AC.calcPow(op1, op2)} got: ' +
               str(AC.calcPow(op1, op2)) + " : " + ("Pass" if AC.calcPow(op1, op2) == AC.calcPow(op1, op2) else "Fail"))
              )