ALPHABET = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']]


def content_to_str(data_file_name):
    """Creates string with content from file"""
    content = []
    with open(data_file_name, 'r') as f:
        content = f.read()
    return content


def main():
    word = content_to_str('text.txt')
    for i in word:

        if i == '\n':
            print('')
        elif i == " ":
            print(' ', end='')
        elif i in ALPHABET[0]:
                poz = ALPHABET[0].index(i) + 1
                print(ALPHABET[0][-poz], end='')
        elif i in ALPHABET[1]:
                poz = ALPHABET[1].index(i) + 1
                print(ALPHABET[1][-poz], end='')


if __name__ == '__main__':
    main()
