import os

#path = print(os.getcwd())

#print(os.get_exec_path())

#print(os.listdir(path='.'))

#for i in os.scandir(path='..'):
#    print(i)
count = 0
for root, dirs, files in os.walk('..'):
    count += 1
    tab = "  "
    for i in dirs:
        print(tab * count + i)

        print(tab * count + '|')
    print(tab * count + '---')
    for j in files:
        print(tab * count + j)

#    print(root)
#    print(dirs)
#    print(files)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")