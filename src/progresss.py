import sys

class Progress:
    complete = 100
    current = 0

    def __init__(self, complete):
        self.complete = complete

    def cont(self):
        self.current += 1

    def print(self, endSentence = ''):
        self.progressBar(self.current, self.complete, endSentence= endSentence)

    def progressBar(self, current, total, barLength = 20, endSentence = ''):
        percent = float(current) * 100 / total
        arrow   = '-' * int(percent/100 * barLength - 1) + '>'
        spaces  = ' ' * (barLength - len(arrow))

        print('Progress: [%s%s] %d %% [%d/%d] %s' % (arrow, spaces, percent, current, total, endSentence), end='\r')