import pandas as pd
from tqdm import tqdm,trange
for i in range(2015,2023):
    pt='future_datasets/'+str(i)+'_fut.csv'    
    future=pd.read_csv(pt,encoding= 'unicode_escape',low_memory=False)
    print(future)
    TX_future=[]
    date=[]
    for i in trange(int(future.shape[0])):
        #print(future.values[i][0],future.values[i][-1])
        if future.values[i][1] == 'TX':
            if future.values[i][0] not in date:
                TX_future.append(future.values[i][:(16-int(future.shape[1]))])
                date.append(future.values[i][0])
            else:
                continue
    TX_future = pd.DataFrame(TX_future, columns=['Date','type','Month','Open','High','Low','Close','Price change','Price change Ratio','Volume','Final Price','# of OC','Final BBP',f'Final BSP','Hitorical HP','Historical LP'])
    print(TX_future)
    if i == 2010:
       TX_future.to_csv("TX.csv")
    else:
       TX_future.to_csv("TX.csv",mode='a',header=False)