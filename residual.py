# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

datasets = ['clint','PPB','Solubility','logD']
models = []



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
    print('without scale')
    
    #model

    regr = RandomForestRegressor(random_state=0)
    regr.fit(X_train, Y_train)
    
    fout = open(data+'_residuals_train.txt','w')
    fout.write('Training Observed Value\tTraining Fitted Value\tTraining Residuals (observed - fitted)\t\n')

    #training performance
    y_pred_train = regr.predict(X_train)
    
    for x in range(len(Y_train)):
        fout.write(str(Y_train[x])+'\t'+str(y_pred_train[x])+'\t'+str(Y_train[x]-y_pred_train[x])+'\n')
         
    fout.close()
    
    #testing performance
    fout = open(data+'_residuals_test.txt','w')
    fout.write('Testing Observed Value\tTesting Fitted Value\tTesting Residuals (observed - fitted)\n')

    y_pred_test = regr.predict(X_test)
    
    for x in range(len(Y_test)):
        fout.write(str(Y_test[x])+'\t'+str(y_pred_test[x])+'\t'+str(Y_test[x]-y_pred_test[x])+'\n')

    fout.close()

