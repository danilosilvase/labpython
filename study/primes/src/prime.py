## Prime numbers

class Prime:
    t = int(input())

    for repeat in range(t):
        n = int(input())
        isPrime = True
        for number in range(1, int(n/2)):
            if n % number == 0:
                isPrime = False
        if isPrime is True:
            print("Prime")
        else:
            print("Not prime")




if __name__ == '__main__':
    prime = Prime()
    # prime.calculePrime(30)
