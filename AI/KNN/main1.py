import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class KNN:
    def __init__(self,path,k):
        self.k=k
        self.dataset=pd.read_csv(path) 

    def fit(self):
        self.x=self.dataset.iloc[:, [1, 2, 3,4]].values
        self.y=self.dataset.iloc[:, -1].values 
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.4, random_state=4, stratify=self.y )

    def predict(self,x):
        distances=[]
        for row, out in zip(self.x_train,self.y_train):
            distance=np.sqrt(np.sum((x-row)**2))
            distances.append((distance,out))
        distances.sort(key=lambda x:x[0])
        distances=distances[:self.k]
        count=dict()
        for distance in distances:
            if distance[1] in count:
                count[distance[1]]+=1
            else:
                count[distance[1]]=1
        return max(count)

    def evaluate(self):
        count=0
        for i in range(len(self.x_test)):
            if self.predict(self.x_test[i])==self.y_test[i]:
                count+=1
        return count/len(self.y_test)

data=KNN("./Iris.csv",5)
data.fit()
print(data.evaluate())
