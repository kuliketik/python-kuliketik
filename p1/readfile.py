#!/usr/bin/env python
# coding=utf-8

FILENAME = "file.txt"

# buka berkas dengan mode read
berkas = open(FILENAME, "r")

# baca isi berkas

print berkas.readlines()


