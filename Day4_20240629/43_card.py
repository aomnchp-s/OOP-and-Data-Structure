import random
from itertools import product

class Card:
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A']
    
    def __init__(self, suit, rank):
        if suit not in Card.suits:
            raise ValueError(f"Invalid suit: {suit}. Valid suits are: {Card.suits}")
        if rank not in Card.ranks:
            raise ValueError(f"Invalid rank: {rank}. Valid ranks are: {Card.ranks}")
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return self.__str__()

class CardShuffler:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = [Card(suit, rank) for suit, rank in product(Card.suits, Card.ranks)] * num_decks
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        card = self.cards[self.index]
        self.index += 1
        return card

    def draw_card(self):
        if len(self.cards) == 0:
            raise IndexError("No more cards to draw")
        return self.cards.pop()

if __name__ == "__main__":
    shuffler = CardShuffler(num_decks=2)

    try:
        card = shuffler.draw_card()
        print(f"Drew card: {card}")
    except IndexError as e:
        print(e)

    shuffler.shuffle()
    for card in shuffler:
        print(card)
