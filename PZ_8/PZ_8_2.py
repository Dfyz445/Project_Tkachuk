"""
Организовать словарь avto, содержащий 3 ключа (марки авто)
и списки из трех моделей в качестве значений.
Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.
"""
avto = {'reno': ['logan','daster','sanderro'],
        'lada': ['largus','vesta','granta'],
        'porshe': [911, 'targa','carrera']}
for k, v in avto.items():
    print(k, v[1])