def createDict(dictionary: dict, filePath: str):  # функция создания глоссария
    with open(filePath, "r", encoding="utf-8") as file:
        while True:
            fileLine = file.readline()

            if fileLine == '':
                break
            else:
                fileLine = fileLine.split(':', 1)

            dictionary[fileLine[0]] = fileLine[1].rstrip('\n').lstrip(' ')
    print("Глоссарий создан!")


def dictToText(dictionary: dict):  # функция перевода глосария в текстовую форму (для функции ниже)
    textList = list()

    for key in dictionary:
        textList.append(key + ': ' + dictionary[key] + '\n')

    text = str()
    for line in textList:
        text += line

    text = text.rstrip('\n')
    return text


def saveDict(dictionary: dict, filePath: str):  # функция для сохранения глоссария в файл
    saveMethod = int(input("Сохранить в теукщий файл (1) или в новый файл(2)? > "))
    if saveMethod == 1:

        check = input("Вы уверены? Введите один из ключей глоссария для подтверждения > ")

        if check in dictionary:
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(dictToText(dictionary))  # здесь нужна функция сверху!
                print("Файл перезаписан!")

        else:
            return "Ключа нет в глоссарии! Отмена команды"
        
    elif saveMethod == 2:

        newFile = input("Введите название нового файла (без расширения) > ") + '.txt'

        with open(newFile, "w", encoding="utf-8") as file:
                file.write(dictToText(dictionary))  # и тут!
                print("Файл создан!")
    
    else:
        print("Неправильный выбор! Отмена команды")


def appendDictElem(dictionary: dict):  # функция для добавления и изменения терминов
    key = input("Введите термин > ")
    text = input("Введите толкование термина > ")

    if key in dictionary:
        choice = input("Термин есть в глоссарии! Перезаписать его толкование?(1 - Да, остальное - нет) > ")
        if choice == '1':
            dictionary[key] = text
            print("Перезаписано!")
        else:
            return "Возращаемся в меню..."
        
    else:
        dictionary[key] = text
        print("Добавлено!")


def deleteDictElem(dictionary: dict):  # функция удаления термина
    key = input("Введите термин, который вы хотите удалить > ")

    if key in dictionary:

        choice = input("Удалить термин?(1 - Да, остальное - нет) > ")
        if choice == '1':
            del dictionary[key]
            print("Термин удалён")
        else:
            return "Возращаемся в меню..."
        
    else:
        print("Термина нет в глоссарии!")


def showDict(dictionary: dict):  # функция, чтобы показать весь глоссарий
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")


def showDictElem(dictionary: dict):  # функция, чтобы показать толкование одного термина (с форматированием!)
    print(f"Термины: ")
    for keys in dictionary:
        print(f">{keys}")
    
    print()
    search = input("Введите термин, толкование которого вы хотите вывести > ")
    print()

    text: str = dictionary.get(search, 'Такого термина нет!')
    text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '\"')  # без этого форматирование не работает

    print(text)


def changePath(currentPath: str):  # функция изменения файла на другой (полезно!)
    newPath = input('Введит название (без расширения) файла, на которое вы хотите поменять текущий > ') + '.txt'

    try:
        f = open(newPath)
        f.close()
        return newPath

    except FileNotFoundError:
        print("Данного файла нет в директории! Возращаемся в меню")
        return currentPath
    

def showMenu():  # функция показа меню
    print("------------------------Меню------------------------")
    print("1 - Создать глосарий на основе текстового файла")
    print("2 - Поменять текущий файл")
    print("3 - Сохранение глоссария в файл")
    print("4 - Добавить в глоссарий: термин: толкование термина")
    print("5 - Удалить из глоссария: термин: толкование термина")
    print("6 - Вывести глоссарий")
    print("7 - Вывод толкования термина (с форматированием)")
    print("8 - Показать меню ещё раз")
    print("Любая другая цифра закрывает программу")


def main():
    mainDict = dict()
    mainPath = 'dict.txt'
    commandDict = {  # глоссарий функций!
        1 : createDict,
        2 : changePath,
        3 : saveDict,
        4 : appendDictElem,
        5 : deleteDictElem,
        6 : showDict,
        7 : showDictElem,
        8 : showMenu
    }

    showMenu()

    while True:
        choice = int(input(f"Текущий файл: {mainPath}. Введите команду > "))
        if choice in commandDict:
            if choice == 2:
                mainPath = commandDict[choice](mainPath)
            elif choice == 1:
                commandDict[choice](mainDict, mainPath)
            elif choice == 8:
                showMenu()
            elif mainDict == {}:
                print("Отсутствует глоссарий!")
            else:
                if choice == 3:
                    commandDict[choice](mainDict, mainPath)
                elif 4 <= choice <= 7:
                    commandDict[choice](mainDict)
        else:
            break
            
        
main()
