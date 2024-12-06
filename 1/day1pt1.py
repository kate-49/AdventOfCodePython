class Day1:
    def __init__(self, file_to_open):
        self.leftNumbers = []
        self.rightNumbers = []
        self.answer = 0
        f = open(file_to_open, 'r')
        self.content = f.read().split('\n')
        f.close()

    def calculate(self):
        for line in self.content:
            splitLine = line.split(' ')
            self.leftNumbers.append(int(splitLine[0]))
            self.rightNumbers.append(int(splitLine.pop()))

        self.leftNumbers.sort()
        self.rightNumbers.sort()

        count = 0
        for x in self.leftNumbers:
            diff = abs(x - self.rightNumbers[count])
            self.answer += diff
            count += 1
        return self.answer
