def main():
    import sys

    def gcd(a, b): # the GCD function from GCD.py

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

    def linear_cong(a,b,c): # the linear congruence function will make use of the extended euclidean algorithm to solved the congruence
                            # ax ≅ c (mod b)
            
        if gcd(a, b) > 1:   # if the gcd(a, b) is 1, no need to check

            if c % gcd(a, b) != 0:                  # standard result from linear diophantine equation that no solution exists if C is not divisible
                return "\nNO SOLUTIONS POSSIBLE!"   # by gcd(a, b) because this can be re-written as ax + by = c and both sides need to be intgers

            g = gcd(a, b)    # reducing a, b by their gcd, also c
            a //= g
            b //= g
            c //= g

        # this is the fun part
        # I will explain using an example of a = 29, b = 67 and c = 129, thus 29x + 67y = 129
        # this is equivalent to solving x = (129 - 67*y)/29
        # we reduce this to x = -2*y + (129 - 9*y)/29
        # now substitute (129 - 9*y)/29 = u
        # solving y in terms of u we get (129 - 29*u)/9
        # the key observation is how 67 got reduced to 29 and 29 got reduced to 9
        # repeating these steps continuously till 29 is reduced to gcd(67, 29) or gcd(a, b)
        # we get a continued fraction in the denominator (recursion was an obvious choice for me here) of the form (c - b*f)/gcd(a, b)
        # now we can simply put any integer of our choice in place of 'f' and i chose c//a
        # this will very easily return and integer value of 'x' in the end!

        if b == 1:           
            return c//a      

        else:
            a, b = b, a % b
            u = linear_cong(a,b,c)

            return (c - a*u)//b

        # time complexity of this function is O(logn) as well as it just repeats until we find the gcd(a, b)
        # the extended euclidean algorithm
        # just like the GCD program, it starts to falter for number with more than 15 digits
    
    while True:

        message = str(input("This is a linear congruence calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the Linear congruence calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = int(input("\nENTER A: "))
                b = int(input("ENTER B: "))
                c = int(input("ENTER C: "))
                
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue
        
            k = linear_cong(a, b, c)
            print(k)
        
        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()