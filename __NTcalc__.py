import simultaneous_congruences                    # import all previous programs
import euler_totient
import factorization
import gcd
import linear_congruence
import linear_diophantine

while True:     #The calculator works until the user quits

    print("WELCOME TO NUMBER THEORY CALCULATOR!")
    print("\nEnter 1 for Chinese Remainder Theorem")
    print("\nEnter 2 for Euler totient function")
    print("\nEnter 3 for Number Factoring Calculator")
    print("\nEnter 4 for GCD")
    print("\nEnter 5 for Linear congruence calculator")
    print("\nEnter 6 for Linear Diophantine Equation Solve")
    print("\nEnter 7 to quit the program")

    message = int(input("\nPLEASE ENTER YOUR OPTION: "))

    if message == 7:
        print("\nTHANK YOUU FOR USING NT CALCULATOR!")
        break
    elif message == 1:
        simultaneous_congruences.main()
    elif message == 2:
        euler_totient.main()
    elif message == 3:
        factorization.main()
    elif message == 4:
        gcd.main()
    elif message == 5:
        linear_congruence.main()
    elif message == 6:
        linear_diophantine.main()
    else:
        print("INVALID INPUT! PLEASE TRY AGAIN!")




