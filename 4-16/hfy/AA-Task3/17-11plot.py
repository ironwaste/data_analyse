import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('17-11 各市客运量和货运量（2023年）.xlsx')
df = excel_file.parse('17-11 各市客运量和货运量（2023年）')
df.columns = ['城市', '客运量(万人)_公路、水路', '客运量(万人)_轨道交通（万人次）', '客运量(万人)_航空', '货运量(万吨)_公路、水路', '货运量(万吨)_航空']
df = df[2:]
df = df.reset_index(drop=True)
filter_df = df[df['城市'].isin(['杭州市', '温州市', '宁波市'])]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
ax = filter_df.set_index('城市').plot(kind='bar')
for container in ax.containers:
    for index, rect in enumerate(container):
        x_coord = rect.get_x() + rect.get_width() / 2
        y_coord = rect.get_height()
        plt.text(x_coord, y_coord, str(y_coord), ha='center', va='bottom', fontsize=4)
plt.xticks(rotation=360)
plt.title('杭州、温州、宁波三个城市客运量和货运量数据对比')
plt.xlabel('城市')
plt.ylabel('运输量')
plt.show()
