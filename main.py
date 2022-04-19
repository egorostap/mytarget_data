import json
import pandas as pd
from datetime import datetime

# # читаем страницу txt
# with open('txt.txt') as f:
#     data = f.read()
# # print(data)
#
# # превращает строки в словарь
# data = eval(data)
# # print(data)
#
# # запись в json
# with open('mt_zapros.json', 'w') as f:
#     json.dump(data, f)

# чтение json
with open('mt_zapros.json') as f:
    data = json.load(f)
# print(type(data))

#Получаем по ключу итемс данные из json
data = data['items']
print(data)

#Создаем пустой dict (словать данных) и счетчик
dict_data = {}
count = 0

#Парсим исходный list формата Json в dictionary (словарь данных)
for i in data:
    # print(i)
    for row in i['rows']:
        # print(row)
        dict_data[count] = {
            'id': i["id"],
            'date': row["date"],
            'shows': row["base"]["shows"],
            'clicks': row["base"]["clicks"],
            'goals': row["base"]["goals"],
            'spent': float(row["base"]["spent"]),
            'cpm': float(row["base"]["cpm"]),
            'cpc': float(row["base"]["cpc"]),
            'cpa': float(row["base"]["cpa"]),
            'ctr': row["base"]["ctr"],
            'cr': row["base"]["cr"],
          }
        count += 1

# print(dict_data)

#Создаем DataFrame из dict (словаря данных или массива данных)
dict_keys = dict_data[0].keys()
df = pd.DataFrame.from_dict(dict_data, orient='index',columns=dict_keys)


# Выгрузка данных из DataFrame в Excel
df.to_excel("traf_mt.xlsx", sheet_name='data', index=False)

print('файл сформирован')
