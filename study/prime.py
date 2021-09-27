
### Print the prime mumbers beteween x and y
def prime():
    for num in range(100,200):
        if all(num % i != 0 for i in range(2,num)):
            print(num)

def main():
    prime()

if __name__=="__main__":
    main()