#dynamic imples for both :)

class stack:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        return f"say bye bye to {self.data.pop()}"

    def show(self):
        return [i for i in self.data]

class queue:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        return f"say bye bye to {self.data.pop(0)}"

    def show(self):
        return [i for i in self.data]

