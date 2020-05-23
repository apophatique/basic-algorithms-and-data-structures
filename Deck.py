class Deck:
    def __init__(self):
        self.items = list()

    def add_first(self, obj):
        self.items.insert(0, obj)

    def add_last(self, obj):
        self.items.append(obj)

    def remove_first(self):
        return self.items.pop(0)

    def remove_last(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
