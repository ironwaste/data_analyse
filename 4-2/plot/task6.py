import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df6 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task6',header=1)

df6 = delet_nan(task_df6)
df6 =df6.iloc[0:10,1:6]
print(df6)
# df6 = df6.sort_values()
arr = np.array(df6)
# 两种将二维数组更改为一维数组的方式
# arr = arr.flatten()
# arr = arr.reshape(arr.shape[0]*arr.shape[1])
arr = arr.reshape(-1,)
# numpy 统计个数 一个数组内同一元素的个数
# dfarr = pd.Series(arr).value_counts()
# x = np.array(dfarr.index)
# y = dfarr.values

plt.hist(arr,bins=8)
plt.show()
