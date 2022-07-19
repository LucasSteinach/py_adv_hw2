from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
# pprint(contacts_list)
# print('\n\n\n')
# TODO 1: выполните пункты 1-3 ДЗ
string_list = [" ".join(i) for i in contacts_list]
# pprint(string_list)
new_list =  []
people_dict = dict()
for item in string_list[1:]:
    # extract str 'Lastname Name Surname'
    fullname = re.findall(r'[а-яёА-ЯЁ\s]+[^a-zA-Z ]', re.split(r'ФНС|Минфин', item)[0])
    if fullname[0] not in people_dict.keys():
        people_dict[fullname[0]] = []
print(people_dict)
    # fills first 3 position
    # new_list.append([i for i in fullname[0].split(' ')[:3] ])
print(new_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writeows(contacts_list)