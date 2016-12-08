class Node:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.directions = []

    # SETTERS

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_direction(self, direction):
        self.directions.append(direction)

    # GETTERS

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.directions

    def compare(self, compare_to_x, compare_to_y):
        if self.x == compare_to_x and self.y == compare_to_y:
            return True
        else:
            return False
