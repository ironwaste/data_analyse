import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./中国地震台数据.csv")
df = df.iloc[:,0:6]
df.drop_duplicates(inplace=True)

# df.info()
location = df.pop('参考位置')
location.astype(str)
location=location.str[:2]
print(location)


df.insert(1,'参考位置',location)

location_counts = df['参考位置'].value_counts()

print("\n参考位置统计结果：")
print(location_counts)

plt.figure(figsize=(12, 6))
location_counts.plot(kind='bar')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('地震参考位置分布统计')
plt.xlabel('参考位置')
plt.ylabel('频次')
plt.xticks(rotation=0, ha='right')
plt.tight_layout()
plt.show()

plt.close()