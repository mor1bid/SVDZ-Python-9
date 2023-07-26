import csv
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

def mathdata():
    with open('datarec.csv', 'r') as csv_eye:
        abc = list()
        worker = csv.reader(csv_eye, lineterminator= '')
        for i in worker:
            print(i)
            if str(i).isdigit():
                numbr = int(i)
                if numbr % 3 != 0:
                    abc.append(i)
                else:
                    print(abc)
                    abc = list()
@mathdata            
def mathline(*args):
    x2 = ''
    disc = args[1] ** 2 - 4 * args[0] * args[2]
    print("Дискриминант\n:", "D =", args[1] ** 2, "-", 4, "*", args[0], "*", args[2], "\n=", disc)
    if disc > 0:
        x1 = round((-args[1] + disc ** 0.5) / 2 * args[0], 2)
        x2 = round((-args[1] - disc ** 0.5) / 2 * args[0], 2)
    elif disc == 0:
        x1 = round(-args[1] / 2 * args[0], 2)
    else:
        x1 = 'Корней нет'
    print(f"Корни\n: {x1}; {x2}")

for fi in os.listdir(os.getcwd()):
    if 'datarec' in fi:
        os.remove(fi)
# a = randint(-10, 11)
# b = randint(-20, 21)
# c = randint(-20, 41)
# print(f"1. Квадратное уравнение\n: {a}x + {b}x + {c} = {0}")
# mathline(a, b, c)

csvrnd()
print("\n2. Файл csv успешно сгенерирован.")
mathdata()