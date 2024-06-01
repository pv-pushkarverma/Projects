import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Cards:
    color_codes = {
        'Red': '\033[91m',
        'Blue': '\033[94m',
        'Green': '\033[92m',
        'Yellow': '\033[93m',
        'Wild': '\033[95m',
        'ENDC': '\033[0m'
    }

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        color_code = Cards.color_codes.get(self.color, Cards.color_codes['ENDC'])
        return f'{color_code}{self.value}[{self.color}]{Cards.color_codes["ENDC"]}'

class Deck:
    def __init__(self):
        self.deck = []
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', 'Skip', 'Reverse']

        for color in colors:
            for value in values:
                self.deck.append(Cards(value, color))
                if value != 0:
                    self.deck.append(Cards(value, color))
        
        for _ in range(4):
            self.deck.append(Cards('+4', 'Wild'))
            self.deck.append(Cards('Wild', 'Wild'))

        random.shuffle(self.deck)
        
    def draw_card(self):
        return self.deck.pop() if self.deck else None

class Players:
    def __init__(self):
        self.player_name = input('Enter your name: ')
        self.players = {'Computer': [], self.player_name: []}
        self.deck = Deck()
        self.played_cards = []
        self.turn = self.player_name

        self.give_cards()
        while True:
            c=self.deck.draw_card()
            if c.value not in ['Skip','+4','+2','Wild','Reverse']:
                self.played_cards.append(c)
                break
    
    def print_rules(self):
        clear_screen()
        print(f"Welcome {self.player_name}.")
        print("\nHere are some rules of Uno.")
        print("\nThe Deck has 108 cards from (0-9) and special cards like 'Skip','Reverse',Wild','+2','+4'.")
        print("\n1.You can play any card if it has either same color or same value as last played card.")
        print("\n2.Special cards:")
        print(" A)'Skip' skips the next players chance.")
        print(" B)'Reverse' reverses the order of playing of players.")
        print(" C)'+2' and '+4' will give next players 2 or 4 cards from the deck.")
        print(" D)'Wild' and '+4 Wild' can be played anytime and they change the color of card to be played.")
        print("\n3.Players are given 7 random cards from the deck.")
        print("\n4.If you do not have any valid card to play then you have to draw a card.")
        print("\n5.The goal of the game is to finish all cards in your hand first to Win.")
        print("\n\nEnjoy The Game!!!\n")
        x=input("Press any key to continue.")
        clear_screen()
    
    def give_cards(self):
        for _ in range(7):
            self.players['Computer'].append(self.deck.draw_card())
            self.players[self.player_name].append(self.deck.draw_card())

    def print_cards(self):
        print(f"\n{self.player_name}'s cards are: ")
        for index,card in enumerate(self.players[self.player_name], start=1):
            print(f"{index}: {card}", end=" , ")
        print()

    def draw_cards(self, count, player):
        print(f"\n{player} draws {count} cards.")
        for _ in range(count):
            self.players[player].append(self.deck.draw_card())

    def check_move(self, card):
        last_card = self.played_cards[-1]
        return card.value == last_card.value or card.color == last_card.color or card.color == 'Wild'

    def move(self, player):
        if player == 'Computer':
            for card in self.players[player]:
                if self.check_move(card):
                    self.played_cards.append(card)
                    self.players[player].remove(card)
                    self.handle_special_cards(card, player)
                    print(f"\nComputer Played Card {card}")
                    return
            self.draw_cards(1, player)
            self.turn = 'Computer' if self.turn == self.player_name else self.player_name
            print(f"\nLast Played Card is: {self.played_cards[-1]}")
        else:
            print(f"\nComputer's Remaining Cards are {len(self.players['Computer'])}")
            self.print_cards()
            while True:
                try:
                    choice = int(input("\nChoose a card number to play or 0 to draw: "))
                    clear_screen()
                    print(f"\nLast Played Card is: {self.played_cards[-1]}")
                    if choice == 0:
                        self.draw_cards(1, player)
                        print(f"\nLast Played Card is: {self.played_cards[-1]}")
                        self.turn = 'Computer' if self.turn == self.player_name else self.player_name
                        return
                    if choice < 0 or choice > len(self.players[player]):
                        print("Invalid choice. Try again.")
                        self.print_cards()
                        print()
                        continue
                    card = self.players[player][choice-1]
                    if self.check_move(card):
                        self.played_cards.append(card)
                        self.players[player].remove(card)
                        self.handle_special_cards(card, player)
                        print(f"\n{self.player_name} Played Card {card}")
                        return
                    else:
                        print("Invalid move. Try again.")
                        self.print_cards()
                        print()
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def handle_special_cards(self, card, player):
        if card.value == '+2':
            self.draw_cards(2, 'Computer' if player == self.player_name else self.player_name)
        elif card.color == 'Wild':
            if player == self.player_name:
                self.print_cards()
                print()
                new_color = input("Choose a color (Red, Blue, Green, Yellow): ")
                while new_color not in ['Red', 'Blue', 'Green', 'Yellow']:
                    new_color = input("Invalid color. Choose again (Red, Blue, Green, Yellow): ")
            else:
                new_color = random.choice(['Red', 'Blue', 'Green', 'Yellow'])
            self.played_cards[-1].color = new_color

            if card.value == '+4':
                self.draw_cards(4, 'Computer' if player == self.player_name else self.player_name)
            else:
                self.turn = 'Computer' if self.turn == self.player_name else self.player_name

        elif card.value in ['Skip','Reverse','None']:
            pass
        else:
            self.turn = 'Computer' if self.turn == self.player_name else self.player_name
            
class Uno(Players):
    def __init__(self):
        super().__init__()

    def play(self):
        self.print_rules()
        print(f"\nLast Played Card is: {self.played_cards[-1]}")
        while True:
            if not self.deck.deck:
                for card in self.played_cards[:-1]:
                    self.deck.deck.append(card)
                random.shuffle(self.deck.deck)
                self.played_cards = [self.played_cards[-1]]
                
            if not self.players['Computer']:
                print("\n\n\n\033[92mComputer Wins!!!\n\n\n")
                break

            if not self.players[self.player_name]:
                    print(f"\n\n\n\033[92m{self.player_name} Wins!!!\n\n\n")
                    break
                
            print()

            if self.turn == 'Computer':
                self.move('Computer')
            else:
                self.move(self.player_name)

if __name__ == "__main__":
    u = Uno()
    u.play()