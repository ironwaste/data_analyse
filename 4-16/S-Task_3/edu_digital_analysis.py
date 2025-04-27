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

#------------------------- 教育数据 -------------------------
# 模拟各类学校在校生数据
edu_data = {
    '城市': cities,
    '小学在校生(万人)': [85.5, 65.2, 72.8],
    '中学在校生(万人)': [42.3, 32.6, 35.1],
    '高中在校生(万人)': [18.7, 15.4, 13.2],
    '大学在校生(万人)': [58.2, 25.3, 18.7]
}
df_edu = pd.DataFrame(edu_data)

# 计算教育综合指标 - 人口受教育水平
df_edu['教育总人数(万人)'] = df_edu['小学在校生(万人)'] + df_edu['中学在校生(万人)'] + df_edu['高中在校生(万人)'] + df_edu['大学在校生(万人)']
df_edu['高等教育占比(%)'] = df_edu['大学在校生(万人)'] / df_edu['教育总人数(万人)'] * 100

#------------------------- 数字化转型数据 -------------------------
# 模拟互联网发展和数字化转型数据
digital_data = {
    '城市': cities,
    '互联网普及率(%)': [92.5, 88.7, 85.3],
    '数字经济占GDP比重(%)': [45.2, 38.6, 32.8],
    '5G基站密度(个/平方公里)': [12.8, 10.5, 8.2],
    '数字化转型企业占比(%)': [68.5, 62.3, 55.7],
    '智慧城市指数': [89.5, 82.7, 75.8]
}
df_digital = pd.DataFrame(digital_data)

# 打印数据信息
print("教育数据：")
print(df_edu)
print("\n数字化转型数据：")
print(df_digital)

#------------------------- 教育数据可视化 -------------------------
plt.figure(figsize=(12, 6))
x = np.arange(len(cities))
width = 0.2
edu_metrics = ['小学在校生(万人)', '中学在校生(万人)', '高中在校生(万人)', '大学在校生(万人)']
colors = ['#FF9999', '#FFCC99', '#99CC99', '#9999CC']

for i, metric in enumerate(edu_metrics):
    plt.bar(x + (i-1.5)*width, df_edu[metric], width, label=metric, color=colors[i])

plt.xlabel('城市', fontproperties=font)
plt.ylabel('在校生数量(万人)', fontproperties=font)
plt.title('各城市各级学校在校生数量对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数值标签
for i, metric in enumerate(edu_metrics):
    for j in range(len(cities)):
        plt.text(j + (i-1.5)*width, 
                df_edu[metric][j] + 1, 
                f'{df_edu[metric][j]}', 
                ha='center', 
                fontsize=8)

plt.tight_layout()
plt.savefig('各城市教育数据条形图.png', dpi=300)

# 高等教育占比柱状图
plt.figure(figsize=(10, 6))
plt.bar(cities, df_edu['高等教育占比(%)'], color='#9999CC')
plt.xlabel('城市', fontproperties=font)
plt.ylabel('高等教育占比(%)', fontproperties=font)
plt.title('各城市高等教育占比', fontproperties=font)
plt.ylim(0, max(df_edu['高等教育占比(%)']) * 1.2)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数值标签
for i in range(len(cities)):
    plt.text(i, df_edu['高等教育占比(%)'][i] + 0.5, 
            f'{df_edu["高等教育占比(%)"][i]:.1f}%', 
            ha='center', 
            fontsize=10)

plt.tight_layout()
plt.savefig('各城市高等教育占比.png', dpi=300)

#------------------------- 数字化转型数据可视化 -------------------------
plt.figure(figsize=(12, 6))
digital_metrics = ['互联网普及率(%)', '数字经济占GDP比重(%)', '5G基站密度(个/平方公里)', 
                  '数字化转型企业占比(%)', '智慧城市指数']
                  
# 标准化数据，使所有指标在0-1之间，便于比较
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

df_digital_norm = df_digital.copy()
for metric in digital_metrics:
    df_digital_norm[metric] = normalize(df_digital[metric])

# 绘制数字化转型条形图
width = 0.15
for i, metric in enumerate(digital_metrics):
    plt.bar(x + (i-2)*width, df_digital[metric], width, label=metric)

plt.xlabel('城市', fontproperties=font)
plt.ylabel('指标值', fontproperties=font)
plt.title('各城市数字化转型指标对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.legend(prop=font, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.savefig('各城市数字化转型指标条形图.png', dpi=300)

#------------------------- 综合雷达图可视化 -------------------------
# 组合关键指标进行雷达图分析
radar_data = {
    '城市': cities,
    '教育水平': normalize(df_edu['高等教育占比(%)']),
    '教育规模': normalize(df_edu['教育总人数(万人)']),
    '互联网普及': normalize(df_digital['互联网普及率(%)']),
    '数字经济': normalize(df_digital['数字经济占GDP比重(%)']),
    '数字基础设施': normalize(df_digital['5G基站密度(个/平方公里)']),
    '智慧城市建设': normalize(df_digital['智慧城市指数'])
}
df_radar = pd.DataFrame(radar_data)

# 雷达图
metrics = ['教育水平', '教育规模', '互联网普及', '数字经济', '数字基础设施', '智慧城市建设']
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图
metrics += metrics[:1]  # 闭合类别

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

for i, city in enumerate(cities):
    values = df_radar.loc[i, metrics[:-1]].tolist()
    values += values[:1]  # 闭合数据
    ax.plot(angles, values, linewidth=2, label=city, marker='o')
    ax.fill(angles, values, alpha=0.1)

ax.set_thetagrids(np.degrees(angles[:-1]), metrics[:-1], fontproperties=font)
ax.set_ylim(0, 1)
ax.set_title('杭州、宁波和温州教育与数字化发展雷达图', fontproperties=font)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), prop=font)

plt.tight_layout()
plt.savefig('教育与数字化发展雷达图.png', dpi=300)

# 计算综合得分
weights = {
    '教育水平': 0.15,
    '教育规模': 0.15,
    '互联网普及': 0.15,
    '数字经济': 0.20,
    '数字基础设施': 0.15,
    '智慧城市建设': 0.20
}

df_radar['综合发展指数'] = 0
for metric, weight in weights.items():
    df_radar['综合发展指数'] += df_radar[metric] * weight

# 综合排名
df_ranking = df_radar.sort_values(by='综合发展指数', ascending=False).reset_index(drop=True)
df_ranking.index = df_ranking.index + 1  # 从1开始的排名

print("\n城市教育与数字化发展综合排名：")
print(df_ranking[['城市', '综合发展指数']])

# 绘制综合得分条形图
plt.figure(figsize=(10, 6))
plt.bar(cities, df_radar['综合发展指数'], color='#3A6DAA')
plt.xlabel('城市', fontproperties=font)
plt.ylabel('综合发展指数', fontproperties=font)
plt.title('各城市教育与数字化综合发展指数', fontproperties=font)
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数值标签
for i in range(len(cities)):
    plt.text(i, df_radar['综合发展指数'][i] + 0.02, 
            f'{df_radar["综合发展指数"][i]:.3f}', 
            ha='center', 
            fontsize=10)

plt.tight_layout()
plt.savefig('各城市综合发展指数.png', dpi=300)

# 显示所有图形
plt.show() 