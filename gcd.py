def main():

    def gcd(a, b):    #defining the GCD Functions

        if b > a:           #Euclidean algorithm works only if a > b, so swapping if a < b is true
            a , b = b, a

        while True:         

            q = a//b      # calculating qoutient and taking integer part, can also 
            r = a - (b*q) # remainder is calculated 

            if r == 0:    # condition to return the last b which is equivalent to gcd of a and b
                return int(b)
            else:             # if not true
                a = (a-r)/q   # assign a = b
                b = r         # assign b = r , continue the loop

    # observation in euclidean algorithm is that the remainder 'r' is always less than half of 'a' even in the worst case scenario
    # of fibonacci sequence where every time is the sum of previous two
    # since a and b are halved in alternating steps (a*b) is halved every step till the product becomes >= 1
    # so finally (a*b)/(2**N) >= 1 where N is the number of times the product got halved
    # after some algebric manipulation we get N <= 7*log(b), hence time complexity of this algorithm is O(logn)

    # I don't know why but this method doesn't return proper integers and starts to make errors for number with more than 15 digits

    while True:

        message = str(input("This is a GCD Calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the GCD calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = int(input("\nENTER A: "))
                b = int(input("ENTER B: "))

            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue

            k = gcd(a, b)
            print(k)

        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()