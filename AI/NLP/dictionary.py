import pandas as pd 

file_path="./dataset/csv/gia_dinh.csv"

special_chars="""' … " -  .  ’ , & : “ ” • { } ? ( ) ~ @ # $ % ^ * < > / \ !  0 1 2 3 4 5 6 7 8 9"""
special_chars=special_chars.split(' ')

VOCAB=dict()
NUM_SENTENCE=0
SENTENCE_LIST=[]
NUM_WORD=0

def preprocess_dataframe(text_arr):
    processed_data=[]
    for row in text_arr:
        processed_data.append(preprocess_row(row))
    return processed_data

def preprocess_row(text):
    global NUM_SENTENCE
    data=[]
    text=str(text).split('\n')
    data+=[para.replace('\r','').split('.') for para in text]
    NUM_SENTENCE+=len(text)
    for sen in text:
        preprocess_sentence(sen)

def preprocess_sentence(text):
    global VOCAB
    global SENTENCE_LIST
    text=str(text).strip().lower()
    for c in special_chars:
        if c in text:
            text=text.replace(c,'')
    SENTENCE_LIST.append(text)
    list_word=text.split(' ')
    
    for word in list_word:
        if word in VOCAB:
            VOCAB[word]+=1
        else:
            VOCAB[word]=1

if __name__=="__main__":
    # print("special_chars: ",special_chars)
    df=pd.read_csv(file_path)
    data=df.values[:,1]
    data=preprocess_dataframe(data)
    print(VOCAB)