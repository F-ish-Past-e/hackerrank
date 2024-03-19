#!/bin/python3
import math
import os
import random
import re
import sys

from dotenv import load_dotenv
load_dotenv()

def solve(s):
	words = s.split(' ')
	a_string = ''
	for s in words:
		a_string = a_string+s.capitalize()+' '
	return a_string

if __name__ == '__main__':

	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	result = solve(s)

	fptr.write(result)

	fptr.close()