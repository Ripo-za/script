#!/usr/bin/python
import sys
size,speed=sys.argv[1],sys.argv[2]
time = (int(size)*1024/int(speed))/60
print(time)

