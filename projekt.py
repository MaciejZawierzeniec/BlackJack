import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} of {self.rank}"


class Deck:

    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return f"{self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21:
            self.value -= 9


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total + 2*self.bet
        self.bet = 0

    def lose_bet(self):
        print("Your chips: {}".format(self.total))


def take_bet():
    bet = Chips()
    bet.bet = input("Type your bet: ")

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    hors = input("\nWould you like to (h)it or (s)tand? ")
    if hors == "s":
        pass
    elif hors == "h":
        hit(deck, hand)

def show_some(player,dealer):

    print("\nPlayer's cards:")
    for card in player.cards:
        print(card)

    print("\nDealer's cards:")
    for card in dealer.cards:
        print(card)
        print("Hidden card")
        break

def show_all(player,dealer):

    print("\nPlayer's cards:")
    for card in player.cards:
        print(card)

    print("\nDealer's cards:")
    for card in dealer.cards:
        print(card)

def player_busts():
    global playing
    playing = False
    print("You lose")

def player_wins():
    global playing
    playing = False
    print("You won")


def push():
    pass


while True:

    deck = Deck()
    deck.shuffle()
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player_chips = Chips()

    take_bet()

    show_some(player,dealer)

    while playing:

        hit_or_stand(deck,player)

        show_some(player,dealer)

        if player.value > 21:
            player_busts()
            break


        while dealer.value < 17:
            dealer.add_card(deck.deal())

        show_all(player,dealer)

        if dealer.value > player.value:
            player_busts()
            player_chips.lose_bet()
        elif dealer.value < player.value:
            player_wins()
            player_chips.win_bet()
        else:
            print("Draw")



    again = input("Would you like to play again(y/n)? ")
    if again == "y":
        playing = True
    else:
        break
