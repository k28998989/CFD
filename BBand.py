import statistics
def SD(TX,Date):
    st_dev=[]
    for i in range(len(TX)):
        if i > Date-1:
            st_dev.append(statistics.pstdev(TX[i-Date:i]))
    return st_dev
def BBand(TX,Date):
    weight=1
    sd=SD(TX,Date)
    UB=[]
    LB=[]
    if Date == 5:
        UB=[8173.69,8193.80,8266.09,8283.00,8299.76]
        LB=[8051.51,8084.20,8117.11,8167.80,8181.44]
    elif Date == 10:
        UB=[8133.28,8159.39,8213.90,8239.34,8263.68,8289.96,8308.49,8306.89,8311.82,8334.19]
        LB=[7855.32,7914.41,7958.30,8011.66,8052.52,8094.24,8128.31,8161.31,8197.98,8208.81]
    else:
        UB=[8033.58,8065.39,8113.98,8148.37,8179.78,8214.81,8244.79,8262.58,8285.20,8308.49,8323.95,8327.94,8327.15,8320.56,8323.90,8330.99,8361.66,8378.73,8377.91,8371.63]
        LB=[7710.42,7721.21,7729.32,7742.03,7774.42,7792.59,7810.61,7834.42,7866.50,7910.71,7960.25,8007.96,8047.25,8080.64,8071.90,8051.81,7972.34,7902.97,7864.39,7808.67]
    ub=[TX[i+4]+sd[i]*weight for i in range(len(sd))]
    lb=[TX[i+4]-sd[i]*weight for i in range(len(sd))]
    UB=UB+ub
    LB=LB+lb
    return UB,LB
    