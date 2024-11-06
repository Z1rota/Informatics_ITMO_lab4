import re
import time

with open('test.xml', 'r', encoding='UTF-8') as file:
    xml = file.read()
start=time.perf_counter()
def parse(xml: str) -> dict:
    pattern = re.compile(r'<(\w+)>(.*?)</\1>', re.DOTALL) #проходимся по всему файлу хмл и ищем ключи и содержимое dotall позволяет захватывать символы другой строки
    dict = {}

    for match in pattern.finditer(xml): #находим сами ключи и содержимое
        key = match.group(1) #ключ
        value = match.group(2).strip() #содержимое
        if re.search(r'<\w+>', value): # проверяем является ли содержимое новым ключем
            dict[key] = parse(value)
        else:
            dict[key] = value

    return dict


def print_json(parsed: dict, depth=1):
    first = True # проверяем на первый элемент
    for key in parsed.keys():
        elem = parsed[key]
        if not first:
            print(',') #добавляем запятую перед каждым элементом кроме первого
        first = False
        if isinstance(elem, dict): #проверка на то является ли содержимое ключа ключом
            print('\t' * depth + f'"{key}":' + '{')
            print_json(elem, depth + 1)
            print('\t' * depth + '}', end='')
        else:
            print('\t' * depth + f'"{key}": "{elem}"', end='')
    #перенос строки если уровень не корневой
    if depth > 1:
        print()

parsed_xml = parse(xml)
print('{')
print_json(parsed_xml)
print()
print('}')
end=time.perf_counter()
print((end-start))