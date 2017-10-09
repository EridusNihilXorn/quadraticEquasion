from math import sqrt
import sys

def solveQuadratic(a, b, c):
    if a == 0:
        return "Highest coefficient was zero. Root is:\n" + str(-c/b)
    D = b**2 - 4*a*c
    #print(D)

    if (D >= 0):
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)

    if (D < 0):
        x1 = (str)(-b/(2*a)) + " + " + "j*" + str(sqrt(-D)/(2*a))
        x2 = (str)(-b/(2*a)) + " - " + "j*" + str(sqrt(-D)/(2*a))

    if D < 0:
        return "Complex roots are:\n" + x1 + " And " + x2

    if D == 0:
        return "D was equal to zero. One root is:\n" + str(x1)

    return "Real roots are:\n" + str(x1) + " And " + str(x2)

def main():
    if len(sys.argv) < 4:
        print ("Incorrect input. Function requires 3 arguments to be passed("A, B, C."))
        return
    print(solveQuadratic(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))

if __name__ == "__main__":
    main()





