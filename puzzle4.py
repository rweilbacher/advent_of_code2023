class Card:
    def __init__(self, card_id, winning, have):
        self.card_id = card_id
        self.winning = winning
        self.have = have


with open("puzzle4_input.txt") as file:
    text = file.read()

text = text.split("\n")[:-1]
cards = []
for line in text:
    line = line.split(":")
    card_id = line[0].split()[1]
    number_groups = line[1].split("|")
    winning = number_groups[0].split()
    have = number_groups[1].split()
    [int(i) for i in winning]
    [int(i) for i in have]
    cards.append(Card(card_id, winning, have))

sum = 0
for card in cards:
    points = 0
    for number in card.have:
        if number in card.winning:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum += points
print(sum)
