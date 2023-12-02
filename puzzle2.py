

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.rounds = []

    def add_round(self, red, green, blue):
        self.rounds.append(Round(red, green, blue))

    def __str__(self):
        name = f"Game {self.game_id}: "
        for round in self.rounds:
            name += str(round) + "; "
        return name


class Round:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"{self.red} red, {self.green} green, {self.blue} blue"


def parse_games(text):
    games = []
    for line in text:
        line = line.split(": ")
        game_id = int(line[0].split(" ")[1])
        game = Game(game_id)
        games.append(game)
        rounds = line[1].split("; ")
        for round in rounds:
            colors = round.split(", ")
            red = 0
            green = 0
            blue = 0
            for color in colors:
                color = color.split(" ")
                if color[1] == "red":
                    red = int(color[0])
                elif color[1] == "green":
                    green = int(color[0])
                elif color[1] == "blue":
                    blue = int(color[0])
                else:
                    pass
            game.add_round(red, green, blue)
    return games


with open("puzzle2_input.txt") as file:
    content = file.read()

content = content.split("\n")[:-1]
games = parse_games(content)

sum = 0
for game in games:
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    for round in game.rounds:
        if round.red > highest_red:
            highest_red = round.red
        if round.green > highest_green:
            highest_green = round.green
        if round.blue > highest_blue:
            highest_blue = round.blue
    sum += highest_red * highest_green * highest_blue
print(sum)