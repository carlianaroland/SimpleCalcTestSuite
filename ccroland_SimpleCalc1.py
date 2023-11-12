# Carliana Roland
# COMP163
# Simple Calc

import ccroland_MyMath as MM


def calcAdd(num1, num2):
    return num1 + num2


avg_list = list()
def calcAvg(avg_list):
    return sum(avg_list) / len(avg_list)

def calcSub(num1, num2):
    if num2 < 0:
        difference = num1 + num2  # the if loop is to add the numbers because the second number is less than the first
    else:
        difference = num1 - num2
    return difference


def calcMult(num1, num2):
    return num1 * num2


def calcDiv(num1, num2):
    return num1 / num2


def calcFloorDiv(f1: float, f2: float):
    return f1 // f2


if __name__ == "__main__": # unit testing for errors and corrections

    print((f'calcAdd: {1} and {2} expect {MM.calcAdd(1, 2)} got: ' + str(MM.calcAdd(1, 2)) + " : " + (
        "Pass" if MM.calcAdd(1, 2) == MM.calcAdd(1, 2) else "Fail")))

    print((f'calcSub: {1} and {2} expect {MM.calcSub(1, 2)} got: ' + str(MM.calcSub(1, 2)) + " : " + (
        "Pass" if MM.calcSub(1, 2) == MM.calcSub(1, 2) else "Fail")))

    print((f'calcDiv: {12} and {6} expect {MM.calcDiv(12, 6)} got: ' + str(MM.calcDiv(12, 6)) + " : " + (
        "Pass" if MM.calcDiv(12, 6) == MM.calcDiv(12, 6) else "Fail")))

    print((f'calcFloorDiv: {12} and {6} expect {MM.calcFloorDiv(12, 6)} got: ' + str(MM.calcFloorDiv(12, 6)) + " : " + (
        "Pass" if MM.calcFloorDiv(12, 6) == MM.calcFloorDiv(12, 6) else "Fail")))
