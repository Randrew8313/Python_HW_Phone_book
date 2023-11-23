import os

def show_all_records(file_name):
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = fd.readlines()
        print()
        print('Номер записи, Фамилия, Имя, Отчество, номер телефона')
        print('----------------------------------------------------')
        data = list(zip(range(1,len(data)+1),data))
        for i in data:
            print(*i)

def add_new_record():
    print()
    new_record = []
    new_record.append(input('Введите фамилию: '))
    new_record.append(input('Введите имя: '))
    new_record.append(input('Введите отчество: '))
    new_record.append(input('Введите номер телефона: '))
    return new_record

def add_record_to_File(file_name,new_record):
    output_string = ', '.join(new_record)
    with open(file_name, 'a',encoding='utf-8') as f:
        data = f.writelines(f'{output_string}' + '\n')
    print()
    print('Запись успешно добавлена')
    print()

def remove_record(file_name, id_record):
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()      
        data.pop(int(id_record)-1)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)
    print()
    print('Запись успешно удалена')
    print()

def edit_record(file_name,id_record):
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        new_record = add_new_record()
        output_string = ', '.join(new_record)
        data[int(id_record)-1] = f'{output_string}' + '\n'
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)  
    print()
    print('Запись успешно изменена')
    print()    

def find_record(file_name,record):
    print()
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()  
        search = list(filter(lambda x: x.split(', ') [0] == record, data))
    print('Результаты поиска:')
    print()
    for i in search:
        print(*i)

def main():
    file_name = 'telephonebook.txt'
    flag_exit = True
    while flag_exit:
        print()
        print('------------------------------------------------')
        print('Для работы с программой введите номер меню:')        
        print('1 - просмотр справочника')
        print('2 - добавление новой записи')
        print('3 - удаление записи')
        print('4 - измение записи')
        print('5 - поиск записи')
        print('Для заврешения работы нажмите Enter')
        print()
        answer = input('Сделайте Ваш выбор: ')
        if answer == '1':
            os.system('CLS')
            print('Просмотр справочника')  
            show_all_records(file_name)
        elif answer == '2':
            os.system('CLS')
            print('Добавление новой записи в справочник:')
            new_record = add_new_record()
            add_record_to_File(file_name, new_record)
        elif answer == '3':
            os.system('CLS')
            print('Удаление записи в справочнике.')  
            show_all_records(file_name)
            id_record = input('Введите номер записи, которую следует удалить: ')            
            remove_record(file_name,id_record)
        elif answer == '4':
            os.system('CLS')
            print('Изменение записи в справочнике.')  
            show_all_records(file_name)
            id_record = input('Введите номер записи, которую следует изменить: ')            
            edit_record(file_name,id_record)
        elif answer == '5':
            os.system('CLS')
            record = input('Введите Фамилию для поиска: ')
            find_record(file_name,record)
        else:
            print('Работа программы завершена.')
            flag_exit = False

main()