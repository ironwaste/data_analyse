import pandas as pd
import numpy as np
from openpyxl.utils.datetime import to_excel

df = pd.read_excel(r'./Report.xlsx')
new_df = df.reindex(columns=['售药时间','社保卡号','商品编码','商品名称','销售数量','应收金额','实收金额'])
new_df['售药时间']=new_df['售药时间'].astype(str)
new_df.loc[:,'售药时间']  = df.loc[:,'购药时间']
df_cleaned = new_df.dropna(axis=0)
df_cleaned.loc[:,'售药时间'] = df_cleaned.loc[:,'售药时间'].str.split(' ').str[0]

df_cleaned['售药时间'] = pd.to_datetime(df_cleaned['售药时间'],format='%Y-%m-%d',errors='coerce')
df_cleaned.sort_values(by='售药时间',ascending=False,inplace=True)
# print(df_cleaned.info())
df_cleaned = df_cleaned[df_cleaned['销售数量'] > 0]
df_cleaned = df_cleaned[df_cleaned['应收金额'] > 0]
df_cleaned = df_cleaned[df_cleaned['实收金额'] > 0]

# print(df_cleaned)
df_cleaned.to_excel(r'2022015232.xlsx')
print('success!!')