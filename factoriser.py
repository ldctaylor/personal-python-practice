# This program will find the factors, and prime factors, of a given number.
def main():
    while True:
        try:
            num = int(input("Give me a number you'd like to find the factors of: "))
            break
        except:
            print("Invalid input, try again")
    print(f"The factors of {num} are {find_factors(num)}")
    print(f"And the prime factors are {find_primes(find_factors(num))}")

def find_factors(num):
    numbers_to_num = [] #will populate with all the integers up to the number selected
    factors = [] #will be populated with list of factors
    for _ in range(1,num+1):
        numbers_to_num.append(_)
    for i in numbers_to_num:
        for j in numbers_to_num:
            if i*j==num:
                if i not in factors: #only adds to list of factors if not already there to prevent duplicates
                    factors.append(i)
                if j not in factors:
                    factors.append(j)
    factors.sort()
    return factors

#Find the factors that are prime: 
def find_primes(factors):
    primes = []
    for _ in factors:
        prime = find_factors(_)
        if len(prime) ==2:
            if prime[0] not in primes: 
                primes.append(prime[0])
            if prime[1] not in primes:
                primes.append(prime[1])
    return primes
        
if __name__ == "__main__":
    main()



