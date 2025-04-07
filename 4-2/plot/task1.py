import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df1 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task1',header=1)

task_df1.info()

task_df1 = delet_nan(task_df1)
task_df1.info()
# reindex
# df1 = task_df1.reindex(index=np.arange(0,32063))
# df1
# 删除缺失值
df1=task_df1[['Number of errors at East Gate ','Number of errors at West Gate ']]
df1 = delet_nan(df1)
# 去除重复值
df1.drop_duplicates(inplace=True,ignore_index=False)
df1.info()
df1.head()
df1.tail()
# df1[['Number of errors at East Gate']]
# list DataFrame 可以直接获取列名称
list_col = []
list_col = list(df1)
# list_col

east = np.array([])
west = east
vcnt = east
lim = 100
cnt,esum,wsum = 0,0,0

for index,value in df1.iterrows() :
    # print(value)
    s = str(value.iloc[0])
    # print(s)
    if not s.isdigit() :
        continue
    esum += (int)(value.iloc[0])
    wsum +=(int)(value.iloc[1])
    cnt += 1
    if cnt >= lim :
        vcnt = np.append(vcnt,[cnt])
        cnt = 0
        east = np.append(east,[esum])
        west = np.append(west,[wsum])
        esum = 0
        wsum = 0


east = np.append(east,[esum])
west = np.append(west,[wsum])
vcnt = np.append(vcnt,[cnt])
print(east)
print(west)
emean = []
wmean = []

emean = east/vcnt
wmean = west/vcnt

print(emean)
print(wmean)
def autolabel(x) :
    """
    将柱状图上添加标签
    """
    for rec in x :
        re_h = rec.get_height()
        re_x = rec.get_x()
        re_width = rec.get_width()
        plt.text(re_x+re_width/2,re_h+1,s='{}'.format(re_h),ha='center',va='bottom',fontsize=9)


bar_width = 0.33
x = np.arange(1,6)
recta = plt.bar(x,emean,width=bar_width)
rectb = plt.bar(x+bar_width,wmean,width=bar_width)
autolabel(recta)
autolabel(rectb)



plt.legend(list_col,loc='lower left')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()