#!/usr/bin/python3

import random
import sys

g = int()
h = int()

def gh_gt_0(g, h):
    
    try:
        if (g / h) > 0:
            return '(A) g: {g} h: {h}, g/h > 0'.format(g=g, h=h)
        else:
            return False
    except:
        return print('''Can't divide by {} or {}'''.format(g, h))
    
def hg_dev_gt_0(h, g):
    
    try:
        if (h / g) > 0:
            return '(B) h: {h} g: {g}, h/g > 0'.format(g=g, h=h)
        else:
            return False
    except:
        return print('''Can't divide by {} or {}'''.format(h, g))

def gh_plus_gt_0(g, h):
    
    if (g + h) > 0:
        return '(C) g: {g} h: {h}, g+h > 0'.format(g=g, h=h)
    else:
        return False

def gh_minus_gt_0(g, h):

    if (g - h) > 0:
        return '(D) g: {g} h: {h}, g-h > 0'.format(g=g, h=h)
    else:
        return False
    
def gh_plus_lt_0(g, h):
    
    if (g + h) < 0:
        return '(E) g: {g} h: {h}, g+h < 0'.format(g=g, h=h)
    else:   
        return False
    

def try_everything(g, h):

    if g * h > 0:

        answers = []

        answer = gh_gt_0(g, h)
        if answer:
            answers.append(answer)

        answer = hg_dev_gt_0(h, g)
        if answer:
            answers.append(answer)

        answer = gh_plus_gt_0(g, h)
        if answer:
            answers.append(answer)

        answer = gh_minus_gt_0(g, h)
        if answer:
            answers.append(answer)

        answer = gh_plus_lt_0(g, h)
        if answer:
            answers.append(answer)

        if len(answers) == 4:
            print('\n'.join(answers))
            print()



if __name__ == '__main__':

    results = 1000000

    g_range = range(-10, 10)
    h_range = range(-10, 10)

    for i in range(0, results):
        g = random.choice(g_range)
        h = random.choice(h_range)
        try_everything(g, h)

        if i % 1000 == 0 and i is not 0:
            print('.', end='')
            sys.stdout.flush()

    print('Just tried {} numbers'.format(results))


