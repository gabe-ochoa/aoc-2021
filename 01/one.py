class Day01():
    def num_increases(input_list: str):
        '''
        Takes an input of numbers and counts the number
        of increases of the ordered list.
        '''
        lines = input_list.splitlines()
        previous = lines.pop(0)
        num = 0
        for i in lines:
            if int(previous) < int(i):
                num += 1
            previous = i
        return num
