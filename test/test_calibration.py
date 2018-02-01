import numpy as np
import sys
import math
a='Users/margobatie/repos/NE204_lab0/code/'
sys.path.insert(0,a)
from code import *

#tests if the number of channels is a power of 2
def test_numchannels():
    assert (math.log2(len(chan))).is_integer()
