
def file_open(input_file):
    output_file = 'Dane\itanic_wynik.txt'
    i = 0
    try:
        with open(input_file, 'r') as input, open (output_file, 'a') as output:
            for line in input:

                passengerid, survived, pclass, name, surname, sex, age, sibsp, parch, ticket, fare, cabin, embarked = line.split(',')
                #print(name)
                #print(age)
                if survived == "0" and sex == 'female'and pclass == '1' :
                    i += 1
                    print(i, name, surname)
                    output.writelines([str(i), name, surname])


    except FileNotFoundError:
        print('Wrong file name or path')


#returns
file_open('Dane\Titanic_Train.csv')
