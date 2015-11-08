import re,pprint

rawString = r'and this ia a\nraw string'    #'and this ia a\\nraw string'


match = re.findall('a', 'abdalkjidsannamdamnad')    #['a', 'a', 'a', 'a', 'a', 'a']



contactInfo = 'Doe, John: 555-1212'
match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)

print(match.group())