datasets = ['clint','PPB','Solubility','logD']

for data in datasets:
    fin = open(data+'_descriptors.csv','r')
    headline = fin.readline()
    features = {}
    
    for line in fin:
        row = line.strip().split(',')
        features[row[0].strip('"')] = row[1:]
        
    fin.close()
    
    fin = open(data+'.txt')
    line = fin.readline()
    row = line.split('\t')
    endpoint_index = row.index('Standard Value')
    
    fout = open(data+'_dataset.txt','w')
    fout.write(headline.strip().replace(',','\t')+'\t'+data+'\n')
    
    for line in fin:
        row = line.split('\t')
        fout.write(row[0])
        
        for col in features[row[0]]:
            fout.write('\t'+col)
            
        fout.write('\t'+row[endpoint_index]+'\n')
        
    fin.close()
    fout.close()
    
