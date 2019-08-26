# Machine Learning Models

This folder contains three machine learning models written in Python. The first two models are for supervised learning and the third model is for unsupervised learning. The details of each model are spelled out below.

1. Perceptron Learning Algorithm:  this subfolder contains a Python program which uses a single layer neural network to compute a decision boundary for a linearly separable data set. The perceptron uses Pandas and Numpy.

2. Linear Regression:  this subfolder contains a Python program which uses linear regression, data normalization, and gradient descent to predict the height of a person based on their age (years) and weight (kg) using CDC data. This model uses Pandas and Numpy. 

3. K-Means Clustering: this subfolder contains a Python program which uses K-means clustering to segment and group pixels of an image according to their RGD value.  This model uses sk.learn.cluster. 

## Getting Started

Each subfolder contains the .py files necessary to execute the program. The folders also contains sample input and output files to test the programs. 

1. Clone a copy of the machine-learning folder (or the subfolder of the model that interests you) and create a copy on your machine. 

2. Using a command prompt of your choice, navigate to the folder on your computer in which the .py files are contained.

3. To run the perceptron, execute the following command: python3 perceptron.py input1.csv <name-of-output-file.csv>

4. To run the linear regression model, execute the following command: python3 linear-regression-cdc.py input2.csv <name-of-output-file.csv>

5. To run the K-means clustering model, execute the following command: python3 k-means-clustering-img.py

You can use Matplotlib for each program to plot the results and display them using a 2D and 3D axis.

### Prerequisites And Installation

Python3:  https://www.python.org/downloads/

## Authors

Caleb Kinmon  
Columbia University, 2020  
Computer Science, Intelligent Systems
