import time
xml=''
i=0
start = time.perf_counter()
xml = open('test.xml' ,'r',encoding='UTF-8').readlines()[1:]
def checkingForOpen(stroka: str) -> str:
    stroka=stroka.strip()
    if stroka.find('</') != -1:
        return ''
    return stroka[1:-1]

def checkingForClose(name: str, stroka: str) ->bool:
    return f'</{name}>' == stroka.strip()

def getElem(stroka: str) -> tuple[str, str]:
    stroka = stroka.strip()
    elemName= stroka[1:stroka.find('>')]
    value = stroka[stroka.find('>')+1:len(stroka)-(len(elemName)+3)]
    return (elemName,value)

def parse(branchName: str) -> dict:
    global i
    diction = dict()
    tempstr = xml[i].replace('\n','')
    while not checkingForClose(branchName,tempstr):
        if i >= len(xml):
            break
        newBranchName = checkingForOpen(tempstr)
        if newBranchName != '':
            i+=1
            diction[newBranchName] = parse(newBranchName)
        else:
            key,value =getElem(xml[i])
            diction[key] =value
            i+=1
        if i >= len(xml):
            break
        tempstr = xml[i].replace('\n', '')
    i+=1

    return diction

parsedxml = parse('')

def printJson(parsed: dict, depth=1):
    first = True  # Флаг для отслеживания первого элемента
    for key in parsed.keys():
        elem = parsed[key]
        if not first:
            print(',')  # Добавляем запятую перед каждым элементом, кроме первого
        first = False  # Устанавливаем флаг в False после первого элемента
        if isinstance(elem, dict):
            print('\t' * depth + f'"{key}":' +'{')
            printJson(elem, depth + 1)
            print('\t' * depth + '}', end='')  # Закрывающая скобка на том же уровне
        else:
            print('\t' * depth + f'"{key}": "{elem}"', end='')  # Убираем запятую здесь

    # Если это не корневой уровень, добавляем перенос строки
    if depth > 1:
        print()
print('{')
printJson(parsedxml)
print()
print('}')
print((time.perf_counter()-start))












