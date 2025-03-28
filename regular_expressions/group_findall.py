import re 

silly_string = "the cat is the hat"
pattern = 'the'

match = re.search(pattern, silly_string)
print(match.group())


# find all

match_all = re.findall(pattern, silly_string)
print(match_all)

# finditer

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    print(s)