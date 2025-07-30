#write code here
from .regular_frame import RegularFrame

class Bowling():
    frames: list[RegularFrame]

    def __init__(self, frame: str):
        frame_list = frame.split()

        tempFrame = []
        for frame_text in frame_list:
            tempFrame.append(RegularFrame(frame_text))

        self.frames = tempFrame

    # transformer la chaine de character

    def calculate(self) -> int:
        total = 0
        for frame in self.frames:
            total += frame.calculate()
        return total