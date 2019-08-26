import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from visualize import *
from matplotlib import cm
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D

def h(row, weights):
    sum = (weights[0] * row._1) + (weights[1] * row._2) + weights[2]
    if sum >= 0:
        return 1
    else:
        return -1

def writeResults(csv, weights):
    csv.write(str(weights[2]) + "\t" + str(weights[0]) + "\t" + str(weights[1]))
    csv.write("\n")

if __name__ == "__main__":

    data = pd.read_csv(sys.argv[1], header=None)
    csv = open(sys.argv[2], "w")
    mismatchCount = 1
    weights = [0,0,0]
    while(mismatchCount > 0):
        mismatchCount = 0
        for row in data.itertuples():
            classification = h(row, weights)
            if classification is not row._3:
                mismatchCount += 1
                weights[0] = weights[0] + ((row._3 - classification) * row._1)
                weights[1] = weights[1] + ((row._3 - classification) * row._2)
                weights[2] = weights[2] + ((row._3 - classification) * 1)        
        writeResults(csv, weights)

    csv.close()