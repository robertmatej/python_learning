"""
open file witch e-mails, filtrate only proper, unique e-mails and save them to file.
usuwać: duplikaty, te same adresy pisane w wileką i mała literą, białe znaki, błedne adresy (brak@ lub kilka @)

"""
import sys

def clean_emails(input_file, output_file):
    #output as collection
    output = set()

    try:
        with open(input_file, "r") as reader, open(output_file, "w") as writer:
            for mail in reader:
                if mail.count('@') == 1:
                    buf = mail.strip()
                    output.add(buf.lower() + '\n')

            output_l = list(output)
            output_l.sort()
#           another method to add New Line symbol
#            output_l = [line + '\n' for line in output_l]
            print(output_l)
            writer.writelines(output_l)

        print("Is file closed? ", reader.closed)
#        print(output)
    except FileNotFoundError:
        print('Wrong file name or path')

def run_program():
# input path "Dane\emails.txt"
# output path "Dane\emails_output.txt"
    if len(sys.argv) == 3:
        clean_emails(sys.argv[1], sys.argv[2])
    else:
        print("Usage: FUNC input_file output_file")


run_program()