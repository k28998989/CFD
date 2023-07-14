import pandas as pd
df=pd.read_csv("allbuy.csv",encoding='unicode_escape')

x=[]
y=[]
for i in range(df.shape[0]):
    if i % 3 == 2:
        x.append(df.values[i][0])
        y.append(df.values[i][12])
print(x)
print(y)
Lot=pd.DataFrame(list(zip(x, y)),columns=['Date', 'UnSellLots'])
print(Lot)