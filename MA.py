
import pandas as pd
def MA(TX):
    MA5=[]
    tx=[]
    for i in range(len(TX)):
        print(i)
        tx.append(int(TX[i]))
        print(tx)
        if i > 4:
            MA5.append(sum(tx[i-4:i])/5)
    print(tx)
    return MA5
TX=pd.read_csv('TX.csv',encoding= 'unicode_escape',low_memory=False)
MA5=MA(TX.loc[:,'Close'])
print(TX.loc[:,'Close'])
print(MA5)