def handle_args(args):
    try :
        part = int(args[1])
    except : 
        part = 0
    try :
        test = bool(args[2])
    except : 
        test = False
    if part in [1,2] : 
        if not test : 
            input_txt = '../inputs/input_' + str(args[0].split('.')[0]) + '_' + str(args[1]) + '.txt'
        else :
            input_txt = '../inputs/test_' + str(args[0].split('.')[0]) + '_' + str(args[1]) + '.txt'
    else :
        print('Arg must be either 1 or 2 being the part of the puzzle day.')
    return input_txt, part