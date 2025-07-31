class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def symbole(self):
        if self.direction == "N":
            return "⬆️"
        if self.direction == "S":
            return "⬇️"
        if self.direction == "E":
            return "➡️"
        if self.direction == "W":
            return "⬅️"
        return "❓"