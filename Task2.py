from itertools import groupby
def compress_string(s):
    compressed = []

    for char, group in groupby(s):
        count = len(list(group))
        compressed.append((count, int(char)))

    result = ' '.join('({}, {})'.format(count, char) for count, char in compressed)

    print(result)


s = input()
compress_string(s)