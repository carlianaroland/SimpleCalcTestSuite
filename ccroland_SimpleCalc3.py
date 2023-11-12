# Carliana Roland
# COMP163
# Trig Calc

import ccroland_MyMath as MM


def calcSin(x: float):
    pi = 3.141592653589793
    while x < -pi or x > pi:
        x += (2 * pi)
    while x > pi:
        x -= (2 * pi)

    t = x
    sine = t
    i = 0
    while abs(t) >= 0.0000000001:
        t *= ((-x**2) / ((2*i + 3) * (2*i + 2)))
        sine += t
        i += 1
    return sine


def calcCosine(x: float):
    pi = 3.141592653589793
    while x < -pi or x > pi:
        x += (2 * pi)
    while x > pi:
        x -= (2 * pi)

    t = 1
    cosine = t
    i = 0
    while abs(t) >= 0.0000000001:
        t *= ((-x ** 2) / ((2 * i + 2) * (2 * i + 1)))
        cosine += t
        i += 1
    return cosine


def calcTan(x: float):
    return calcSin(x) / calcCosine(x)


if __name__ == "__main__":

    print((f'calcSin: Sine of {1.047197551} expect {MM.calcSin(1.047197551)} got: ' + str(MM.calcSin(1.047197551)) +
           " : " + ("Pass" if MM.calcSin(1.047197551) == MM.calcSin(1.047197551) else "Fail")))

    print((f'calcCosine: Cosine of {1.047197551} expect {MM.calcCosine(1.047197551)} got: ' +
           str(MM.calcCosine(1.047197551)) + " : " + ("Pass" if MM.calcCosine(1.047197551) ==
            MM.calcCosine(1.047197551) else "Fail")))

    print((f'calcTan: Tangent of {1.047197551} expect {MM.calcTan(1.047197551)} got: ' + str(MM.calcTan(1.047197551)) +
           " : " + ("Pass" if MM.calcTan(1.047197551) == MM.calcTan(1.047197551) else "Fail")))
