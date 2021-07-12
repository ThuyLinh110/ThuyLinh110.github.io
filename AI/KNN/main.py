import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
dataset=pd.read_csv("./Iris.csv")
print(type(dataset))
x=dataset.iloc[:, [1, 2, 3,4]].values
y=dataset.iloc[:, -1].values

# num_of_sample=len(y)

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=4, stratify=y )

# def predit(x,k):
#     distances=[]
#     for row, out in zip(x_train,y_train):
#         distance=np.sqrt(np.sum((x-row)**2))
#         distances.append((distance,out))
#     distances.sort(key=lambda x:x[0])
#     distances=distances[:k]
#     count=dict()
#     for distance in distances:
#         if distance[1] in count:
#             count[distance[1]]+=1
#         else:
#             count[distance[1]]=1
#     return max(count)

# def evaluate(x_test,y_test):
#     count=0
#     for i in range(len(x_test)):
#         if predit(x_test[i],5)==y_test[i]:
#             count+=1
#     return count/len(y_test)

# print(evaluate(x_test,y_test))

