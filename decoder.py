ALPHABET = (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))


def content_to_str(data_file_name):
    """Creates string with content from file"""
    content = []
    with open(data_file_name, 'r') as f:
        content = f.read()
    return content


def print_decoded(i, n):
    poz = ALPHABET[n].index(i) + 1
    print(ALPHABET[n][-poz], end='')


def main():
    word = content_to_str('text.txt')
    for i in word:

        if i == '\n':
            print('')
        elif i == " ":
            print(' ', end='')
        elif i in ALPHABET[0]:
            print_decoded(i, 0)
        elif i in ALPHABET[1]:
            print_decoded(i, 1)


if __name__ == '__main__':
    main()
