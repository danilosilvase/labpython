


def check_palimdrome(word_a, word_b):
    print("Word a = {} - Word b = {}".format(word_a, word_b[::-1]))
    if word_a == word_b[::-1]:
        print("Is palindrome")
    else:        
        print("try again!")

def main():
    while True:
        word_a = input("Type the fist word: ")
        word_b = input("Type the second word: ")
        check_palimdrome(word_a, word_b)

if __name__=="__main__":
    main()

