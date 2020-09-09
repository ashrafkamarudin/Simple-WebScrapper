class Progress:
    complete = 100
    current = 0

    def __init__(self, complete):
        self.complete = complete

    def cont(self):
        self.current += 1

    def print(self, string):
        string = string.replace(":min", str(self.current), 1)
        string = string.replace(":max", str(self.complete), 1)
        print(string)