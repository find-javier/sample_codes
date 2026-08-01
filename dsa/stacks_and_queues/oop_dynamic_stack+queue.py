#dynamic imples for both :)

class stack:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        if self.data:
            return f"say bye bye to {self.data.pop()}"

    def show(self):
        return [i for i in self.data]

class queue:
    def __init__(self):
        self.data = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        if self.data:
            return f"say bye bye to {self.data.pop(0)}"

    def show(self):
        return [i for i in self.data]


# ---- Stack tests ----
def test_stack():
    s = stack()
    assert s.show() == []
    s.append(1)
    s.append(2)
    s.append(3)
    assert s.show() == [1, 2, 3]
    result = s.pop()
    assert result == "say bye bye to 3"
    assert s.show() == [1, 2]

    result = s.pop()
    assert result == "say bye bye to 2"
    assert s.show() == [1]

    result = s.pop()
    assert result == "say bye bye to 1"
    assert s.show() == []
    print("stack tests passed")


# ---- Queue tests ----
def test_queue():
    q = queue()
    assert q.show() == []
    q.append("a")
    q.append("b")
    q.append("c")
    assert q.show() == ["a", "b", "c"]
    result = q.pop()
    assert result == "say bye bye to a"
    assert q.show() == ["b", "c"]
    result = q.pop()
    assert result == "say bye bye to b"
    assert q.show() == ["c"]
    result = q.pop()
    assert result == "say bye bye to c"
    assert q.show() == []
    print("queue tests passed")


test_stack()
test_queue()
