class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(5)
n2 = Number(9)

print(n1 + n2)