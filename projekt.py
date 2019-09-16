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
        self.deck = []  # start with an empty list
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
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21:
            self.value -= 9


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
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
    # Print an opening statement


    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)

        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts()
            break


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            dealer.add_card(deck.deal())

        # Show all cards
        show_all(player,dealer)

        # Run different winning scenarios
        if dealer.value > player.value:
            player_busts()
            player_chips.lose_bet()
        elif dealer.value < player.value:
            player_wins()
            player_chips.win_bet()
        else:
            print("Draw")


    # Inform Player of their chips total

    # Ask to play again
    again = input("Would you like to play again(y/n)? ")
    if again == "y":
        playing = True
    else:
        break
