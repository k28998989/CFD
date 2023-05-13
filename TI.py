from MA import MA
from BBand import BBand
import pandas as pd
import matplotlib.pyplot as plt
TX=pd.read_csv('TX.csv',encoding= 'unicode_escape',low_memory=False)
print(TX)
tx,MA5,MA10,MA20=MA(TX)
BBAND5UP,BBAND5LOW=BBand(tx,5)
BBAND10UP,BBAND10LOW=BBand(tx,10)
BBAND20UP,BBAND20LOW=BBand(tx,20)
TI_list=zip(MA5,MA10,MA20,BBAND5UP,BBAND5LOW,BBAND10UP,BBAND10LOW,BBAND20UP,BBAND20LOW)
TI_PD=pd.DataFrame(TI_list,columns=['MA5','MA10','MA20','BBAND5UP','BBAND5LOW','BBAND10UP','BBAND10LOW','BBAND20UP','BBAND20LOW'])
print(TI_PD)
