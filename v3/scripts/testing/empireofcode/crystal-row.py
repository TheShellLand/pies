def check_line(line):
    print(line)
    index = 0
    while index + 1 < len(line):
        _current = line[index]
        if index + 1 < len(line):
            _next = line[index + 1]
        if _current == _next:
            print(_current, _next, 'False')
            return False
        if _current != _next:
            print(_current, _next, 'True')
            index = index + 1
    return True


if __name__ == '__main__':
    #line = ["Z", "X", "Z", "X", "Z", "Z", "X"]
    line = ["Z", "X", "Z"]
    check_line(line)

    # These "asserts" using only for self-checking and not necessary for auto-testing




