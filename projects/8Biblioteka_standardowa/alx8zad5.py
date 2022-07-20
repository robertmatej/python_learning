import re

input_file = 'dane\input.txt'
content = ''
postal_codes = []
emails = []

# open file
try:
    with open(input_file, 'r') as reader:
        content = reader.read()

except FileNotFoundError:
    print('File not found')


# find all postal codes + print them
post_codes_pattern = re.compile(r'(?<=\d\d)-(?=\d\d\d)')
for code in post_codes_pattern.finditer(content):
    #print(f'dopasowano: {i.group()}, początek: {i.start()}, koniec: {i.end()}')
    #print(f'znaleziony kod: {content[i.start() - 2 : i.end() + 3]}')
    postal_codes.append(content[code.start() - 2 : code.end() + 3])
print(f'znaleziono {len(postal_codes)} kodów pocztowych')
print(postal_codes)


# find all e-maild + print them
#emails_pattern = re.compile(r'.+@.+\..+\w', flags=re.IGNORECASE)
emails_pattern = re.compile(r'\S+[@].', flags=re.IGNORECASE)
for mail in emails_pattern.finditer(content):
    print(mail)
    emails.append(mail)
print(len(emails))




