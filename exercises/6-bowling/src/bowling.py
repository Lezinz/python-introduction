from .regular_frame import RegularFrame
from .spare_frame import SpareFrame

class Bowling:
    def __init__(self, frame_str: str):
        self.frames = frame_str.strip().split()

    def calculate(self) -> int:
        total = 0
        i = 0
        while i < 10:
            frame = self.frames[i]
            if '/' in frame:
                previous_throw = int(frame[0]) if frame[0] != '-' else 0
                if i + 1 < len(self.frames):
                    next_frame = self.frames[i + 1]
                else:
                    next_frame = frame[2:] if len(frame) > 2 else "0"
                spare = SpareFrame(previous_throw, next_frame)
                total += spare.calculate()
            else:
                regular = RegularFrame(frame)
                total += regular.calculate()
            i += 1
        return total