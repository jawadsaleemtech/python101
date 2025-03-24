import argparse

parser = argparse.ArgumentParser(description="Example of different actions")

parser.add_argument("--name", action="store", help="Stores a value")
parser.add_argument("--debug", action="store_true", help="Sets debug to True")
parser.add_argument("--no-cache", action="store_false", help="Sets cache to False")
parser.add_argument("--nums", action="append", help="Appends multiple values")
parser.add_argument("-v", "--verbose", action="count", help="Increases verbosity level")

args = parser.parse_args()
print(args)


## OUTPUT

# python script.py --name Alice          # args.name = "Alice"
# python script.py --debug               # args.debug = True
# python script.py --no-cache             # args.cache = False
# python script.py --nums 1 --nums 2      # args.nums = ['1', '2']
# python script.py -v -v -v               # args.verbose = 3
