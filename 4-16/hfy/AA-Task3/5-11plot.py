import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']



excel_file = pd.ExcelFile('5-11 各市城乡居民人均生活消费支出情况（2021-2023年）.xlsx')
sheet_name = excel_file.sheet_names
df = excel_file.parse(sheet_name[0])
df.columns = ['城市', '全体居民_2021', '全体居民_2022', '全体居民_2023', '城镇常住居民_2021', '城镇常住居民_2022', '城镇常住居民_2023', '农村常住居民_2021', '农村常住居民_2022', '农村常住居民_2023']
df = df[3:]
df = df.reset_index(drop=True)
selected_cities = ['杭州市', '宁波市', '温州市']
df = df[df['城市'].isin(selected_cities)]
plt.figure(figsize=(10, 6))
width = 0.25
years = ['2021', '2022', '2023']
num_years = len(years)
num_cities = len(df['城市'])
x = np.arange(num_cities)
for i, year in enumerate(years):
    all_residents = df[f'全体居民_{year}']
    urban_residents = df[f'城镇常住居民_{year}']
    rural_residents = df[f'农村常住居民_{year}']
    pos = x + (i - 1) * width
    plt.bar(pos, all_residents, width, label=f'全体居民_{year}')
    plt.bar(pos + width, urban_residents, width, label=f'城镇常住居民_{year}')
    plt.bar(pos + 2 * width, rural_residents, width, label=f'农村常住居民_{year}')
plt.xticks(x + width, df['城市'], rotation=45)
plt.title('杭州、宁波、温州不同类型居民 2021 - 2023 年人均生活消费支出情况')
plt.xlabel('城市')
plt.ylabel('人均生活消费支出（元）')
plt.legend()
plt.show()