import csv
import json
import os
from random import randint

def csvrnd(round = 0):
    with open('datarec.csv', 'a+') as csv_rec:
        trio = randint(-15, 31)
        worker = csv.writer(csv_rec, lineterminator= '')
        if round % 3 == 0:
            worker.writerow('\n')
        worker.writerow([str(trio)] + [' '])
        if round < 300:
            return csvrnd(round + 1)
        
def jsondata(keybox):
    def jsonwrite(key, value):
        with open ('datarecord.json', 'a+', encoding= 'utf-8') as json_rec:
            json.dump([{key: value}], json_rec, indent= 2)
        json_rec.close()
    return jsonwrite

def mathdata(numbers, page = 0):
    print(numbers)
    def mathread(*args):
        with open('datarec.csv', 'r') as csv_rec:
            watcher = csv.reader(csv_rec, lineterminator= '')
            for eye in watcher:
                if len(eye) > 1:
                    eye.pop()
                    eye = list(map(int, eye))
                    print(eye)
                    if page % 3 == 0:
                        return numbers(eye)
    return mathread(page + 1)

@jsondata
@mathdata            
def mathline(*argument, line = 0):
    print(f"1. Квадратное уравнение\n: {argument[line][0]}x + {argument[line][1]}x + {argument[line][-1]} = {0}")
    x2 = ''
    disc = argument[line][1] ** 2 - 4 * argument[line][0] * argument[line][-1]
    print("Дискриминант\n:", "D =", argument[line][1] ** 2, "-", 4, "*", argument[line][0], "*", argument[line][2], "\n=", disc)
    if disc > 0:
        x1 = round((-argument[line][1] + disc ** 0.5) / 2 * argument[line][0], 2)
        x2 = round((-argument[line][1] - disc ** 0.5) / 2 * argument[line][0], 2)
    elif disc == 0:
        x1 = round(-argument[line][1] / 2 * argument[line][0], 2)
    else:
        x1 = 'Корней нет'
    print(f"Корни\n: {x1}; {x2}")
    # return mathline(line + 1)


for fi in os.listdir(os.getcwd()):
    if 'datarec' in fi:
        os.remove(fi)

csvrnd()
print("\n2. Файл csv успешно сгенерирован.")