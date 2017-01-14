#!/usr/bin/env python
# coding=utf-8

FILENAME = "file.txt"

TARGET = "python"

prog_lang =  open(FILENAME, "r").readline().strip("\n")

print prog_lang

if TARGET in prog_lang:
    print "{0} in {1}".format(TARGET, FILENAME)
else:
    print "{0} not found".format(TARGET)


