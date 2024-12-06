class Day1Pt2:
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

        count = 0
        for x in self.leftNumbers:
            count_number_of_times_x_in_right_list = self.rightNumbers.count(x)
            self.answer += (x * count_number_of_times_x_in_right_list)
            count += 1
        return self.answer
