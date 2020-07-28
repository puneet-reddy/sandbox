import re
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='specify word to search for')
    parser.add_argument('fname', help='specify file to search')
    args = parser.parse_args()

    search_file = open(args.fname)
    line_num = 0 

    for line in search_file.readlines():
        line = line.strip('\n\r')
        line_num += 1
        search_result = re.search(args.word, line, re.M|re.I)
        if search_result:
            print (str(line_num), ': ', line)

if __name__ == '__main__':
    Main()