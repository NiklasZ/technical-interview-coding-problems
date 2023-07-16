# Problem:
# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

# !/bin/python3

import math
import os
import random
import re
import sys
from typing import List


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matching_strings(string_list: List[str], queries: List[str]):
    frequencies = {s: 0 for s in string_list + queries}
    for s in string_list:
        frequencies[s] += 1
    return [frequencies[q] for q in queries]

