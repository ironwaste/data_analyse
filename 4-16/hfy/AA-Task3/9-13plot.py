import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
excel_file = pd.ExcelFile('9-13 按地区分信息通信技术应用和数字化转型情况（2023年）.xlsx')
sheet_name = excel_file.sheet_names
df = excel_file.parse(sheet_name[0])
df.columns = ['行业', '企业数(个)', '期末使用计算机数(台)', '每百人使用计算机数(台)', '企业拥有网站数(个)', '每百家企业拥有网站数(个)', '有电子商务交易活动_企业数(个)', '有电子商务交易活动_比重(%)', '电子商务销售额(亿元)', '电子商务采购额(亿元)']
df = df[4:14]
df = df.reset_index(drop=True)
selected_cities = ['杭州市', '宁波市', '温州市']
selected_df = df[df['行业'].isin(selected_cities)]
fig, axes = plt.subplots(5, 2, figsize=(15, 20))
metrics = ['企业数(个)', '期末使用计算机数(台)', '每百人使用计算机数(台)', '企业拥有网站数(个)', '每百家企业拥有网站数(个)', '有电子商务交易活动_企业数(个)', '有电子商务交易活动_比重(%)', '电子商务销售额(亿元)', '电子商务采购额(亿元)']
for i, metric in enumerate(metrics):
    row = i // 2
    col = i % 2
    axes[row, col].bar(selected_df['行业'], selected_df[metric])
    axes[row, col].set_title(metric)
    axes[row, col].set_xlabel('城市')
    axes[row, col].set_ylabel(metric.split('(')[0])
    for bar in axes[row, col].patches:
        height = bar.get_height()
        axes[row, col].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()
