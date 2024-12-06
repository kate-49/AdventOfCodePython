from array import array


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
            print("line")
            print(line)
            array_of_line = line.split()

            diff_of_more_than_3 = self.check_if_diff_of_more_than_3(array_of_line)
            print("diff")
            print(diff_of_more_than_3)
            some_increasing_and_some_decrease = self.check_if_all_increasing_or_decreasing(array_of_line)
            print("increase")
            print(some_increasing_and_some_decrease)

            if not diff_of_more_than_3:
                if not some_increasing_and_some_decrease:
                    print("increasing answer")
                    print(array_of_line)
                    self.answer = self.answer + 1

        print("final answer")
        print(self.answer)
        return self.answer

    def check_if_diff_of_more_than_3(self, array_of_line):
        diff_of_more_than_3 = False
        count = 0
        while count < len(array_of_line) - 1:
            # print("count")
            # print(array_of_line[count])
            diff = abs(int(array_of_line[count]) - int(array_of_line[count + 1]))
            if diff > 3:
                print("diff is more than 3 at count")
                print(count)
                print(array_of_line[count])
                diff_of_more_than_3 = True
            if diff == 0:
                diff_of_more_than_3 = True
            count = count + 1
        return diff_of_more_than_3

    def check_if_all_increasing_or_decreasing(self, array_of_line):
        increasing = False
        decreasing = False
        some_increase_and_some_decrease = False

        count = 0

        while count < len(array_of_line) - 1:
            # print("count")
            # print(count)
            if array_of_line[count] < array_of_line[count + 1]:
                if count == 0:
                    increasing = True
                if count >= 1 & increasing == False:
                    print("should not access here")
                    some_increase_and_some_decrease = True
            elif array_of_line[count] > array_of_line[count + 1]:
                if count == 0:
                    decreasing = True
                if count >= 1 & decreasing == False:
                    print("should not access here")
                    some_increase_and_some_decrease = True
            count = count + 1

        return some_increase_and_some_decrease