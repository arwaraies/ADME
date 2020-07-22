# -*- coding: utf-8 -*-

endpoints = ['logD','clint','PPB','solubility']

for endpoint in endpoints:
    fin = open(endpoint+'.txt','r')
    
    line = fin.readline()
    row = line.split('\t')
    id_index = row.index('Molecule ChEMBL ID')
    smiles_index = row.index('Smiles')
    
    for line in fin:
        row = line.split('\t')
        
        fout = open('./'+endpoint+'_smiles/'+row[id_index]+'.smi','w')
        fout.write(row[smiles_index])
        fout.close()
    
    
    fin.close()

