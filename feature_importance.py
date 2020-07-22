# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

    regr = RandomForestRegressor(random_state=0)
    regr.fit(X_train, Y_train)
    ranked_indices = -(regr.feature_importances_).argsort()
    
    row=headline.split('\t')
    fout.write(data)
    
    for x in range(10):
        fout.write('\t'+row[ranked_indices[x]+1]) #+1 because the compound name is the first column
        
    fout.write('\n')
        
fout.close()

