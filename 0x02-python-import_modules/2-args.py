#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arg = (len(sys.argv) - 1)
if arg == 0:
    print("{} arguments".format(0))
elif arg == 1:
    print("{} argument:".format(arg))
    for i in range(arg):
        i = i + 1
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("{} arguments:".format(arg))
    for i in range(arg):
        i = i + 1
        print("{}: {}".format(i, sys.argv[i]))
