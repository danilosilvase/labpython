class PlayCards():
    
    def read_print_single_value(self, card_number):
        cards = {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        # print(cards.get("B", "Non existe!"))
        if card_number in range(10):
            print(card_number)
        else:
            print(cards[card_number])
            
def main():
    play1 = PlayCards()
    play1.read_print_single_value("J")
    play1.read_print_single_value("Q")
    play1.read_print_single_value("A")
    play1.read_print_single_value(1)
    
if __name__=="__main__":
    main()
    