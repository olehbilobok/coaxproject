import csv


def open_file(file_name, operation):
    return open(file_name, operation)

def get_value(data, max_val=True):
    values = [int(x.split(';')[-1]) for x in data]
    return max(values) if max_val else min(values)

def read(file, max_val=None):

    data = [x[0] for x in csv.reader(file)]
    value = get_value(data, max_val) if max_val != None else 0

    for i, row in enumerate(data, start=1):

        if value != 0 and int(row.split(';')[-1]) == value:
            print(i, row)
        elif value == 0:
            print(i, row)



def add(file, data):
    csv.writer(file, delimiter=';').writerow(data)

def delete(input_data, index):


    data = []

    writer = csv.writer(input_data)
    for i, row in enumerate(csv.reader(input_data), start=1):
        if i == index:
            action = input(f'are you sure you want to delete this row?\n{row[0]}\nyes or no\ntype here: ')
            if action == 'yes':
                continue
        data.append(row)
    writer.writerows(data)


def main():

    # file_name = input('give me file name :)')

    while True:

        action = input('what do you wanna do ?)\ntype here: ')

        if action == 'read':

            file = open_file('films.csv', 'r')

            selection = input('do you need to get movies by rating? yes or no \ntype here: ')

            value = None

            if selection == 'yes':
                value = input('higher or lower?\n type here: ')

                value = True if value == 'higher' else False

            read(file, value)

        elif action == 'add':

            file = open_file('films.csv', 'a')
            data = input('add data \nfor example: name,notes,rating\ntype here:')

            add(file, [x.strip() for x in data.split(',')])

            print('was added successfully!')


        elif action == 'delete':

            file = open_file('films2.csv', 'r+')
            index = int(input('index for delete?\ntype here '))

            delete(file, index)

            print('was deleted successfully!')

        elif action == 'stop':
            break


main()