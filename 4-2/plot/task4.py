import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df4 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task4',header=1)


df4 = delet_nan(task_df4)


list4 = []
list4 = list(df4)
list4 = list4[1:4]
df4 = df4[list4]

label_y = list4[1:]
label4 = df4[list4[0]]
df4 = df4[list4[1:]]
df4 = np.array(df4)
label4 = np.array(label4)

plt.plot(label4,df4)
plt.legend(label_y)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
# label_y