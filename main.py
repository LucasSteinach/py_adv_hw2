from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
print(contacts_list)
print('\n\n\n')
# TODO 1: выполните пункты 1-3 ДЗ
for contact in contacts_list:
    fullname = ' '.join(contact[:3])
    sep_name = re.findall(r'\w+', fullname)
    for i in range(len(sep_name)):
        contact[i] = sep_name[i]

    pattern = re.compile(r"(\+7|8)[\s\(]*(\d{3})[\s\)-]*(\d{3})-?(\d{2})-?(\d{2})[\(доб[\.\s]*(\d*)\)?")
    if contact[5] != '':
        main_phone = pattern.sub(r'+7(\2)\3-\4-\5', contact[5])
        add_phone = pattern.sub(r'\6', contact[5])
        if len(add_phone) == 0:
            contact[5] = main_phone
        else:
            contact[5] = main_phone + ' доб.' + add_phone


pprint(contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writeows(contacts_list)