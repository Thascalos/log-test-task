#!/usr/bin/env python3
#tested on Python 3.5.3
import collections
import sys


def log_parser(file):
    # Парсим лог и добавляем в список
    log = []
    for line in file:
        split_line = line.split()
        log.append((split_line[0], int(split_line[9])))
    return log


def main():
    if not len(sys.argv) > 1:
        print("You must specify logfile")
        sys.exit(1)

    file = sys.argv[1]
    c = collections.Counter()

    try:
        file = open(file, 'r')
    except IOError:
        print("Can't open file")
        sys.exit(1)

    log = log_parser(file)
    # В цикле суммируем трафик
    for k, v in log:
        c[k] += v
    log = sorted(c.items(), key=lambda x:x[1], reverse=True) #Сортируем трафик от максимума к минимуму

    print("\nTop-10 ip with high traffic, sorted by summary traffic: \n")
    for x, y in log[:10]:
        print('ip address: ' + x + ' traffic: ' + str(y) + ' bytes')
    print("\nOnly ip addresses: \n")
    for x,y in log[:10]:
        print(x)


if __name__ == "__main__":
    main()
