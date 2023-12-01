DIGITS = "0123456789"
SPELLED_DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def forwards(line):
    idx = 0
    curr_word = ""
    while idx < len(line):
        curr_word += line[idx]
        if line[idx] in DIGITS:
            return line[idx]
        else:
            for key in SPELLED_DIGITS.keys():
                if key in curr_word:
                    return SPELLED_DIGITS[key]
        idx += 1


def backwards(line):
    idx = len(line) - 1
    curr_word = ""
    while idx >= 0:
        curr_word = line[idx] + curr_word
        if line[idx] in DIGITS:
            return line[idx]
        else:
            for key in SPELLED_DIGITS.keys():
                if key in curr_word:
                    return SPELLED_DIGITS[key]
        idx -= 1


with open("puzzle1_input.txt") as file:
    content = file.read()

content = content.split("\n")[:-1]

sum = 0
for line in content:
    value = forwards(line) + backwards(line)
    sum += int(value)
print(sum)
