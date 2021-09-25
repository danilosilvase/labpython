#!/bin/python3

# Write a program that can read fortune files and returns a random fortune to the user.
# Fortune Format Example: Fortunes are separated by a % sign on a single line followed by a newline character. 

import random

class Fortune:
    def __init__(self, name: str, filename: str):
        self.name = name
        self.filename = filename

    def read_fortunes_file(self, filename: str) -> list:
        fortunes = []
        with open(filename) as logfile:
            for line in logfile:
                if line.strip():
                    fortunes.append(list(line.strip().split("%")))
        return fortunes

    def print_fortunes_file(self):
        fortunes = self.read_fortunes_file(self.filename)
        for values in fortunes:
            print(values)

    def add_fortune(self, fortune):
        with open(self.filename, "a") as logfile:
            logfile.write(fortune + "\n" + "\n")

    def print_user_fortune(self):
        fortunes = self.read_fortunes_file(self.filename)
        user_fortune = random.choice(fortunes)
        total = 0
        for line in user_fortune:
            total += int(line)
        print("The {}s fortune is £{}!".format(self.name, float(total)))

def main():
    try:        
        user1 = Fortune("Danilo", "/tmp/fortune")
        # user1.add_fortune("344%222%444585")
        # user1.add_fortune("444444%123%8889")
        # user1.add_fortune("44%987%434442")
        user1.print_user_fortune()
    except:
        print("Error found")


if __name__ == '__main__':
    main()

