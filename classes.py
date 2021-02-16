

class Keypoint:
    def __init__(self, x, y, c):
        self.x = round(x)  # x position
        self.y = round(y)  # y position
        self.c = c  # confidence


class Mouth:
    def __init__(self, left, right, top, bot, width, height, relation):
        self.left = left
        self.right = right
        self.top = top
        self.bot = bot
        self.width = width
        self.height = height
        self.relation = relation

class Eye:
    def __init__(self, left, right, top, bot, width, height):
        self.left = left
        self.right = right
        self.top = top
        self.bot = bot
        self.width = width
        self.height = height