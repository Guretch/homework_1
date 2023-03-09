def read_last(lines_num, file):
    if lines_num > 0:
        with open(file, 'r', encoding='utf-8') as my_file:
            file_lines = my_file.readlines()[-lines_num:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Try again. Please, input positive number of lines')


read_last(5, 'text_2.txt')
