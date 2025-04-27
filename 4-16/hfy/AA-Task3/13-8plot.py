import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('13-8 主要城市空气指标（2023年）.xlsx')
df = excel_file.parse('13-8 主要城市空气指标（2023年）', header=1)
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
selected_df = df.loc[1:3]
selected_df.set_index('城市', inplace=True)
plt.figure(figsize=(15, 8))
ax = selected_df.plot(kind='bar')
plt.title('杭州、温州、宁波2023年空气指标对比')
plt.xlabel('城市')
plt.ylabel('指标值')
plt.xticks(rotation=45)
ax.legend(bbox_to_anchor=(1, 0.95), loc='upper right')
plt.tight_layout()
plt.show()