from .regular_frame import RegularFrame
from .spare_frame import SpareFrame
from .strike_frame import StrikeFrame

class Bowling:
    def __init__(self, frame_str: str):
        self.frames = frame_str.strip().split()

    def get_next_throws(self, i: int) -> str:
        throws = ""
        idx = i + 1
        while len(throws) < 2 and idx < len(self.frames):
            throws += self.frames[idx]
            idx += 1
        return throws

    def calculate(self) -> int:
        total = 0
        i = 0
        frame_count = 0

        while frame_count < 10:
            frame = self.frames[i]

            if frame == "X":
                next_throws = self.get_next_throws(i)
                strike = StrikeFrame(next_throws)
                total += strike.calculate()
                i += 1

            elif '/' in frame:
                previous_throw = int(frame[0]) if frame[0] != '-' else 0
                if i + 1 < len(self.frames):
                    next_frame = self.frames[i + 1]
                else:
                    next_frame = frame[2:] if len(frame) > 2 else "0"
                spare = SpareFrame(previous_throw, next_frame)
                total += spare.calculate()
                i += 1

            else:
                regular = RegularFrame(frame)
                total += regular.calculate()
                i += 1

            frame_count += 1

        return total