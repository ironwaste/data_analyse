import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df3 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task3',header=1)

def autolabel(x) :
    """
    将柱状图上添加标签
    """
    for rec in x :
        re_h = rec.get_height()
        re_x = rec.get_x()
        re_width = rec.get_width()
        plt.text(re_x+re_width/2,re_h+1,s='{}'.format(re_h),ha='center',va='bottom',fontsize=9)


df3= delet_nan(task_df3)
# df3
list3 = []
list3 = list(df3)
list3 = list3[1:7]
df3 = df3[list3]
label3 = df3[list3[0]]
df3 = df3[list3[1:]]
arr3 = np.array(df3)
label_y = np.array(list3[1:])
label_x = np.array(label3)
print(label_x)
# print(arr3)
# print(label_y)

arr3 = arr3.T
cnt = 0
width3 = 0.1
pos_x = np.arange(1,5)
for rows in arr3:
    recta = plt.bar(pos_x+cnt*width3,rows,width=width3,tick_label=label_x)
    autolabel(recta)
    cnt+= 1
plt.legend(label_y,loc='upper right',bbox_to_anchor=[1.3,1.02])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
