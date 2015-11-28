import pip
from subprocess import call


def install(package):
    print('Installing... ' + package)
    pip.main(['install', package])

def uninstall(package):
    print('Uninstalling... ' + package)
    pip.main(['uninstall', package])

def upgrade():
    print('Upgrading... pip')
    call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])


def main():
    while True:
        package = input('Type in a package: ')
        #print('length: ' + len(package).__str__())
        if len(package) > 0:
            break

    while True:
        print('1. Install\n' + '2. Uninstall\n' + '\n' + '3. Upgarde pip')
        action = input('Choose an option: ').__str__()
        #print('length: ' + len(action).__str__())

        if len(action) == 0:
            pass

        elif int(action) == 1:
            try:
                install(package)
            finally:
                break

        elif int(action) == 2:
            try:
                uninstall(package)
            finally:
                break

        elif int(action) == 3:
            try:
                upgrade()
            finally:
                break



if __name__ == '__main__':
    main()