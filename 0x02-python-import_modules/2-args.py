#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_count = len(argv)
    if arg_count == 1:
        print("0 arguments.")
    elif arg_count > 1:
        plural = "s" if arg_count > 2 else ""
        print("{:d} argument{:s}:".format(arg_count - 1, plural))
        for i in range(1, arg_count):
            print("{:d}: {:s}".format(i, argv[i]))
