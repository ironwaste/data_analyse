import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('17-2 各市国民经济主要指标（2023年）.xlsx')
df = excel_file.parse('17-2 各市国民经济主要指标（2023年）')
df.columns = ['城市', '年末常住人口（万人）', '生产总值(亿元)', '生产总值(亿元)_第一产业', '生产总值(亿元)_第二产业', '生产总值(亿元)_第三产业', '生产总值(亿元)_工业', '人均生产总值(元)', '社会消费品零售总额 (亿元)', '进口总额 (亿元)', '出口总额 (亿元)', '财政总收入 (亿元)', '一般公共预算收入 （亿元', '一般公共预算支出 （亿元', '住户存款年末余额 (亿元)', '城镇居民人均可支配收入 (元)', '农村居民人均可支配收入 (元)']
df = df[2:]
df = df.reset_index(drop=True)
filter_df = df[df['城市'].isin(['杭州市', '温州市', '宁波市'])]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
bar = filter_df.set_index('城市')[['年末常住人口（万人）', '生产总值(亿元)', '人均生产总值(元)']].plot(kind='bar')
for container in bar.containers:
    for index, rect in enumerate(container):
        x_coord = rect.get_x() + rect.get_width() / 2
        y_coord = rect.get_height()
        week_day = filter_df['城市'].iloc[index]
        time_period = bar.get_xticklabels()[index].get_text()
        plt.text(x_coord, y_coord, str(y_coord), ha='center', va='bottom', fontsize=4)
plt.xticks(rotation=360)
plt.title('杭州、温州、宁波三个城市部分指标数据对比')
plt.xlabel('城市')
plt.ylabel('指标值')
plt.show()
