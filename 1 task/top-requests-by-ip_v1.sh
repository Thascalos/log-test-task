#!/bin/bash
cat ../test.log | cut -d '"' -f1 | cut -d ' ' -f1 | sort | uniq -c | sort -rn | head -n1
