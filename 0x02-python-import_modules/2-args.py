#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print("{:d} arguments.".format(num_args))
else:
    print("{:d} argument{}:".format(num_args, 's' if num_args > 1 else ''))
    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, argv[i]))
