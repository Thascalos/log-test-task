#!/usr/bin/env python3
import collections
import sys

def log_parser(file):
    #Парсим лог и добавляем в список
    log = []
    for line in file:
        split_line = line.split()
        log.append((split_line[0], int(split_line[9])))
    return log

def main():
    if not len(sys.argv) > 1:
        print ("You must specify logfile")
        sys.exit(1)

    file = sys.argv[1]
    c = collections.Counter()

    try:
        file = open(file, 'r')
    except IOError:
        print ("Can't open file")
        sys.exit(1)
    
    log = log_parser(file) 
    #В цикле суммируем трафик
    for k, v in log:
        c[k] += v
    log = dict(c.most_common(10)) #Для удобства переводим в словарь первые 10 значений, сортировка уже произошла на шаге суммирования трафика
    print("\nTop-10 ip with high traffic, sorted by summary traffic: \n")
    print(log)

if __name__ == "__main__":
    main()
