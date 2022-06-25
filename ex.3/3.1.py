class LeftParagraph:
    def __init__(self, num=int()):
        self.num = num
        self.counter = []
    def add_word(self, strr=str()):
        if len(self.counter) == 0 or len(strr + self.counter[-1]) >= self.num:
            self.counter.append(strr)
        else:
            self.counter[-1] = self.counter[-1] + ' ' + str(strr)
    def end(self):
        for i in self.counter:
            print(i)

class RightParagraph:
    def __init__(self, num=int()):
        self.num = num
        self.counter = []
    def add_word(self, strr=str()):
        if len(self.counter) == 0 or len(strr + (self.counter[-1]).lstrip()) >= self.num:
            self.counter.append(strr.rjust(self.num, ' '))
        else:
            self.counter[-1] = (self.counter[-1].lstrip() + ' ' + str(strr)).rjust(self.num, ' ')
    def end(self):
        for i in self.counter:
            print(i)
