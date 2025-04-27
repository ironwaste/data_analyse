import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
excel_file = pd.ExcelFile('4-5 各市、县居民消费价格指数（2023年）.xlsx')
# 获取所有表名
sheet_name = excel_file.sheet_names

# 读取表格的数据
df = excel_file.parse('4-5 各市、县居民消费价格指数（2023年）')
df.columns = ['市（县）名称', '居民消费价格指数', '食品烟酒', '食品烟酒_食品', '食品烟酒_食品_粮食', '食品烟酒_食品_菜', '食品烟酒_食品_畜肉类', '食品烟酒_食品_禽肉类', '食品烟酒_食品_水产品', '食品烟酒_食品_蛋类', '食品烟酒_食品_奶类', '衣着', '居住', '生活用品及服务', '交通和通信', '教育文化和娱乐', '医疗保健', '其他用品和服务']
df = df[4:]
df = df.reset_index(drop=True)
df['居民消费价格指数'] = pd.to_numeric(df['居民消费价格指数'])
selected_cities = ['杭州市', '宁波市', '温州市']
selected_df = df[df['市（县）名称'].isin(selected_cities)]
plt.figure(figsize=(8, 6))
bars = plt.bar(selected_df['市（县）名称'], selected_df['居民消费价格指数'])
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             '%.2f' % height,
             ha='center', va='bottom')
plt.title('宁波、杭州和温州居民消费价格指数')
plt.xlabel('市名称')
plt.ylabel('居民消费价格指数')
plt.show()