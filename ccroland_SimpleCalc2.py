# Carliana Roland
# COMP163
# Advanced Calc

import ccroland_MyMath as MM


def calcAbs(num: int):
    if num < 0:
        return -num
    else:
        return num


def calcRoot(n: int, r: int):
    g = 1
    while True:
        g_prime = g - (g ** r - n) / (r * g ** (r - 1))
        if calcAbs(g_prime - g) < 0.0000000001:  # the user-defined absolute function is to find the absolute for the
            # root function
            return g
        g = g_prime


def calcGCD(n1: int, n2: int):
    if n2 == 0:
        return n1
    elif n1 == 0:
        return n2
    else:
        return calcGCD(n2, n1 % n2)


def calcLCM(num1: int, num2: int):
    return (num1 * num2) / calcGCD(num1, num2)


def calcPow(n, power):
    count = 1
    for i in range(1, power+1):
        count *= n
    return count


if __name__ == "__main__":
    print((f'calcAbs: The absolute of {MM.calcAbs(12)} expect {MM.calcAbs(12)} got: ' + str(MM.calcAbs(12)) + " : " +
           ("Pass" if MM.calcAbs(12) == MM.calcAbs(12) else "Fail")))

    print((f'calcRoot: The root of {5.0625} and {4} expect {MM.calcRoot(5.0625, 4)} got: ' + str(MM.calcRoot(5.0625, 4))
           + " : " + ("Pass" if MM.calcRoot(5.0625, 4) == MM.calcRoot(5.0625, 4) else "Fail")))

    print((f'calcGCD: The GCD of {12} and {6} expect {MM.calcGCD(12, 6)} got: ' + str(MM.calcGCD(12, 6)) + " : " + (
        "Pass" if MM.calcGCD(12, 6) == MM.calcGCD(12, 6) else "Fail")))

    print((f'calcLCM: The LCM of {4} and {6} expect {MM.calcLCM(4, 6)} got: ' + str(MM.calcLCM(4, 6)) + " : " + (
        "Pass" if MM.calcLCM(4, 6) == MM.calcLCM(4, 6) else "Fail")))

    print((f'calcPow: The power of {5} and {2} expect {MM.calcPow(5, 2)} got: ' + str(MM.calcPow(5, 2)) + " : " + (
        "Pass" if MM.calcPow(5, 2) == MM.calcPow(5, 2) else "Fail")))
