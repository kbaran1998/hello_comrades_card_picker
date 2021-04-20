import random


class CardStack:

    def __init__(self, cards):
        self.card_list = cards
        random.shuffle(self.card_list)
        self.card_rest = set()

    def pick_card(self):
        if len(self.card_list) == 0:
            self.card_list = list(self.card_rest)
            random.shuffle(self.card_list)
            self.card_rest = set()
        card = self.card_list.pop()
        self.card_rest.add(card)
        return card
