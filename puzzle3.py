SYMBOLS = "*+-=#%$@/&"
DIGITS = "0123456789"


class Number:
    def __init__(self, value, x, y, width):
        self.value = value
        self.x = x
        self.y = y
        self.width = width

    def __str__(self):
        return f"{self.value} at {self.x}, {self.y}"


class Symbol:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.value} at {self.x}, {self.y}"


def is_adjacent(number, symbol):
    if number.y - 1 <= symbol.y <= number.y + 1:
        if number.x - 1 <= symbol.x <= number.x + number.width:
            return True
    return False


with open("puzzle3_input.txt") as file:
    text = file.read()

numbers = []
symbols = []
text = text.split("\n")[:-1]
y = 0
while y < len(text):
    curr_number = ""
    x = 0
    while x < len(text[y]):
        char = text[y][x]
        if char in DIGITS:
            curr_number += char
        elif char in SYMBOLS or char == ".":
            if curr_number != "":
                numbers.append(Number(int(curr_number), x - len(curr_number), y, len(curr_number)))
                curr_number = ""
            if char in SYMBOLS:
                symbols.append(Symbol(char, x, y))
            elif char == ".":
                pass
        x += 1
    if curr_number != "":
        numbers.append(Number(int(curr_number), x - len(curr_number), y, len(curr_number)))
        curr_number = ""
    y += 1


# Part 1
sum = 0
for number in numbers:
    sum = sum
    for symbol in symbols:
        if is_adjacent(number, symbol):
                sum += number.value
                break
print(f"Part 1: {sum}")


# Part 2
sum = 0
for symbol in symbols:
    if symbol.value != "*":
        continue
    adj_numbers = []
    for number in numbers:
        if is_adjacent(number, symbol):
            adj_numbers.append(number)
    if len(adj_numbers) == 2:
        sum += adj_numbers[0].value * adj_numbers[1].value
print(f"Part 2: {sum}")