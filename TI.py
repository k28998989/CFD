from MA import MA
from BBand import BBand
import pandas as pd
import matplotlib.pyplot as plt
TX=pd.read_csv('TX.csv',encoding= 'unicode_escape',low_memory=False,header=None)
tx,MA5,MA10,MA20=MA(TX)
BBAND5UP,BBAND5LOW=BBand(tx,5)
BBAND10UP,BBAND10LOW=BBand(tx,10)
BBAND20UP,BBAND20LOW=BBand(tx,20)
TX=TX.iloc[:,1:]
#TX=pd.DataFrame(TX,columns=['Date','type','Month','Open','High','Low','Close','Price change','Price change Ratio','Volume','Final Price','# of OC','Final BBP','Final BSP','Hitorical HP','Historical LP'])
print(TX)
TI_list=zip(MA5,MA10,MA20,BBAND5UP,BBAND5LOW,BBAND10UP,BBAND10LOW,BBAND20UP,BBAND20LOW)
TI_PD=pd.DataFrame(TI_list,columns=['MA5','MA10','MA20','BBAND5UP','BBAND5LOW','BBAND10UP','BBAND10LOW','BBAND20UP','BBAND20LOW'])

#print(TI_PD)

TX_TI=pd.concat([TX,TI_PD],axis=1)
TX_TI=TX_TI.rename(columns={1:'Date',2:'type',3:'Month',4:'Open',5:'High',6:'Low',7:'Close',8:'Price change',
                     9:'Price change Ratio',10:'Volume',11:'Final Price',12:'# of OC',13:'Final BBP',14:'Final BSP',15:'Hitorical HP',16:'Historical LP'})
print(TX_TI)
TX_TI.to_csv("TX_TI.csv")
