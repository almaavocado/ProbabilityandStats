import numpy as np
import random

import matplotlib
import matplotlib.pyplot as plt

def nSidedDie(p):
  n = np.size(p)
  #assign random num to r
  r = np.random.rand()
  #assign the cumulative sum of the elements in p to cs.
  cs = np.cumsum(p)
  cp = np.append(0,cs)

  #follow same method from lab one
  for k in range (0, n):
    if r > cp [k] and r <= cp[k + 1]:
      d = k + 1
      break
  return d


def enhancedTransmissionMethod(N):
    p0 = 0.6
    e0 = 0.05
    e1 = 0.03
    arrayS = []
    arrayR = []


    for i in range(0, N):
        s = nSidedDie([p0, 1 - p0])
        s -=1 

        if s == 1:
            arr = [1, 1, 1]
            arrayS.append(arr)

            arr = []

            for i in range(0, 3):
                r = nSidedDie([e1, 1 - e1])
                r -= 1
                arr.append(r)

            arrayR.append(arr)

        elif s == 0:
            arr = [0, 0, 0]
            arrayS.append(arr)

            arr = []
            for i in range(0, 3):
                r = nSidedDie([1 - e0, e0])
                r -= 1
                arr.append(r)
            arrayR.append(arr)


    temp = 0
    for k in range(len(arrayS)):

        cnt0 = arrayR[k].count(0)
        cnt1 = arrayR[k].count(1)

        if arrayS[k] == [0, 0, 0]:
            if cnt1 > cnt0:
                temp += 1
                
        elif arrayS[k] == [1, 1, 1]:
            if cnt0 > cnt1:
                temp += 1
    return temp / N


def main():
  print(enhancedTransmissionMethod(100000))

main()