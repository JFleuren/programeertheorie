class Path:
    def __init__(self):
        self.list = []

    def append_child(self, child):
        self.list.append(child)

    def calculate_path_length(self):
        return len(self.list)
