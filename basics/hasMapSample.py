

class HashMap():
    
    def check_voter(self):
        dict_vote = dict()
        while True:
            name = input()
            option = input()
            dict_vote[name] = option
            if dict_vote.get(name, "nao existe"):
                print("Kick them out")
            else:
                print("Let Them vote")

def main():

    vote_president = HashMap()
    vote_president.check_voter()

if __name__ == '__main__':
    main()