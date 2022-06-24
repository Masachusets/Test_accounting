documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def name_by_doc(docnumber):
    for doc in documents:
        if docnumber == doc['number']:
            return doc['name']
    return 'Документа с таким номером у нас нет!'


def shelf_by_doc(docnumber):
    for shelf, docs in directories.items():
        if docnumber in docs:
            return shelf
    return 'Документа с таким номером у нас нет!'


def doclist():
    alldocs = []
    for doc in documents:
        alldocs.append(', '.join(doc.values()))
    return alldocs


def add_doc(docnumber, type, owner, shelf):
    for docs in directories.values():
        if docnumber in docs:
            return 'Документ с таким номером уже существует'
    if shelf in directories:
        documents.append({"type": type, "number": docnumber, "name": owner})
        directories[shelf].append(docnumber)
        return f'Документ {type} с номером {docnumber} добавлен на полку {shelf}'
    else:
        return 'Полки с таким номером у нас нет!'


def del_doc(docnumber):
    for doc in documents:
        if docnumber == doc['number']:
            documents.remove(doc)
            break
    else:
        return 'Документа с таким номером у нас нет!'
    for shelf, docs in directories.items():
        if docnumber in docs:
            directories[shelf].remove(docnumber)
    return 'Документ удалён!'


def move_doc(docnumber, shelf):
    if shelf in directories:
        for docs in directories.values():
            if docnumber in docs:
                docs.remove(docnumber)
                directories[shelf].append(docnumber)
                return f'Документ {docnumber} перемещён на полку {shelf}'
        return 'Документа с таким номером у нас нет!'
    else:
        return 'Полки с таким номером у нас нет!'


def add_shelf(shelf):
    if shelf not in directories:
        directories[shelf] = []
        return f'Полка {shelf} добавлена, теперь на неё можно что-нибудь положить'
    else:
        return 'Полка с таким номером уже есть!'


def main(documents, directories):
    '''
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
    '''
    while True:
        comand = input('Введите команду: ')
        if comand == 'p':
            print(name_by_doc(input('Введите номер документа: ')))
        elif comand == 's':
            print(shelf_by_doc(input('Введите номер документа: ')))
        elif comand == 'l':
            print(*doclist(), sep='\n')
        elif comand == 'a':
            print(add_doc(input('Введите номер документа: '),
                          input('Введите тип документа: '),
                          input('Введите имя владельца документа: '),
                          input('Введите номер полки для документа: ')))
        elif comand == 'd':
            print(del_doc(input('Введите номер документа: ')))
        elif comand == 'm':
            print(move_doc(input('Введите номер документа: '),
                           input('Введите номер полки для документа: ')))
        elif comand == 'as':
            print(add_shelf(input('Введите номер новой полки: ')))
        elif comand == 'q':
            break


# main(documents, directories)
FIXTURE = [('1', 'Документа с таким номером у нас нет!')] \
          + [(doc, shelf) for shelf, docs in directories.items() for doc in docs]
print(FIXTURE)