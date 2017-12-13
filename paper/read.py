import csv


def read_csv(file: str) -> list:
    l = []
    f = open(file, encoding='utf-8-sig', mode='r')
    data = csv.reader(f)
    for row in data:
        l.append(row)

    return l
