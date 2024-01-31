# Справочник контактов с 5 функциями
def choose_action(phonebook):  # Начало. Выбор действия
    while True:
        print('1 - Добавить контакт\n2 - Найти контакт\n\
3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        user_choice = int(input('Что вы хотите сделать?\nВаше действие: '))
        print()
        if user_choice == 1:
            add_phone_number(phonebook)
        elif user_choice == 2:
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == 3:
            change_phone_number(phonebook)
        elif user_choice == 4:
            delete_contact(phonebook)
        elif user_choice == 5:
            show_phonebook(phonebook)
        elif user_choice == 0:
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as fileq:
        lines = fileq.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as filee:
        contact_list = []
        for line in filee.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():  # Поиск
    print('По какому полю выполнить поиск?')
    search_field = int(input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n'))
    print()
    search_value = None
    if search_field == 1:
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == 2:
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == 3:
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as filef:
        filef.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):  # Поиск Для изменения файла
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):  # Изменение Контакта
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = int(input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n'))
    if field == 1:
        number_to_change[0] = input('Введите фамилию: ')
    elif field == 2:
        number_to_change[1] = input('Введите имя: ')
    elif field == 3:
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as filea:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            filea.write(line)


def delete_contact(file_name):  # Удаление контакта
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as files:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            files.write(line)
    print("Контакт удалён")


def print_contacts(contact_list: list):  # Печать всех контактов
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)
