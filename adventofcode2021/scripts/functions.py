from sys import argv


def handle_args(args):
    """
    Used to provide a file name that will hit test or real input and part 1 or 2 of each day.
    If input for part 1 and 2 are identical, the user can provide an additional argument Same.
    """
    try:
        part = int(args[1])
    except:
        part = 0

    try:
        if args[2] == "True":
            test = True
        elif args[2] == "False":
            test = False
        elif args[2] == "Same":
            test = False
            same = 1
    except:
        test = False

    try:
        if args[3] == "Same":
            same = 1
    except:
        pass

    try:
        # If same if already = 1 pass
        if same == 1:
            pass
    except:
        same = part

    if part in [1, 2]:
        if not test:
            input_txt = (
                "../inputs/input_"
                + str(args[0].split(".")[0])
                + "_"
                + str(same)
                + ".txt"
            )
        elif test:
            input_txt = (
                "../inputs/test_"
                + str(args[0].split(".")[0])
                + "_"
                + str(same)
                + ".txt"
            )
    else:
        print("Arg must be either 1 or 2 being the part of the puzzle day.")
    return input_txt, part


if __name__ == "__main__":
    print(handle_args(argv))
