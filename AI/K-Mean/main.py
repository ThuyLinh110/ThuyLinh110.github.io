import numpy as np 
import json
import matplotlib.pyplot as plt

def process_data(path):
    with open(path, "r") as f:
        data = json.load(f)
    X=np.zeros((len(data),2))
    x,y=[],[]
    for d in data:
        x.append(d['Math'])
        y.append(d['Literature'])
    X[:,0]=x 
    X[:,1]=y
    return X

def init_center(X,k):
    return X[np.random.choice(X.shape[0],k,replace=False)]

def distance(X,center):
    distances=[]
    for x in X:
        distance=[]
        for c in center:
            distance.append(np.sqrt(np.sum((x-c)**2)))
        distances.append(distance)
    return distances
    
def assign_label(X,center):
    D= distance(X,center)
    return np.argmin(D,axis=1)

def update_center(X,label,K):
    center=np.zeros((K,X.shape[1]))
    for k in range(K):
        Xk=X[label ==k ,:]
        center[k,:]=np.mean(Xk,axis=0)
    return center

def has_converged(center, new_center):
    return (set([tuple(a) for a in center]) == 
    set([tuple(b) for b in new_center]))

def kMeans(X,K):
    center =[ init_center(X,K)]
    label=[]
    while True:
        label.append(assign_label(X,center[-1]))
        new_center= update_center(X,label[-1],K)
        if has_converged(center[-1], new_center):
            break
        center.append(new_center)
        display(X,label[-1],new_center)
    return (center, label)

def display(X, label,center):
    K=np.amax(label)+1
    X0=X[label==0,:]
    X1=X[label==1,:]
    X2=X[label==2,:]
    X3=X[label==3,:]
    plt.plot(X0[:, 0], X0[:, 1], 'yo', markersize = 5, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 5, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'ro', markersize = 5, alpha = .8)
    plt.plot(X3[:, 0], X3[:, 1], 'bo', markersize = 5, alpha = .8)

    plt.plot(center[:, 0], center[:, 1], 'ko', markersize = 5, alpha = .8)

    plt.axis('equal')
    plt.plot()
    plt.show()

K=4
X= process_data("score_cluster.json")
(centers, labels) = kMeans(X, K)
print('Centers found by our algorithm:')
print(centers[-1])

