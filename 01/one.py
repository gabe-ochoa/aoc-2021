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
        lines = input_list.splitlines()

        def str2int(string: str):
            return int(string)

        int_lines = map(lambda x: int(x), lines)
        list_lines = list(int_lines)
        output = 0
        while(len(list_lines) > 3):
            first_three_sum = list_lines[0] + list_lines[1] + list_lines[2]
            second_three_sum = list_lines[1] + list_lines[2] + list_lines[3]

            if first_three_sum < second_three_sum:
                output += 1
            list_lines.pop(0)

        return output


if __name__ == '__main__':
    print('Starting Day 1')
    input_file = open('/code/01/input.txt', 'r')
    data = input_file.read()
    input_file.close()
    print(Day01.num_increases(data))
    print(Day01.measurement_windows(data))
