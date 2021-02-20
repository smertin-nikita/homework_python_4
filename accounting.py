documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_documents(number):
    """ Возращет список документов """
    return list(filter(lambda x: x['number'] == number, documents))


def print_people(number):
    """ Возвращает все имена с нормером паспорта = number """
    return [item['name'] for item in get_documents(number)]


def get_shelfs(number):
    """ Возращет все номера полок которые содержат number документа """
    return [key for key, value in directories.items() if number in value]


def get_all_documents():
    """  Возвращает все докумены """
    return [item.values() for item in documents]


def add_document(type_doc, number, name, shelf_num):
    """ Добавляет новый документ. Возращет True если документ добавился """
    if shelf_num in directories:
        documents.append({"type": type_doc, "number": number, "name": name})
        directories[shelf_num].append(number)
        return True
    else:
        return False


def del_documents(number):
    """ Удоляет документы с number. Возращет True если документы удалились """
    if len(get_documents(number)):
        for item in get_documents(number):
            documents.remove(item)
        for item in get_shelfs(number):
            directories[item].remove(number)
        return True
    else:
        return False


def move_document(number, shelf_num):
    """ Перемещает документы с number на другую полку. Возращет True если документы переместились """
    if (shelf_num in directories) and len(get_documents(number)):
        for item in get_shelfs(number):
            directories[item].remove(number)
        directories[shelf_num].append(number)
        return True
    else:
        return False


def add_shelf(shelf_num):
    """ Создает новую полку с number . Возращет True если полка создана """
    if shelf_num not in directories:
        directories[shelf_num] = []
        return True
    else:
        return False


commands = {
    'p': (print_people, ['10006']),
    's': (get_shelfs, ['1']),
    'l': (get_all_documents, []),
    'a': (add_document, ['passport', '1', 'Иван Петров', '3']),
    'd': (del_documents, ['1']),
    'm': (move_document, ['11-2', '3']),
    'as': (add_shelf, ['3'])
}


def test():
    for command, args in commands.values():
        print(command.__doc__)
        print(command(*args))
        print('------------ Докумены -----------')
        get_all_documents()
        print('------------- Полки -------------')
        print(directories)
        print('-------------------------------')


def user_interface():
    while True:
        print()
        print('Введите команду: help, p, s, l, a, d, m, as')
        command = input()
        if command == 'p':
            print('Введите номер документа!')
            print_people(input())

        elif command == 's':
            print('Введите номер документа!')
            print(get_shelfs(input()))

        elif command == 'l':
            get_all_documents()

        elif command == 'a':
            print('Введите номер документа!')
            number = input()
            print('Введите тип документа!')
            type_doc = input()
            print('Введите имя!')
            name = input()
            print('Введите номер полки!')
            shelf_num = input()

            if not add_document(type_doc, number, name, shelf_num):
                print(f'Полки {shelf_num} нет!')

        elif command == 'd':
            print('Введите номер документа!')
            if not del_documents(input()):
                print('Документов с таким номером не существует')

        elif command == 'm':
            print('Введите номер документа!')
            number = input()
            print('Введите номер полки!')
            shelf_num = input()
            if not move_document(number, shelf_num):
                print(f'Полки {shelf_num} нет!')
                print(f'Или документа {number} не существует!')

        elif command == 'as':
            print('Введите номер полки!')
            shelf_num = input()
            if not add_shelf(shelf_num):
                print(f'Полка {shelf_num} уже существует!')

        elif command == 'help':
            for command, func in commands.items():
                print(f'{command}: {func[0].__doc__}')

        else:
            print('Неверная команда!')
            print('Выполнен выход.')
            break


if __name__ == '__main__':
    test()
# user_interface()
