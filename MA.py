
import pandas as pd
def MA(TX):
    MA5=[8112,8139,8191.6,8225.4,8240.6]
    MA10=[7994,8036.9,8086.1,8125.5,8158.1,8192.1,8218.4,8234.1,8254.9,8271.5]
    MA20=[7872,7893.3,7921.65,7945.2,7977.1,8003.7,8027.7,8048.5,8075.9,8109.6,8142.1,8167.95,8187.20,8200.60,8197.90,8191.40,8167.00,8140.85,8121.15,8090.15]
    tx=[]
    for i in range(len(TX)):
        tx.append(int(TX.values[i][7]))
        if i > 4:
            MA5.append(sum(tx[i-5:i])/5)
        if i > 9:
            MA10.append(sum(tx[i-10:i])/10)
        if i >19:
            MA20.append(sum(tx[i-20:i])/20)
    #print(tx)
    return tx,MA5,MA10,MA20
#TX=pd.read_csv('TX.csv',encoding= 'unicode_escape',low_memory=False)
#MA5,MA10,MA20=MA(TX)
#print(MA5)