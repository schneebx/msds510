import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def convert(input, output):
    with open(input, 'rb') as f:
        lines = f.read()
    decode_data = lines.decode('ISO-8859-1')
    with open(output, 'w') as g:
        g.write(decode_data)


if __name__ == '__main__':
    convert(input_file, output_file)