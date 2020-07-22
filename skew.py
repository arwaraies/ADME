# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error

from scipy.stats import skew, skewtest
import numpy as np

datasets = ['clint','PPB','Solubility','logD']
models = [RandomForestRegressor(random_state=0)]



for data in datasets:
    print(data)
    
    X = []
    Y = []
    fin = open(data+'_dataset.txt')
    
    line = fin.readline()
    
    for line in fin:
        row = line.strip().split('\t')
        
        X.append([float(x) if x != '' else 0.0 for x in row[1:-1] ])
        Y.append(float(row[-1]))
        
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20, random_state = 0)
    
    #model
    for model in models:
        regr = model
        regr.fit(X_train, Y_train)
            
        #training performance
        y_pred_train = regr.predict(X_train)
        residue = np.array(Y_train) - np.array(y_pred_train)
        print(skewtest(residue))
        
        #testing performance
        y_pred_test = regr.predict(X_test)
        residue = np.array(Y_test) - np.array(y_pred_test)
        print(skewtest(residue))

