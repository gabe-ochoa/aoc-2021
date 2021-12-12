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

    def measurement_windows(input_list: str):
        '''
        Sum batches of 3 measurements and put them in a 
        list

        return batches: list[str]
        '''
        


if __name__ == '__main__':
    print('Starting Day 1')
    input_file = open('/code/01/input.txt', 'r')
    data = input_file.read()
    input_file.close()
    print(Day01.num_increases(data))
