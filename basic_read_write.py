"""
Owner: Akhil Agrawal
Purpose: Generic Python file to start with any input/output in any competitive coding.
"""

import sys

#important imports
from collections import Counter
import heapq
import math

def get_a_int():
    return int(input())

def get_ints():
    """for multiple integers one or more"""
    return map(int,sys.stdin.readline().strip().split())

def get_int_array():
    return list(map(int,input().strip().split()))

def get_string():
    return sys.stdin.readline().strip()

def reading_file(file_name,encoding=None):
    # good in case of small files
    with open(file_name,'r', encoding = encoding) as f:
        lines = f.readlines()
    return lines

def writing_file(file_name,data,encoding=None):
    """Assunimg data is in list of data that needs to be printed"""
    with open(file_name,'w', encoding = encoding) as f:
        for line in data:
            f.write(line)
            f.write('\n')
    return "success"

if __name__=="__main__":
    #listy=list(get_ints())
    string=get_string()
    print(string)
