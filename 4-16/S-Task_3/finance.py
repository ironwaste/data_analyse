import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 目标城市
cities = ['杭州', '宁波', '温州']

# 创建三组独立的数据，模拟三个Excel文件的内容
# 1. 气温数据
temp_data = {
    '城市': cities,
    '一月': [4.5, 5.1, 8.3],
    '四月': [16.8, 16.2, 18.5],
    '七月': [28.9, 27.8, 28.2],
    '十月': [18.5, 19.1, 21.6]
}
df_temp = pd.DataFrame(temp_data)
df_temp['年平均气温'] = df_temp[['一月', '四月', '七月', '十月']].mean(axis=1)

# 2. 日照时数数据
sunshine_data = {
    '城市': cities,
    '一月': [120, 130, 110],
    '四月': [150, 155, 145],
    '七月': [220, 210, 200],
    '十月': [160, 165, 155]
}
df_sunshine = pd.DataFrame(sunshine_data)
df_sunshine['年平均日照'] = df_sunshine[['一月', '四月', '七月', '十月']].mean(axis=1)

# 3. 空气质量数据
air_data = {
    '城市': cities,
    'PM2.5': [35, 32, 30],  # 数值越低越好
    'AQI': [78, 75, 72],    # 数值越低越好
    '优良天数占比': [82, 85, 87]  # 百分比，数值越高越好
}
df_air = pd.DataFrame(air_data)

# 4. 经济指标数据
econ_data = {
    '城市': cities,
    'GDP(亿元)': [18000, 14000, 7800],
    '人均可支配收入(元)': [68000, 62000, 55000],
    '城镇化率(%)': [78, 72, 70]
}
df_econ = pd.DataFrame(econ_data)

# 打印每个数据集的信息
print("气温数据：")
print(df_temp)
print("\n日照时数数据：")
print(df_sunshine)
print("\n空气质量数据：")
print(df_air)
print("\n经济指标数据：")
print(df_econ)

# 1. 气温数据可视化
plt.figure(figsize=(10, 6))
# 条形图
months = ['一月', '四月', '七月', '十月']
x = np.arange(len(cities))
width = 0.2
for i, month in enumerate(months):
    plt.bar(x + (i-1.5)*width, df_temp[month], width, label=month)

plt.ylabel('气温 (°C)', fontproperties=font)
plt.title('各城市季节性气温对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市气温条形图.png', dpi=300)

# 气温折线图
plt.figure(figsize=(10, 6))
for i, city in enumerate(cities):
    plt.plot(months, df_temp.loc[i, months], marker='o', label=city)

plt.ylabel('气温 (°C)', fontproperties=font)
plt.title('各城市季节性气温变化趋势', fontproperties=font)
plt.legend(prop=font)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市气温折线图.png', dpi=300)

# 2. 日照时数可视化
plt.figure(figsize=(10, 6))
# 条形图
for i, month in enumerate(months):
    plt.bar(x + (i-1.5)*width, df_sunshine[month], width, label=month)

plt.ylabel('日照时数 (小时)', fontproperties=font)
plt.title('各城市季节性日照时数对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市日照条形图.png', dpi=300)

# 日照折线图
plt.figure(figsize=(10, 6))
for i, city in enumerate(cities):
    plt.plot(months, df_sunshine.loc[i, months], marker='o', label=city)

plt.ylabel('日照时数 (小时)', fontproperties=font)
plt.title('各城市季节性日照时数变化趋势', fontproperties=font)
plt.legend(prop=font)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市日照折线图.png', dpi=300)

# 3. 空气质量可视化
plt.figure(figsize=(10, 6))
# 条形图
air_metrics = ['PM2.5', 'AQI', '优良天数占比']
for i, metric in enumerate(air_metrics):
    plt.bar(x + (i-1)*width, df_air[metric], width, label=metric)

plt.ylabel('指标值', fontproperties=font)
plt.title('各城市空气质量指标对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市空气质量条形图.png', dpi=300)

# 4. 经济指标可视化
plt.figure(figsize=(10, 6))
# 条形图 - GDP和人均收入需要不同的Y轴
fig, ax1 = plt.subplots(figsize=(10, 6))

