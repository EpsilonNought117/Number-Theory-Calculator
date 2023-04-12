def main():

    def gcd(a, b):    

        if b > a:          
            a , b = b, a

        while True:         
            if b == 0:    
                return int(a)
            else:             
                b, a = a % b, b

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