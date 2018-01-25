import numpy as np

from code.modelling import gaus

def test_gaus_symmetry():
	A=100
	B=0
	C=1
	xr=2.0
	xl=-xr
	assert gaus(xr, A,B,C)==gaus(xl,A,B,C)
