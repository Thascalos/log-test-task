#!/bin/bash
awk '{print $1}' ../test.log | sort | uniq -c | sort -nr | head -1