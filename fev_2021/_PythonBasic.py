#!/bin/python3

#Reverse Words and Swap Case

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
        return (" ".join(sentence.split()[::-1])).swapcase()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = "aWESOME is cODING" #input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()