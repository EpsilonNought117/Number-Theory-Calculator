def main():

    import sys

    def gcd(a, b):  # standard GCD function using eulcidean algorithm

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

    def linear_cong(a,b,c): # linear congruence function for solving the congruences N_i*x ≅ 1 (mod m)
                            # where N_i is N divided by m_i

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

    def CRT(a, m):

        a = [int(i) for i in a] # the residues
        m = [int(i) for i in m] # the moduli
        n = []                  # empty list to store the N_i's
        y = []                  # empty list to store inverse of N_i (mod m)
        X = 0                   # the final integer which satisfies the given system of congruence

        if len(a) != len(m):         # there has to be same number of residues as the moduli
            return "\nINVALID INPUT"
            
        for i in range(1, len(m)):  # I had to restrict input to co-prime moduli as it was getting a bit too difficult for me to factor down
            for j in range(i):      # into co-prime moduli to solver the set of congruences
                if gcd(m[i], m[j]) != 1:
                    return "\nMODULI ARE NOT CO-PRIME, PLEASE TRY AGAIN!"
                    

        for i in range(len(a)):  # reducing the residue (mod m)
            if a[i] > m[i]:
                a[i] = a[i] % m[i]

        N = 1 # will use this to calculate N1, N2, N3 ... and so on

        for i in m:     # calculating the N_i's
            N *= i

        for i in m:     # storing them in the list
            n.append(N//i)

        for i in range(len(m)):

            x = linear_cong(n[i], m[i], 1) # calling the linear congruence function to solve N_i*x ≅ 1 (mod m)

            if x < 0:                      # just in case my answer is negative
                x = x + m[i]

            y.append(x) # appending the calculated inverses into a list

        for i in range(len(a)):

            X += n[i]*y[i]*a[i] # summing up the (N_i)*(n'_i)*(a_i)

        return (X % N) # reducing the X to X(mod N) and returning the solution

    while True:

        message = str(input("This is a Chinese Remainder Theorem calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the CRT calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = list(map(int, input("\nENTER THE RESIDUES: ").split(" ")))
                m = list(map(int, input("ENTER CO-PRIME MODULI: ").split(" ")))
                
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue

            k = CRT(a, m)
            print(k)
        
        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()
