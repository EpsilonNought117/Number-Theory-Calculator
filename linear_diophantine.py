def main():
    import functools

    def gcd(a, b): #GCD using euclidean algorithm 

        if b > a:
            a , b = b, a

        while True:

            q = int(a / b)
            r = a - (b*q)

            if r == 0:
                return int(b)

            else:
                a = (a-r)/q
                b = r

    def linear_cong(a,b,c): #solution of linear congruence using extended eulcidean algorithm

        g = gcd(a, b)

        if g > 1:

            a //= g
            b //= g
            c //= g
            
        if b == 1:

            return c//a

        else:

            a, b = b, a % b
            u = linear_cong(a,b,c)
            return (c - a*(u))//b

    def diophantine(n, N): # defining the function to solve diophantine equation

        print("\n")
        n = [int(i) for i in n] # converting the input list to integers
        
        n = list(set(n))    # removing any repeated input of coefficients

        soln = []

        g = functools.reduce(gcd, n)

        if N % g != 0: # diophantine equations have no solution in integers if the gcd of all coefficients doesn't divide the integer N on RHS
            print("This Diophantine Equation has no possible solutions!")
            quit()
        
        for i in range((len(n) - 1), -1, -1): # taking all the coefficients of the diophantine equation except the last

            g = n[0] 
            
            for j in range(i): # calculate gcd of coefficients till the second-last coefficient
                g = gcd(g, n[j])

            # solving a linear diophantine equation of form n1*x1 + n2*x2 + n3*x3 + .........+ nk*xk = N
            # is same as solving g*y + nk*xk = N where
            # g is the gcd(n1, n2, n3, ......, n(k-1)) and y is any coefficient
            # solving this will yield a solution for xk via the linear congruence method
            # we can now subtract (nk*xk) from N resulting in a new N1
            # now reduce g*y to g1*y1 + n(k-1)*x*(k-1) = N1
            # repeatedly solve this till the integer value for x_i are found

            x = linear_cong(g, n[i], N)

            if n[i] != n[0]:

                y = (N - g*x)//n[i] # returning the value of xk
                N = x*g             # and assigning new value of N
                
            else:
                y = N//n[i]
            
            soln.append(y)

        return n, soln[::-1]

    while True:

        message = str(input("This is a Linear Diophantine Equation Solver. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the LDE Solver!")
            break

        elif message.upper() == 'Y':

            try:
                n = list(map(int , input("\nENTER THE INTEGER COEFFICIENTS: ").split(" ")))
                N = int(input("ENTER THE INTEGER FOR WHICH TO SOLVE THE LDE: "))

            except ValueError:
                
                print("\nInvalid Input! Please try again.")
                continue

            print(diophantine(n, N))
                
        else:
            print("\nInvalid Input! Please try again.")
        
if __name__ == "__main__":
    main()



