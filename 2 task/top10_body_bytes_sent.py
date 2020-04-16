#!/usr/bin/env python3
import sys
def log_parser(file):
    log = []
    for line in file:
        split_line = line.split()
        log.append({'remote_host': split_line[0],
            'bytes_transfered': split_line[9],
        })

    return log

def myFunc(e):
  return e['bytes_transfered']

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print ("You must specify logfile")
        sys.exit(1)
        
    f = sys.argv[1]
    
    try:
        f = open(f, 'r')
    except IOError:
        print ("Can't open file")
        sys.exit(1)
        
    log = log_parser(f)
    log.sort(reverse=True, key=myFunc)
    print("\nTop-10 ip with high traffic (in one query): \n")
    for x in log[:10]:
        print(x)
    f.close()
