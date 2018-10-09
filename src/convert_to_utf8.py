import sys


def main():
    print(sys.argv)


if __name__ == '__main__':
    main()


input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
    lines = f.read()

decode_data = lines.decode('ISO-8859-1')

with open(output_file, 'w') as g:
    g.write(decode_data)


