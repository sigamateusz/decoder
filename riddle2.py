import string


def content_to_list(data_file_name):
    """Creates string with content from file"""
    with open(data_file_name, 'r') as f:
        content = f.read().upper()
    return content


def matrix():
    """Creates list with lists of alphabet"""
    alpha = list(string.ascii_uppercase)
    matrix = []
    n = 0
    while n < len(alpha):
        matrix.append(alpha[n:] + alpha[:n])
        n += 1
    return matrix


def decoded(text, KEY, alphabet):
    while len(KEY) < len(text):
        KEY += KEY
    num = len(text)
    i = 0
    j = 0
    while i < num:
        if not text[i].isalpha():
            print(text[i], end='')
        else:
            kol = alphabet[0].index(KEY[j])
            for n in range(26):
                if alphabet[n][kol] == text[i]:
                    row = n
                    j += 1
                    print(alphabet[row][0], end='')
        i += 1


def main():
    KEY = ('ERRORSQUAD')
    alphabet = matrix()
    content = content_to_list('text2.txt')
    decoded(content, KEY, alphabet)


if __name__ == '__main__':
    main()
