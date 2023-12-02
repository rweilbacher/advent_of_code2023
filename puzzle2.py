

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

id_sum = 0
target_red = 12
target_green = 13
target_blue = 14
for game in games:
    valid_rounds = 0
    for round in game.rounds:
        if round.red <= target_red and round.green <= target_green and round.blue <= target_blue:
            valid_rounds += 1
        else:
            pass
    if valid_rounds == len(game.rounds):
        id_sum += game.game_id
print(id_sum)