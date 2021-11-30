import pandas as pd
import numpy as np

## format  : FPKM, TPM, Count

def read_data_mmu(format):
    data = pd.read_csv('../data/mmu_data/mouse_all_data.csv',sep='\t')
    columns_filter = [i for i in data.columns if format in i]
    columns_filter.insert(0, 'Gene Symbol')
    data = data.loc[:,columns_filter]
    return data

def read_data_hsa(format):
    data = pd.read_csv('../data/hsa_data/cancer_rna.csv',sep='\t',index_col=1)
    columns_filter = [i for i in data.columns if format in i]
    data = data.loc[:,columns_filter]
    return data
