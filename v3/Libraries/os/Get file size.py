import os
from pprint import pprint


def print_size_of(file):
    fsize = os.path.getsize(file)
    pprint(fsize)


def main():
    print_size_of(imput)


if __name__ == "__main__":
    main()