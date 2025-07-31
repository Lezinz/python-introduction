class StrikeFrame:
    bonus_1: int
    bonus_2: int

    def __init__(self, next_throws: str):
        self.bonus_1 = self.parse_throw(next_throws[0])
        self.bonus_2 = self.parse_throw(next_throws[1]) if len(next_throws) > 1 else 0

    def parse_throw(self, throw: str) -> int:
        if throw == "X":
            return 10
        elif throw == "-":
            return 0
        elif throw == "/":
            return 10 - self.bonus_1
        else:
            return int(throw)

    def calculate(self) -> int:
        return 10 + self.bonus_1 + self.bonus_2