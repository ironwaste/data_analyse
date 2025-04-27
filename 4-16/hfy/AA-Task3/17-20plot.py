import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('17-20 各市各类学校在校生数（2023年）.xlsx')
df = excel_file.parse('17-20 各市各类学校在校生数（2023年）')
filter_df = df[df['17-20 各市各类学校在校生数（2023年）'].isin(['杭州市', '温州市', '宁波市'])]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
filter_df.columns = ['城市', '高等学校 (人)', '中等职业学校 (人)', '普通中学 (万人)', '小学(万人)']
ax = filter_df.set_index('城市').plot(kind='bar')
for container in ax.containers:
    for index, rect in enumerate(container):
        x_coord = rect.get_x() + rect.get_width() / 2
        y_coord = rect.get_height()
        plt.text(x_coord, y_coord, str(y_coord), ha='center', va='bottom', fontsize=4)
plt.xticks(rotation=360)
plt.title('杭州、温州、宁波三个城市各类学校在校生数对比')
plt.xlabel('城市')
plt.ylabel('在校生数')
plt.show()
