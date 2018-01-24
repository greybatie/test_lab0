import numpy as np

def gaus(x,A,B,C):
  """
  this is called a doc string with the three double quotation marks
  
  This is a 3-parameter gaussian function
  A=amplitdue
  B=centroid
  C= std. deviation
  """
  return A*np.exp(-(x-B)**2/(2*C**2))
