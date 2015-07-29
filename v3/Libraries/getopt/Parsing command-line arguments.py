import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for opts, args in opts:
        if opts == "-v":
            verbose = True
        elif opts in ("-h", "--help"):
            usage()
            sys.exit()
        elif opts in ("-o", "--output"):
            output = args
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()