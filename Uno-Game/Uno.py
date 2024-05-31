import random

class Cards:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return f'{self.value}[{self.color}]'

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
            if c.value not in ['Skip','+4','+2','Wild']:
                self.played_cards.append(c)
                break

    def give_cards(self):
        for _ in range(7):
            self.players['Computer'].append(self.deck.draw_card())
            self.players[self.player_name].append(self.deck.draw_card())

    def print_cards(self):
        print(f"{self.player_name}'s cards are: ")
        for card in self.players[self.player_name]:
            print(card)
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
                    print(f"Computer Played Card {card}")
                    return
            self.draw_cards(1, player)
            self.turn = 'Computer' if self.turn == self.player_name else self.player_name
        else:
            self.print_cards()
            while True:
                try:
                    choice = int(input("Choose a card number to play or -1 to draw: "))
                    if choice == -1:
                        self.draw_cards(1, player)
                        self.turn = 'Computer' if self.turn == self.player_name else self.player_name
                        return
                    if choice < 0 or choice > len(self.players[player]):
                        print("Invalid choice. Try again.")
                        continue
                    card = self.players[player][choice-1]
                    if self.check_move(card):
                        self.played_cards.append(card)
                        self.players[player].remove(card)
                        self.handle_special_cards(card, player)
                        print(f"{self.player_name} Played Card {card}")
                        return
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def handle_special_cards(self, card, player):
        if card.value == '+2':
            self.draw_cards(2, 'Computer' if player == self.player_name else self.player_name)
        elif card.color == 'Wild':
            if card.value == '+4':
                self.draw_cards(4, 'Computer' if player == self.player_name else self.player_name)
            
            else:
                if player == self.player_name:
                    new_color = input("Choose a color (Red, Blue, Green, Yellow): ")
                    while new_color not in ['Red', 'Blue', 'Green', 'Yellow']:
                        new_color = input("Invalid color. Choose again (Red, Blue, Green, Yellow): ")
                else:
                    colors=['Red','Blue','Green','Yellow']
                    new_color=colors[int((random.random()*10)%4)]
                self.turn = 'Computer' if self.turn == self.player_name else self.player_name
            self.played_cards[-1].color = new_color
        elif card.value in ['Skip','Reverse']:
            pass
        else:
            self.turn = 'Computer' if self.turn == self.player_name else self.player_name
            
class Uno(Players):
    def __init__(self):
        super().__init__()

    def play(self):
        while True:
            if not self.players['Computer']:
                print("Computer Wins!!!")
                break
            if not self.players[self.player_name]:
                    print(f"{self.player_name} Wins!!!")
                    break

            print(f"Last Played Card is: {self.played_cards[-1]}")
            print()

            if self.turn == 'Computer':
                self.move('Computer')
            else:
                self.move(self.player_name)

if __name__ == "__main__":
    u = Uno()
    u.play()