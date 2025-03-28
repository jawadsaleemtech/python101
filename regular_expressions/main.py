# meta characters
# + * [] ? {} ^

import re

text = 'abcdefghi'
parser = re.search('a[b-f]*f',text)

print(parser)
print(parser.group())

parser2 = re.search('a[b-f]+f',text)
print(parser)
print(parser2.group())