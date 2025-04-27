import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('13-5 主要城市平均气温（2023年）.xlsx')
df = excel_file.parse('13-5 主要城市平均气温（2023年）', header=2)
selected_cities = ['杭  州', '温  州', '宁  波']
filtered_df = df[df['城市'].isin(selected_cities)]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
melted_df = pd.melt(filtered_df, id_vars='城市', var_name='月份', value_name='平均气温')
plt.figure(figsize=(12, 6))
for city in selected_cities:
    city_data = melted_df[melted_df['城市'] == city]
    plt.plot(city_data['月份'], city_data['平均气温'], marker='o', label=city)
plt.title('杭州、温州、宁波2023年各月平均气温变化趋势')
plt.xlabel('月份')
plt.ylabel('平均气温（摄氏度）')
plt.xticks(rotation=45)
plt.legend()
plt.show()