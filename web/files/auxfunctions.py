import pandas as pd
import numpy as np

def calccossim(x, doc1, doc2): 
    vec_1 = x[doc1].to_numpy()   
    vec_2 = x[doc2].to_numpy()   
    return similarcos(value_1, value_2)

def similarcos(a, b):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def idf(freq, n):
    return np.log10(n/freq)

def tf(freq):
    if freq <= 0:
        return 0
    else:
        return 1 + np.log10(freq)


