import pip

def install(package):
    pip.main(['install', package])

def uninstall(package):
    pip.main(['uninstall', package])

def main():
    package = input('Type in a package: ')
    action = input('[Install]/Uninstall:')

if __name__ == '__main__':
    main()