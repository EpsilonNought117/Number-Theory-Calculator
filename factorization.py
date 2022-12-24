def main():
    def factor(x):
        i , factor_list = 2, [] # start with i as 2 because starting with 1 will lead to infinitely many executions of inner loop 
                                # also a list for storing the prime factors of x
            
        while i * i <= x:       # worst case time complexity of outer while loop is O(sqrt(n))
                            
            if x % i == 0:      # direct search factorization algorithm
                while x % i == 0:
                    x /= i
                    factor_list.append(i)

            i += 1
            
        if x > 1:
            factor_list.append(int(x))
        
        return factor_list

    while True:

        message = str(input("This is a Factorization Calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the Factorization Calculator!")
            break

        elif message.upper() == 'Y':
            
            try:
                n = int(input("\nENTER N: "))
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue
            
            print(factor(n))

        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()