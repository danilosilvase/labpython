
# Write a program that can read fortune files and returns a random fortune to the user.
# Fortune Format Example: Fortunes are separated by a % sign on a single line followed by a newline character.

import random

class Fortune():    
  
    def readFortune(self):
        with open("/tmp/fortune") as file:
            for line in file:
                fortune = (line.strip().split("%"))
        ## return a random value
        return random.choice(fortune)    

    def printResult(self, user):
        print("{}'s fortune is £{}".format(user,self.readFortune()))

def main():
    fortuna = Fortune()
    fortuna.printResult("Danilo")

if __name__ == '__main__':
    main()


            









