import string

KEY = ('ERRORSQUAD')


def content_to_list(data_file_name):
    """Creates string with content from file"""
    with open(data_file_name, 'r') as f:
        content = f.read().upper()
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


def decoded(text, KEY):
    while len(KEY) < len(text):
        KEY += KEY
    num = len(text)
    i = 0
    j = 0
    while i < num:
        if not text[i].isalpha():
            print(text[i], end='')
        else:
            kol = a[0].index(KEY[j])
            for n in range(26):
                if a[n][kol] == text[i]:
                    row = n
                    j += 1
                    print(a[row][0], end='')
        i += 1


con = content_to_list('text2.txt')
decoded(con, KEY)
