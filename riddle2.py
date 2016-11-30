import string

KEY = ('ERRORSQUAD')


def content_to_list(data_file_name):
    """Creates string with content from file"""
    content = []
    with open(data_file_name, 'r') as f:
        content = f.read()
    content = content.upper()
    return content


def matrix():
    alpha = list(string.ascii_uppercase)
    a = []
    n = 0
    while n < len(alpha):
        a.append(alpha[n:] + alpha[:n])
        n += 1
    return a
a = matrix()


def decored(text, KEY):
    while len(KEY) < len(text):
        KEY += KEY
    text = text.upper()
    num = len(text)
    i = 0
    j = 0
    while i < num:
        if text[i] == ' ':
            print(' ', end='')
        elif text[i] == '\n':
            print('')
        else:
            kol = a[0].index(KEY[j])
            for n in range(26):
                if a[n][kol] == text[i]:
                    row = n
                    j += 1
                    print(a[row][0], end='')
        i += 1


con = content_to_list('text2.txt')
decored(con, KEY)
