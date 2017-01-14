#!/usr/bin/env python
# coding=utf-8

FILENAME = "file.txt"

prog_lang =  open(FILENAME, "r").readlines()

for lang in prog_lang:
    print lang.strip("\n")



