import sys
import re

argv = sys.argv[1:]

def getFlags(*flags):
    for flag in flags:
        for arg in argv:
            if (flag == arg):
                return flag
    return ''

def getFlagsList(flags):
    for flag in flags:
        for arg in argv:
            if (flag == arg):
                return flag
    return ''

def getFiles(exc = r'^-[A-z]+', inc = r'.*'):
    files = []
    for arg in argv:
        if (not re.search(exc,arg)):
            if (re.search(inc, arg)):
                files.append(arg)
    return files