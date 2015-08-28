import re, pprint

def find(mod, regex):
    count = 0
    for list in dir(mod):
        hit = re.findall(regex, list)
        if hit:
            count += 1
            print(hit)

    if count == 0:
        pprint.pprint(dir(mod))


find('os', r'call')