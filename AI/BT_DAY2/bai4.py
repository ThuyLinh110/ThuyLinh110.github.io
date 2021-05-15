import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('./Car_sales.csv', encoding='utf-8')
#1
print(df.head(20))
#2
list =df.groupby('Manufacturer')
print(list['Sales_in_thousands'].agg([np.sum]))
#3
data=df[df['Manufacturer'] == 'Chevrolet']
plt.bar(data["Model"],data["Fuel_efficiency"],color='green')
plt.title("Chevrolet")
plt.xlabel("Model")
plt.ylabel("Fuel_efficiency")
plt.show()