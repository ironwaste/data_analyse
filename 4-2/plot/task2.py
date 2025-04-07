import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df2 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task2',header=1)


df2 = delet_nan(task_df2)
# df2
list2 = []
list2 = list(df2)
list2 = list2[1:3]
df2 = df2[list2]

label_y = np.array(df2[list2[0]])
x= np.array(df2[list2[1]])
# print(label_y)
# print(x)
# pie chart

plt.pie(x,autopct='%.03lf%%',startangle=90)



plt.legend(label_y,loc='upper right',bbox_to_anchor=[1.3,1.3])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()