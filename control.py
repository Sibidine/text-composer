from compose import compose
from parser import parse
import sys
import os

def main():
    filename = sys.argv[-1]
    user_file = parse(filename)
    compose(user_file)
    os.remove(user_file)

main()

