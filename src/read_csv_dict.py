import sys
import csv


def main():
    pass
    # print(sys.argv)


if __name__ == '__main__':
    main()


input_file = sys.argv[1]

with open(input_file, 'r') as f:
    output_file = csv.DictReader(f, delimiter=',')
    line_count = 0
    for row in output_file:
        if line_count == 162:
            print(row)
            line_count += 1
        else:
            line_count += 1
