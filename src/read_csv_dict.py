# Option 1
import sys
import csv

input_file = sys.argv[1]


def reading(input):
    with open(input, 'r') as f:
        temp_file = csv.DictReader(f)
        keys = temp_file.fieldnames
        output_file = []
        for row in temp_file:
            output_file.append(row)
        for key in keys:
            print(key + ':', output_file[160][key], end=' ')


if __name__ == '__main__':
    reading(input_file)


# Option 2
import sys
import csv

input_file = sys.argv[1]


def reading(input):
    with open(input, 'r') as f:
        temp_file = csv.DictReader(f)
        output_file = []
        for row in temp_file:
            output_file.append(row)
        print(output_file[160])


if __name__ == '__main__':
    reading(input_file)