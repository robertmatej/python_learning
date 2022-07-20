import sys

def open_file(path):
    #path ="Dane\excell.csv"

    try:
        file = open(path, "r")

    except FileNotFoundError:
        print("Wrong file name or path")

    else:
        file_lines = file.readlines()
        for count, line in enumerate(file_lines):
            print(count + 1, ':', line, end='')

        file.close()
        #return (count + 1, ':', line)


def console_commands():
#    print(len(sys.argv))

    if len(sys.argv) < 2:
        print("No input path")

    elif len(sys.argv) > 1:
        open_file(sys.argv[1])


console_commands()

