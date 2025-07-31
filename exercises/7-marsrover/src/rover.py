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
        return "?"

    def tourner_droite(self):
        directions = ["N", "E", "S", "W"]
        i = directions.index(self.direction)
        self.direction = directions[(i + 1) % 4]

    def tourner_gauche(self):
        directions = ["N", "E", "S", "W"]
        i = directions.index(self.direction)
        self.direction = directions[(i - 1) % 4]

    def avancer(self, carte):
        if self.direction == "N":
            dx, dy = 0, -1
        elif self.direction == "S":
            dx, dy = 0, 1
        elif self.direction == "E":
            dx, dy = 1, 0
        else:
            dx, dy = -1, 0

        nx = self.x + dx
        ny = self.y + dy

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            return

        if carte.grille[ny][nx] == "🌳":
            return

        self.x = nx
        self.y = ny