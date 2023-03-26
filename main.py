#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from test0 import test
from exams import quiz
import sys


# Let's load the csv with the data
csv = open('pinyin.csv', 'r', encoding='utf-8').read().split("\n")

language = 2  # default: english
if len(sys.argv) > 1:  # some parameters introduced!
	if sys.argv[1] == "--spanish": language = 3
	elif sys.argv[1] == "--russian": language = 4

# Build an array made of dictionaries
dict_array = []

for line in csv:
	dict_array.append({
		"chinese":line.split(";")[0],
		"pinyin":line.split(";")[1],
		"translation":line.split(";")[language]#,  # list()
		#"sentences":[],       # list()
		#"tag":""
	})

#test(dict_array)  # uncomment for test porpouses
quiz(dict_array, language)
