import pandas as pd 
import os

csv_path="./dataset/csv"
out_path="./dataset/tf_idf_csv"
special_chars = """' ... " + - _ . ’ , & : “ ” • [ ] { } ? ( ) ~ @ # $ % ^ * < > / \\ !  0 1 2 3 4 5 6 7 8 9"""
special_chars=special_chars.split(' ')

def preprocess_dataframe(text_arr):
    processed_data=[]
    for row in text_arr:
        processed_data.append(preprocess_row(row))
    return processed_data

def preprocess_row(text):
    data=[]
    data_arr=[]
    text=str(text).split('\n')
    data+=[para.replace('\r','').split('.') for para in text]
    for sen in data:
        sen=str(sen).strip().lower()
        for c in special_chars:
            if c in sen:
                sen=sen.replace(c,'')
        sen=sen.split('  ')
        data_arr.append(sen)
    return data_arr   


def get_vector_appear(para):
    wordDict=[]
    wordSet=para[0][0].split()
    for text in para:
        for sen in text:
            sen=sen.split()
            wordSet=set(wordSet).union(set(sen))
    for text in para:
        for sen in text:
            sen=sen.split()
            Dict=dict.fromkeys(wordSet,0)
            for word in sen:
                Dict[word]+=1
            wordDict.append(Dict)
    return wordDict   

def computeTF(wordD, sen):
    tfDict = {}
    wordsCount = len(sen)
    for word, count in wordD.items():
        tfDict[word] = count/float(wordsCount)
    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))     
    return idfDict

def computeTFIDF(tfDocs, idfs):
    tfidf = {}
    for word, val in tfDocs.items():
        tfidf[word] = val*idfs[word]
    return tfidf

def vector_TFIDF(para):
    wordDict=get_vector_appear(para)
    word=[]
    for text in para:
        for sen in text:
            if len(sen)>0:
                word.append(sen)
    idfs=computeIDF(wordDict)
    tfIdf=[]
    for i in range(len(word)):
        tfdocA= computeTF(wordDict[i],word[i])
        tfIdf.append(computeTFIDF(tfdocA,idfs))	
    return tfIdf

def list_folder_to_save(csv_path):
	folder=[]
	for label in os.listdir(csv_path):
		folder.append(label.split('.')[0])
	return folder

def save_to_csv(folder,label,data):
	df=pd.DataFrame(sen for sen in data)
	df.to_csv(f"{out_path}/{folder}_{label}.csv",index=False, encoding='utf-16')

if __name__=="__main__":
    list_folder=list_folder_to_save(csv_path)
    for folder in list_folder:
        df=pd.read_csv("./dataset/csv/am_nhac.csv",encoding='utf-16',sep=",")
        data=df['text']
        data=preprocess_dataframe(data)
        num_file=0
        for para in data:
            save_to_csv(folder,num_file,vector_TFIDF(para))
            num_file+=1
        exit(0)
