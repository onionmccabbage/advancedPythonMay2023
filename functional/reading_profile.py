import pstats
def main():
    '''This will open a profile output and display nicely'''
    p = pstats.Stats('prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()