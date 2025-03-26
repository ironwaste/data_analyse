import numpy as np
import pandas as pd
from pandas import DataFrame
df = pd.read_csv('./Report 5-Starbucks.csv')

## 计算南北半球
# 计算南北半球
df['Hemisphere_NS'] = df['Latitude'].apply(lambda x: 'Northern' if x >= 0 else 'Southern')

# 计算东西半球
df['Hemisphere_EW'] = df['Longitude'].apply(lambda x: 'Eastern' if x >= 0 else 'Western')


# 统计南北半球的门店数量
ns_counts = df['Hemisphere_NS'].value_counts()

# 统计东西半球的门店数量
ew_counts = df['Hemisphere_EW'].value_counts()

print("=== 南北半球星巴克门店数量 ===")
print(ns_counts)

print("\n=== 东西半球星巴克门店数量 ===")
print(ew_counts)


#######################################

# df = df.groupby(by='Country')

# cou = df['Brand'].count()
# cou_sorted = cou.sort_values(ascending=False)

# print(cou_sorted)
# print(cou)

# df_timezone = df.groupby(by='Timezone')
# dfcou = df_timezone["Brand"].count()
# print(dfcou)
# most_time = dfcou.idxmax()
# most_time = dfcou
# min_time = dfcou.idxmin()
# print(f"最多数量的时区是 ： {most_time}, 最少的失时区是{min_time}")

# # 2. 筛选中国和美国的数据
# china_data = df[df['Country'] == 'CN']  # 中国的数据
# us_data = df[df['Country'] == 'US']    # 美国的数据
#
#
#
# # 3. 统计中国各省的门店数量
# china_province_counts = china_data['State/Province'].value_counts()
# most_province_cn = china_province_counts.idxmax()  # 门店最多的省份
# max_count_cn = china_province_counts.max()         # 该省份的门店数量
#
# # 4. 统计美国各州的门店数量
# us_state_counts = us_data['State/Province'].value_counts()  # 注意列名可能是 'State/Province' 或 'State'
# most_state_us = us_state_counts.idxmax()  # 门店最多的州
# max_count_us = us_state_counts.max()      # 该州的门店数量
#
# # 5. 比较结果
# print("中国星巴克门店最多的省份:")
# print(f"{most_province_cn}: {max_count_cn} 家门店")
#
# print("\n美国星巴克门店最多的州:")
# print(f"{most_state_us}: {max_count_us} 家门店")
#
# print("\n比较结果:")
# if max_count_cn > max_count_us:
#     print(f"中国 {most_province_cn} 的门店数量 ({max_count_cn}) 多于美国 {most_state_us} ({max_count_us})")
# elif max_count_cn < max_count_us:
#     print(f"美国 {most_state_us} 的门店数量 ({max_count_us}) 多于中国 {most_province_cn} ({max_count_cn})")
# else:
#     print(f"中国 {most_province_cn} 和美国 {most_state_us} 的门店数量相同 ({max_count_cn})")
#
#





# print(df.groups)
# df_CN = df.get_group('CN')
# print(df_CN)
# df_prv = df_CN.groupby(by='State/Province')
# cou = df["Brand"].count()
# cn = cou['CN']
# fr = cou['FR']
# print(cou)
# df_prv = df_CN.groupby(by='State/Province')
# df_pro = df_prv.get_group('33')
# df_city = df_pro.groupby(by='City')
# cou = df_city['City'].count()
# print(cou)
# hangzhou = cou['杭州市']
# ningbo = cou['宁波市']
# print(hangzhou)
# print(ningbo)
# print(cou)

