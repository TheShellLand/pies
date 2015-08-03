import os, subprocess




def interfaces():
    iwconfig = subprocess.call('iwconfig')

def ifconfig_manage(device, state):
    ifconfig = subprocess.call(['ifconfig', device, state])

def macchanger(device):
    macchanger = subprocess.call(['macchanger', '-a', device])

def airodump(device, opt):
    airodump = subprocess.call(['airodump-ng', device, opt])


def main():
    interfaces()

if __name__ == "__main__":
    main()