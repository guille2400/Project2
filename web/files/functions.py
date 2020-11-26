import pandas as pd
import numpy as np
import pickle
import ast
import math

from files.TweetContainer import TweetContainer
from files.functions2 import *
from files.defines import *
from files.auxfunctions import *

PATH = "./store/"

def word_relevantdata(word):
	l = 0
	r = NUM_TERMS - 2

	while l <= r:
		m = (l + r) // 2
		row = pd.read_csv(PATH + 'merged.csv', skiprows = m, nrows = 1).values.tolist()
		if word == str(row[0][0]):
			return {word : [(k, v) for k, v in ast.literal_eval(row[0][1]).items()]}
		if str(row[0][0]) < word:
			l = m + 1
		else:
			r = m - 1
	return {word : []}

def doc_freq_to_df(d_dict):
	df = pd.DataFrame(columns = ["word", "doc_freq"])
	for key in list(d_dict.keys()):
		dictofdata = {}
		dictofdata["word"] = key
		dictofdata["doc_freq"] = len(d_dict[key])
		new_row_df = pd.DataFrame(dictofdata, index = [0])
		df = df.append(dictofdata, ignore_index = True) 
	return df


def colmunsimportant(data_dict):
	column_set = set()
	for key in list(data_dict.keys()):
		for tuples in data_dict[key]: 
			column_set.add(tuples[0])
	return list(column_set)

def similar_n(text, n):
	tweet = TweetContainer([0, 0, text])
	textproccess = tweet.wordList

	dataofword = {}
	for word in set(textproccess):
		dataofword = {**dataofword, **word_relevantdata(word)}
		

	frequencydoc = {}
	documents = {}
	for word, term_freq in dataofword.items():
		frequencydoc[word] = len(term_freq) + 1
		for doc, freq in term_freq:
			if doc not in documents:
				documents[doc] = {}
			documents[doc][word] = freq

	query_freq = {}
	for word in textproccess:
		if word not in query_freq:
			query_freq[word] = 0
		query_freq[word] += 1
	
	tfidf_query = {}
	query_arg = 0
	for word in set(textproccess):
		tfidf_query[word] = tf(query_freq[word]) * idf(frequencydoc[word], DOCUMENT_COUNT)
		query_arg += tfidf_query[word]**2
	query_arg = math.sqrt(query_arg);
	
	idscore = []
	for doc, term_freq in documents.items():
		score = 0
		argofdoc = 0
		for word, freq in term_freq.items():
			tfidf = tf(freq) * idf(frequencydoc[word], DOCUMENT_COUNT)
			score += tfidf * tfidf_query[word]
			argofdoc += tfidf**2
		argofdoc = math.sqrt(argofdoc)
		score /= argofdoc * query_arg
		idscore.append((score, doc))
	
	idscore.sort(key=lambda tup: tup[0], reverse = True) 
	print(idscore[:n])
	return idscore[:n]
