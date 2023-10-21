#1.	Напишите программу, которая считывает данные из CSV-файла и выводит суммарное значение определенного столбца.
def a(column_id):
    fileName = "C:\\Users\\prots\\PycharmProjects\\Task1\\PR1\\file.csv"
    desc = open(fileName)
    matrix = list()
    for str in desc:
        columns = str.rsplit(sep=";")
        matrix.append(columns)
    sum = 0
    for l in matrix:
        sum += int(l[column_id])
    return sum

print(a(1))
# %%
#2.	Создайте функцию, которая принимает список чисел и возвращает только уникальные значения из этого списка.
def getSetOfItems(collection):
    return set(collection)

setElements = getSetOfItems((1,2,3,4,4,5,5,1))

print(setElements.__str__())

# %%
#3.	Напишите программу, которая анализирует текстовый файл и выводит самое часто встречающееся слово.
import re
fileName = "C:\\Users\\prots\\PycharmProjects\\Task1\\PR1\\task3"
desc = open(fileName)
dictionary = dict()

current_moda = 0
current_words_with_highest_mode = list()

for str in desc:
    words = re.findall(r'\b\w+\b', str, flags=re.IGNORECASE)
    for w in words:
        currentValue = 0
        if (w in dictionary):
            currentValue = dictionary[w]

        currentValue = currentValue + 1
        dictionary[w] = currentValue

        if (currentValue > current_moda):
            current_moda = currentValue
            current_words_with_highest_mode.clear()
            current_words_with_highest_mode.append(w)

        elif (currentValue == current_moda):
            current_words_with_highest_mode.append(w)

print(f"Мода = {current_moda}\n " + current_words_with_highest_mode.__str__())


# %%
#4.	Создайте функцию, которая принимает два списка чисел и возвращает их пересечение, то есть значения, которые присутствуют в обоих списках.
def a(first_col , second_col):
    intersections = list()
    for i in first_col:
        if(i in second_col):
            intersections.append(i)
    return intersections

print(a([1, 2, 3], (2, 1)).__str__())

# %%
#5.	Напишите программу, которая считывает данные из JSON-файла и выводит информацию на основе определенных фильтров.
import json
import re

def filter(name = "",sex = "",min_age = 0,max_age = 1000):
    result_list = list()
    items = json.load(open("C:\\Users\\prots\\PycharmProjects\\Task1\\PR1\\task5.json"))
    people = items["people"]
    for p in people:
        reg_name = name + r'.*'
        filter_name = re.fullmatch(reg_name, p["name"]) is not None
        filter_age = (min_age <= int(p["age"]) <= max_age)
        filter_sex = (sex == "" or p["sex"] == sex)
        if(filter_name and filter_age and filter_sex):
            result_list.append(p)
    return result_list

print(filter("Anton", "male").__str__())
print(filter(sex = "female").__str__())
print(filter(sex = "male", min_age = 10, max_age= 20).__str__())

# %%
#6.	Реализуйте функцию, которая принимает строку и проверяет, является ли она палиндромом (читается одинаково слева направо и справа налево).
def a(str):
    str = str.lower()
    reversed_str = str[::-1]
    return str == reversed_str

print("12221 - Палиндром? " + a("1221").__str__())
print("122 - Палиндром? " + a("122").__str__())
print("Топот - Палиндром? " + a("Топот").__str__())

# %%
#7.	Напишите функцию, которая принимает список строк и считает частотность каждого слова в этом списке.
def a(collection):
    dictionary = dict()
    for w in collection:
        curValue = 0
        if w in dictionary:
            curValue = dictionary[w]
        curValue += 1
        dictionary[w] = curValue
    return dictionary

print(a(("Коробка", "Ремень", "Коробка", "Ножницы")).__str__())

# %%
#8.	Реализуйте программу, которая считывает данные из Excel-файла и выполняет любую операцию с ячейками и столбцами.
import pandas as pd
data = pd.DataFrame(
    {
        "id" : [1,2,3],
        "name" : ["Ivan", "Pert", "Alex"]
    }
)
data.to_excel('C:\\Users\\prots\\PycharmProjects\\Task1\\PR1\\task10.xlsx')
