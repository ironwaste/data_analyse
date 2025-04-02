import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({'子类目':['童装','奶粉辅食','孕妈专区','洗护喂养','宝宝尿裤','春夏新品','童车童床','玩具文娱','童鞋'],
                   '销售额':[29665,3135.4,4292.4,5240.9,5543.4,5633.8,6414.5,9308.1,10353]})

name = np.array(df['子类目'])
data = np.array(df['销售额'])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(data,radius=1.5,labels=name,
        autopct='%0.3lf%%',pctdistance=0.5)
plt.show()

