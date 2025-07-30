class RegularFrame():
    throw1: int
    throw2: int

    def __init__(self, frame: str):
        self.throw1 = int(frame[0]) if frame[0] != "-" else 0
        self.throw2 = int(frame[1]) if frame[1] != "-" else 0

    def calculate(self) -> int:
        return self.throw1 + self.throw2