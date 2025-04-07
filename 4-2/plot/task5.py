import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as oxl
import datetime

def delet_nan(df) :
    df = df.dropna(axis=0,how ='all')
    return df

task_df5 = pd.read_excel('../Assignment8.xlsx',sheet_name='Task5',header=1)

df5 = delet_nan(task_df5)


list5 = []
list5 = list(df5)
list5 = list5[2:4]
df5 = df5[list5]
# df5 = delet_nan(df5)

label_y = list5
# print(df5.iloc[:,0])
px = np.array(df5.iloc[:,0])
py = np.array(df5.iloc[:,1])

plt.scatter(px,py)

plt.show()
print(px)
print(py)

# label5 = df5[list5[0]]
# px
