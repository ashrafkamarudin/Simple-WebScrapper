import sys

class Progress:
    complete = 100
    current = 0

    def __init__(self, complete):
        self.complete = complete

    def cont(self):
        self.current += 1

    def print(self):
        self.progressBar(self.current, self.complete)

    def progressBar(self, current, total, barLength = 20):
        percent = float(current) * 100 / total
        arrow   = '-' * int(percent/100 * barLength - 1) + '>'
        spaces  = ' ' * (barLength - len(arrow))

        print('Progress: [%s%s] %d %% [%d/%d] url processed' % (arrow, spaces, percent, current, total), end='\r')