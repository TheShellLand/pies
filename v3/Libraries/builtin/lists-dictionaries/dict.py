>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
>>> print stuff['name']
Zed
>>> print stuff['age']
39
>>> print stuff['height']
74
>>> stuff['city'] = "San Francisco"
>>> print stuff['city']
San Francisco







>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}

>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}







In [1]: import json

In [2]: s = """\
   ...: {
   ...:   "A": {
   ...:     "B": {
   ...:       "unknown": {
   ...:         "1": "F",
   ...:         "maindata": [
   ...:           {
   ...:             "Info": "TEXT"
   ...:           }
   ...:         ]
   ...:       }
   ...:     }
   ...:   }
   ...: }"""

In [3]: data = json.loads(s)

In [4]: data['A']['B']['unknown']['maindata'][0]['Info']
Out[4]: u'TEXT'




dict((el,0) for el in a)
{el:0 for el in a}


