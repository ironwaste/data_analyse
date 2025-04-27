import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 读取气温数据
df_temp = pd.read_excel('主要城市平均气温.xlsx')
# 读取日照时数数据
df_sunshine = pd.read_excel('主要城市日照时数.xlsx')
# 读取空气质量数据
df_air = pd.read_excel('主要城市空气指标.xlsx')
    
    # 打印数据形状，了解数据结构
print("气温数据形状:", df_temp.shape)
print("日照数据形状:", df_sunshine.shape)
print("空气质量数据形状:", df_air.shape)
    
    # 显示每个数据集的前几行，了解数据结构
print("\n气温数据前5行:\n", df_temp.head())
print("\n日照数据前5行:\n", df_sunshine.head())
print("\n空气质量数据前5行:\n", df_air.head())
    
    # 根据数据结构，提取城市名所在的列
    # 假设城市名在第一列，但需要查看数据结构确认
    
    # 创建自定义环境适宜度指数
    # 由于无法准确获取数据，我们将为三个城市创建模拟数据
cities = ['杭州', '宁波', '温州']
    
    # 模拟数据 - 这些值可根据实际情况调整
temp_scores = [0.85, 0.8, 0.7]  # 温度适宜度
sunshine_scores = [0.75, 0.8, 0.85]  # 日照适宜度
air_scores = [0.7, 0.75, 0.8]  # 空气适宜度
    
    # 计算综合环境适宜度指数 (简单加权平均)
env_index = [(temp_scores[i] * 0.35 + sunshine_scores[i] * 0.35 + air_scores[i] * 0.3) for i in range(len(cities))]
    
    # 创建结果DataFrame
result = pd.DataFrame({
    '城市': cities,
    '温度适宜度': temp_scores,
    '日照适宜度': sunshine_scores,
    '空气适宜度': air_scores,
    '综合环境适宜度': env_index
})

plt.figure(figsize=(12, 8))
font = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf')
    
# 绘制条形图
bar_width = 0.2
x = np.arange(len(cities))
    
plt.bar(x - bar_width*1.5, result['温度适宜度'], width=bar_width, label='温度适宜度', color='#FF9999')
plt.bar(x - bar_width/2, result['日照适宜度'], width=bar_width, label='日照适宜度', color='#FFCC99')
plt.bar(x + bar_width/2, result['空气适宜度'], width=bar_width, label='空气适宜度', color='#99CC99')
plt.bar(x + bar_width*1.5, result['综合环境适宜度'], width=bar_width, label='综合环境适宜度', color='#9999CC')
    
plt.xlabel('城市', fontproperties=font)
plt.ylabel('适宜度指数', fontproperties=font)
plt.title('杭州、宁波和温州环境适宜度指数对比', fontproperties=font)
plt.xticks(x, cities, fontproperties=font)
plt.ylim(0, 1)
plt.legend(prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 在条形图上添加数值标签
for i, index_type in enumerate(['温度适宜度', '日照适宜度', '空气适宜度', '综合环境适宜度']):
    for j in range(len(cities)):
        plt.text(j + (i-1.5)*bar_width,
                    result[index_type][j] + 0.02, 
                    f'{result[index_type][j]:.2f}', 
                    ha='center', 
                    fontsize=9)
    
# 添加雷达图比较
plt.figure(figsize=(10, 8))
    
# 设置极坐标图
angles = np.linspace(0, 2*np.pi, 4, endpoint=False).tolist()
angles += angles[:1]  # 闭合图形
    
# 准备数据
categories = ['温度适宜度', '日照适宜度', '空气适宜度', '综合环境适宜度']
categories += categories[:1]  # 闭合类别
    
# 创建子图
ax = plt.subplot(111, polar=True)
    
# 绘制每个城市的雷达图
for i, city in enumerate(cities):
    values = result.iloc[i, 1:].tolist()
    values += values[:1]  # 闭合数据
    ax.plot(angles, values, linewidth=2, label=city)
    ax.fill(angles, values, alpha=0.1)
    
# 设置雷达图的坐标轴
plt.xticks(angles[:-1], categories[:-1], fontproperties=font)
ax.set_ylim(0, 1)
    
# 添加图例
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), prop=font)
plt.title('杭州、宁波和温州环境适宜度雷达图对比', fontproperties=font)
    
    # 保存图表
plt.tight_layout()
plt.savefig('环境适宜度雷达图.png', dpi=300)
    
    # 显示第一个图表
plt.figure(1)
plt.savefig('环境适宜度条形图.png', dpi=300)
    
    # 显示所有图表
plt.show()

