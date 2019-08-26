import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from visualize import *
from matplotlib import cm
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D

def scale(df):
    data = pd.DataFrame(df)
    std = data.std()
    mean = data.mean()
    df[0] = (df[0] - mean[0]) / std[0]
    df[1] = (df[1] - mean[1]) / std[1]
    return df

def gradientDescent(df, weights, learning_rate):
    for row in df.itertuples():
        predicted_output = weights[0] + row[1]*weights[1] + row[2]*weights[2]
        loss = predicted_output - row[3]
        weights[0] = weights[0] - ((learning_rates[i] / n) * loss)
        weights[1] = weights[1] - ((learning_rates[i] / n) * loss * row[1])
        weights[2] = weights[2] - ((learning_rates[i] / n) * loss * row[2])
    return weights

def writeResults(csv, learning_rate, iteration, weights):
    csv.write(str(learning_rate) + "\t")
    csv.write(str(iteration) + "\t")
    csv.write(str('{:3f}'.format(weights[0])) + "\t" + str('{:3f}'.format(weights[1])) + "\t" + str('{:3f}'.format(weights[2])))
    csv.write("\n")


if __name__ == "__main__":

    data = pd.read_csv(sys.argv[1], header=None)
    df = scale(data)
    csv = open(sys.argv[2], "w")
    learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, .075]
    n = len(df)

    weights = [0,0,0]
    for i in range(len(learning_rates)):
        weights = [0,0,0]
        for iteration in range(1, 101):
            weights = gradientDescent(df, weights, learning_rates[i])
        writeResults(csv, learning_rates[i], iteration, weights)
    
    csv.close()