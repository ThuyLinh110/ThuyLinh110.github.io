import pandas as pd 
import os
dataset_path="./dataset/new test"
csv_path="./dataset/csv"

def read_data_from_dir(dir,label=None):
    if label is None:
        label=dir.split("/")[-1]
    label ="_".join(label.lower().split())
    data=[]  
    file_paths=os.listdir(dir)
    if file_paths and len(file_paths):
        for file in file_paths:
            with open(f"{dir}/{file}",mode='rb') as f:
                text=f.read() 
                data.append(text.decode("utf16").strip())
    return label,data

def save_to_csv(label,data):
    df=pd.DataFrame(data,columns=["text"])
    df.to_csv(f"{csv_path}/{label}.csv",index=True, encoding='utf-16')

if __name__=="__main__":
    folder_dirs=os.listdir(dataset_path)
    print(folder_dirs)
    for dir in folder_dirs:
        label,data=read_data_from_dir(f"{dataset_path}/{dir}")
        save_to_csv(label,data)


