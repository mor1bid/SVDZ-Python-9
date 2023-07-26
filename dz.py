import csv
import os
from random import randint

def csvrnd(round = 0):
    with open('datarec.csv', 'a+') as csv_rec:
        trio = randint(-100, 1000)
        # print(trio)
        worker = csv.writer(csv_rec)
        if round % 3 == 0:
            worker.writerow(' ')
        worker.writerow([str(trio)] + [' '])
        if round != 100:
            return csvrnd(round + 1)

for fi in os.getcwd():
    if 'datarec' in fi:
        os.remove(fi)
csvrnd()
print("\n2. Файл csv успешно сгенерирован.")