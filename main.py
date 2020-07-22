# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error
from statistics import mean

datasets = ['clint','PPB','Solubility','logD']
models = []

fout = open('results.txt','w')
fout.write('Dataset\tModel\tRandom Training R2\tRandom Testing R2\tTraining R2\tTesting R2\tRandom Training MAE\tRandomt Testing MAE\tTraining MAE\tTesting MAE\n')

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

    regr = RandomForestRegressor(random_state=0)
    regr.fit(X_train, Y_train)
    
    #random model (assign the average value for all predictions)
    y_pred = [mean(Y_train) for x in range(len(Y_train))]
    r2_random_training = r2_score(Y_train,y_pred)
    msr_random_training = median_absolute_error(Y_train,y_pred)
    
    y_pred = [mean(Y_train) for x in range(len(Y_test))]
    r2_random_testing = r2_score(Y_test,y_pred)
    msr_random_testing = median_absolute_error(Y_test,y_pred)
    
    #training performance
    y_pred = regr.predict(X_train)
    r2_training = r2_score(Y_train,y_pred)
    msr_training = median_absolute_error(Y_train,y_pred)
    
    #testing performance
    y_pred = regr.predict(X_test)
    r2_testing = r2_score(Y_test,y_pred)
    msr_testing = median_absolute_error(Y_test,y_pred)
    
#        print(str(regr.__class__.__name__)+'\tR2\t'+str(r2_random)+'\t'+str(r2_training)+'\t'+str(r2_testing))
#        print(str(regr.__class__.__name__)+'\tMAR\t'+str(msr_random)+'\t'+str(msr_training)+'\t'+str(msr_testing))
    
    fout.write(data+'\t'+str(regr.__class__.__name__)+'\t'+\
               str(r2_random_training)+'\t'+str(r2_random_testing)+'\t'+str(r2_training)+'\t'+str(r2_testing)+'\t'+\
               str(msr_random_training)+'\t'+str(msr_random_testing)+'\t'+str(msr_training)+'\t'+str(msr_testing)+'\n')
        

fout.close()

