import pandas as pd
import numpy as np
import os
import re


# def modify_file(path,year) :
#     df = pd.read_csv(path)
#     df = df.drop(0)  # 删除 列名
#     df.columns = df.iloc[0]
#     df = df.drop(1)  # 删除第一行
#
#     df = df.drop(df.columns[0], axis=1)  # 删除多余的列
#     df = df.reset_index(drop=True)
#     df['年份'] = year
#
#
#
# list_path = [] # 用于存放文件的地址
# year = 2004
# for i in list_path :
#     modify_file(i,year)
#     year += 1
#
df = pd.read_csv('./by_year/2004.csv')

df = df.drop(0) # 删除 列名
df.columns = df.iloc[0]
df = df.drop(1) # 删除第一行

df = df.drop(df.columns[0],axis=1)# 删除多余的列
df = df.reset_index(drop=True)
df['年份'] = 2023

df.to_csv('./by_year/ans.csv')

# print(df)

# df = df.drop(df.columns[0], axis=1) # 删除第一列
# 自定义函数Preprogress对后几年数据需要进行的预处理
# 传入参数为df：数据框；year：年份数
# 返回处理过的数据框
# def Preprogress(df, year):
#     df.drop("Unnamed: 0", axis =1, inplace= True)       # 删除第0列
#     df.drop([0, 1 , len(df)-1], axis =0, inplace= True) # 删除头两行和后一行
#     df["年份"] = year                                   # 重塑年份变量
#     return(df)                                          # 返回值
#
#
# ## 自义函数ReadYear用于批量读取拼接数据
# ## 传入参数file_name:文件名列表;the_path:路径
# ## 返回值other_data：拼接过的数据
# def ReadYear(file_name, the_path):
#     list = []                                                        # 建立空列表用于存放数据
#     for i in range(len(file_name)):                                  # 通过循环遍历读取文件
#         df = pd.read_csv(the_path + file_name[i] , encoding = "gbk") # 读取数据
#         year = 2004+i+1                                              # 依次累加年份
#         Preprogress(df, year)                                        # 进行预处理及其重塑变量
#         list.append(df)                                              # 将处理过后的数据框添加到list中
#         other_data = pd.concat(list)                                 # 使用concat合并list内的数据
#     return(other_data)                                               # 返回值
#
#
#
# other_data = ReadYear(file_name, "by_year/")                         # 批量读取数据，命名为other_data
# other_data.head()
#


# os.chdir('C:/Users/CCC/Desktop/')                        # 设置工作路径为C盘桌面
# dat0 = pd.read_csv("by_year/2004.csv", encoding = "gbk") # 读取数据，命名为dat0
# # dat0.head()
# dat0.drop("Unnamed: 0", axis =1, inplace= True)        # 删除第一列
# col_name = dat0.iloc[1]                                # 选取真实列名所在的第1行
# dat0.columns = col_name                                # 更改列名
# dat0.drop([0, 1, len(dat0)-1], axis =0, inplace= True) # 删除多余的行
# # dat0.head()
#
#
#
# dat0.reset_index(inplace = True, drop=True) # 重新设置被打乱的index
# dat0["年份"] = 2004                         # 添加年份变量
# dat0.head()                                 # 展示数据
#
# file_name = os.listdir('by_year') # 获得by_year文件夹内的文件名[list形式]
# file_name.remove("2004.csv")      # 剔除已经读入的2004年的数据
# file_name                         # 查看列表