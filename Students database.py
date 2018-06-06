""" Task 2: Create a database with students.
    Fields: Фам, Имя, Пол, Лет.
    A script has an opportunity to search and save result to a file"""
import json
from collections import OrderedDict


def open_convert(db):
    """ Open a text file with database
        and group it by 4 elements:
        surname, name, gender, age"""
    with open(db) as f:
        final_entries = []
        temp = []
        for line in f:
            temp.append(line.strip())
            if len(temp) == 4:
                final_entries.append(temp)
                temp = []
    return final_entries


def make_orderdict(entries):
    """ Get entries and convert it to ordered dictionaries.
        It helps to make search"""
    dict_list = []
    for entry in entries:
        dictis = [
            ('Фам', entry[0]),
            ('Имя', entry[1]),
            ('Пол', entry[2]),
            ('Лет', entry[3])
        ]
        dict_list.append(OrderedDict(dictis))

    return dict_list


def searching():
    """ Get a request from user and convert it to dictionary
        with pairs key: value."""
    search = input('Enter your request:\n')
    if search:
        search_list = search.title().split('%')

        try:
            my_search = dict(map(lambda x: x.split('='), search_list))
        except ValueError:
            print('Incorrect request')
        else:
            return my_search


def compare(dict_list, my_search):
    """ Compare search with entries from database"""
    if my_search:
        result = []
        for num, one_entry in enumerate(dict_list):
            count = 0

            for key, val in one_entry.items() & my_search.items():
                count += 1
                if count == len(my_search):
                    print_entry = ' '.join(one_entry.values())
                    print("An entry №{} in database: {}".format(num + 1,
                                                                print_entry))
                    result.append(dict(one_entry))
                    result.append(print_entry)
    else:
        print('Error: No request')
        result = None

    return result


def writing(result):
    """ Offer to save data to txt or json fiile"""
    if result:
        save = ''
        while save not in ['txt', 'json']:
            save = input("Enter a type of saving file [txt/json]:\n")
            if save.lower() == 'txt':
                text = []
                for i in range(1, len(result), 2):
                    text.append(result[i])

                with open('hw9_result.txt', 'w') as txt_f:
                    txt_f.write('\n'.join(text))
            else:
                with open('hw9_result.json', 'w') as js:
                    json_data = []
                    for i in range(0, len(result), 2):
                        json_data.append(result[i])
                    json.dump(json_data, js, ensure_ascii=False)
                    js.close()


def run_programm():
    """ Run script """
    data = 'database.txt'
    print(data)
    database = open_convert(data)
    dict_entries = make_orderdict(database)
    search = searching()
    result = compare(dict_entries, search)
    writing(result)


if __name__ == '__main__':
    run_programm()

"""
try:
    with open('hw9_result.json', 'r') as xx:
        f = json.load(xx)
        print(f)
except:
    print("Can't open a file. No match founded")

"""
