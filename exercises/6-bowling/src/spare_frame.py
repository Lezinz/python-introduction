class SpareFrame:
    first_throw: int
    bonus_throw: int

    def __init__(self, previous_throw: int, next_throw: str):
        self.first_throw = previous_throw
        if next_throw[0] == "X":
            self.bonus_throw = 10
        elif next_throw[0] == "-":
            self.bonus_throw = 0
        else:
            self.bonus_throw = int(next_throw[0])

    def calculate(self) -> int:
        return 10 + self.bonus_throw