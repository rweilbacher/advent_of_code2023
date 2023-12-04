from copy import copy


class Card:
    def __init__(self, card_id, winning, have):
        self.card_id = card_id
        self.winning = winning
        self.have = have
        self.amount = 1
        self.winning_amount = None

    def __str__(self):
        return f"{self.card_id} | {self.amount}"

    def add_cards(self, amount):
        self.amount += amount

    def calc_winning_amount(self):
        if self.winning_amount is not None:
            return self.winning_amount
        else:
            self.winning_amount = 0
            for number in self.have:
                if number in self.winning:
                    self.winning_amount += 1
            return self.winning_amount


with open("puzzle4_input.txt") as file:
    text = file.read()

text = text.split("\n")[:-1]
cards = []
for line in text:
    line = line.split(":")
    card_id = line[0].split()[1]
    card_id = int(card_id)
    number_groups = line[1].split("|")
    winning = number_groups[0].split()
    have = number_groups[1].split()
    [int(i) for i in winning]
    [int(i) for i in have]
    cards.append(Card(card_id, winning, have))

for i in range(0, len(cards)):
    card = cards[i]
    winning_amount = card.calc_winning_amount()
    for j in range(1, winning_amount + 1):
        cards[i + j].add_cards(card.amount)
    all_cards = 0
    for card in cards:
        all_cards += card.amount
    print(f"{card.card_id} | {all_cards}")
pass
