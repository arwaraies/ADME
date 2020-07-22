# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, ElasticNet, HuberRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error
from statistics import mean
from sklearn.preprocessing import MaxAbsScaler
from scipy.stats import skew, skewtest
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2, f_regression, mutual_info_regression

datasets = ['clint','PPB','Solubility','logD']

fout = open('chi2.txt','w')

for data in datasets:
    print(data)
    
    X = []
    Y = []
    fin = open(data+'_dataset.txt')
    
    headline = fin.readline()
    
    for line in fin:
        row = line.strip().split('\t')
        
        X.append([float(x) if x != '' else 0.0 for x in row[1:-1] ])
        Y.append(float(row[-1]))
        
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20, random_state = 0)
    
    ch2 = SelectKBest(mutual_info_regression, k=10)
    ch2.fit(X_train, Y_train)
    
    selected_features = ch2.get_support(indices = True)
    
    row=headline.split('\t')
    fout.write(data)
    
    for feature in range(len(selected_features)):
        fout.write('\t'+row[feature+1]) #+1 because the compound name is the first column
        
    fout.write('\n')
    
    
fout.close()