# GDP条形图
ax1.bar(x - width/2, df_econ['GDP(亿元)'], width, label='GDP(亿元)', color='skyblue')
ax1.set_ylabel('GDP (亿元)', fontproperties=font, color='skyblue')
ax1.set_title('各城市经济指标对比', fontproperties=font)
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontproperties=font)
ax1.tick_params(axis='y', colors='skyblue')

# 人均收入条形图
ax2 = ax1.twinx()
ax2.bar(x + width/2, df_econ['人均可支配收入(元)'], width, label='人均可支配收入(元)', color='salmon')
ax2.set_ylabel('人均可支配收入 (元)', fontproperties=font, color='salmon')
ax2.tick_params(axis='y', colors='salmon')

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', prop=font)

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('各城市经济指标条形图.png', dpi=300)

# 5. 环境适宜度综合评估
# 根据上述数据计算环境适宜度指数
# 标准化函数
def normalize(series, reverse=False):
    result = (series - series.min()) / (series.max() - series.min())
    return 1 - result if reverse else result

# 计算各项指标的标准化得分
temp_score = normalize(df_temp['年平均气温'])  # 假设温度适中最好
sunshine_score = normalize(df_sunshine['年平均日照'])
pm25_score = normalize(df_air['PM2.5'], reverse=True)  # PM2.5越低越好
aqi_score = normalize(df_air['AQI'], reverse=True)  # AQI越低越好
good_days_score = normalize(df_air['优良天数占比'])  # 优良天数占比越高越好
income_score = normalize(df_econ['人均可支配收入(元)'])  # 收入越高越好

# 创建综合环境适宜度指数
env_index_data = {
    '城市': cities,
    '气候舒适度': (temp_score + sunshine_score) / 2,
    '空气质量': (pm25_score + aqi_score + good_days_score) / 3,
    '经济水平': income_score,
}
df_env = pd.DataFrame(env_index_data)

# 计算综合指数
weights = {'气候舒适度': 0.4, '空气质量': 0.4, '经济水平': 0.2}
df_env['环境适宜度指数'] = (
    df_env['气候舒适度'] * weights['气候舒适度'] +
    df_env['空气质量'] * weights['空气质量'] +
    df_env['经济水平'] * weights['经济水平']
)

print("\n环境适宜度指数：")
print(df_env)

# 综合环境适宜度雷达图
metrics = ['气候舒适度', '空气质量', '经济水平']
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图
metrics += metrics[:1]  # 闭合类别

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

for i, city in enumerate(cities):
    values = df_env.loc[i, metrics[:-1]].tolist()
    values += values[:1]  # 闭合数据
    ax.plot(angles, values, linewidth=2, label=city, marker='o')
    ax.fill(angles, values, alpha=0.1)

ax.set_thetagrids(np.degrees(angles[:-1]), metrics[:-1], fontproperties=font)
ax.set_ylim(0, 1)
ax.set_title('杭州、宁波和温州环境适宜度雷达图', fontproperties=font)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), prop=font)

plt.tight_layout()
plt.savefig('环境适宜度雷达图.png', dpi=300)

# 综合环境适宜度条形图
plt.figure(figsize=(12, 6))
index = np.arange(len(cities))
bar_width = 0.2

for i, metric in enumerate(metrics[:-1] + ['环境适宜度指数']):
    plt.bar(index + (i-1.5)*bar_width, df_env[metric], 
            bar_width, label=metric)

plt.xlabel('城市', fontproperties=font)
plt.ylabel('指数值', fontproperties=font)
plt.title('杭州、宁波和温州环境适宜度指数对比', fontproperties=font)
plt.xticks(index, cities, fontproperties=font)
plt.ylim(0, 1)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在条形图上添加数值标签
for i, metric in enumerate(metrics[:-1] + ['环境适宜度指数']):
    for j in range(len(cities)):
        plt.text(j + (i-1.5)*bar_width, 
                df_env[metric][j] + 0.02, 
                f'{df_env[metric][j]:.2f}', 
                ha='center', 
                fontsize=8)

plt.tight_layout()
plt.savefig('环境适宜度条形图.png', dpi=300)

# 创建环境适宜度排名并展示
df_ranking = df_env.sort_values(by='环境适宜度指数', ascending=False).reset_index(drop=True)
df_ranking.index = df_ranking.index + 1  # 从1开始的排名

print("\n城市环境适宜度排名：")
print(df_ranking[['城市', '环境适宜度指数']])

# 显示所有图形
plt.show()
