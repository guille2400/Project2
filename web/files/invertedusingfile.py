import pandas as pd
import numpy as np
import pickle 
from defines import *

def inverted_using_file(file_name):
    data_dict = {}
    word_processed = []
    word_processing = ""
    chunks = pd.read_csv(file_name,chunksize = CHUNK_SIZE)
    final_file = open(data_file_name, "wb")
    for chunk in chunks:
        for i, r in chunk.iterrows():
            current_word = r.values[0]

            # Aniadimos la primera palabra
            if len(word_processing) == 0:
                word_processing = current_word
                data_dict[current_word] = [] 
                data_dict[current_word].append((r.values[1], r.values[2]))
                continue

            # Aniadimos tf a la palabra actual
            else if word_processing == current_word:
                data_dict[current_word].append((r.values[1], r.values[2]))
                continue

            # Última instancia de palabra, volcar a archivo y borrar dict
            else:
                pickle.dump(data_dict, final_file) 
                data_dict.clear()

                word_processing = current_word
                data_dict[current_word] = [] 
                data_dict[current_word].append((r.values[1], r.values[2]))

