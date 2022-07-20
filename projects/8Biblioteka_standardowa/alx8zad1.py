"""
Json database for employees
Name surname date of birth e-amil salary
sae to  jason file, open from json fle, printing employees
"""
import json

class Company_Workers:

    def __init__(self, surname):

        self.surname = surname
        self.database = {}
        self.worker_sheme = ('name', 'date of birth', 'e-amil', 'salary')
        '''
        self.ids = ids
        self.name = name     
        self.email = email
        self.salary = salary
        '''

    def add_entry(self):
        key = input("Type surname: ")
        self.database[key] = self.dictionary_input()


    def dictionary_input(self):
        worker_output = []
        for i in self.worker_sheme:
            worker_output.append(input(f"Type {i}: "))
        return worker_output


    def print_entry(self):
        worker_to_print = input("all or type surname: ")

        if worker_to_print.lower() == 'all':
            for key in self.database:
                print(f'surname: {key} ', end='')
                for i, sheme in enumerate(self.worker_sheme):
                    print(f'{sheme}: {self.database[key][i]}, ', end='')
                print()
        else:
            print_worker = worker_to_print + ', '
            try:
                for i, value in enumerate(self.database[worker_to_print]):
                    print_worker += self.worker_sheme[i] + ': ' + value + ', '
                print(f"surname: {print_worker}")

            except KeyError:
                print("Wrong surname, person not in base")


    def write_to_json(self):
        try:
            with open('json_workers2.json', encoding='utf-8', mode='w') as file:

                json.dump(self.database, file, indent=1, sort_keys=True)
                print("Successfully saved to file")

        except FileNotFoundError:
            print("Save to file Error")

    def open_from_json(self):
        try:
            with open('json_workers.json', 'r') as file:
                self.database = json.load(file)
                print("Successfully load data")

        except FileNotFoundError:
            print('Wrong input file')

        except json.decoder.JSONDecodeError:
            print("wrong data in file, can't load")


    def main_loop(self):
        loop = ''
        while loop != 'q':
            loop = input('Type: q - quit, a - add new worker, p - print data, f - save to file, l - load from file\n')
            if loop == 'a':
                self.add_entry()

            if loop == 'p':
                self.print_entry()

            if loop == 'f':
                self.write_to_json()

            if loop == 'l':
                self.open_from_json()

            if loop == 'q':
                print("Exit Program")


kfc = Company_Workers('')
kfc.main_loop()


