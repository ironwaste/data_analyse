import numpy as np
import pandas as pd
import os

# 读取CSV文件
df = pd.read_csv('小说.csv')

# 将第一列为空的部分用第二列补充
df.iloc[:, 0] = df.iloc[:, 0].fillna(df.iloc[:, 1])

# 将第三列为空的部分用第四列补充
df.iloc[:, 2] = df.iloc[:, 2].fillna(df.iloc[:, 3])

# 删除第二列和第四列
df = df.drop(df.columns[[1, 3]], axis=1)

# 对数据进行去重
df = df.drop_duplicates()

# 根据观察可以得出，从第二章开始第一列内容为一些广告和其他的奇怪内容
# 所以我们直接将其赋值并且将 第二列内容删除
# 最后形成的格式就是第一列为 内容
# 而第二列为作评名称
# 第三列是章节名称
df.iloc[130:,0] = df.iloc[130:,1]
df = df.drop(df.columns[[1]],axis=1)
df = df.drop_duplicates()

# 创建保存文件的目录
output_dir = 'processed_novels'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 根据作者名称分组并分别保存
for author, group in df.groupby(df.columns[1]):  # 按第二列（作品名称）分组
    # 清理文件名中的非法字符
    safe_author_name = "".join(x for x in author if x.isalnum() or x in (' ', '-', '_', '@'))
    output_file = os.path.join(output_dir, f'{safe_author_name}.csv')
    group.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f'已保存作者 {author} 的作品到 {output_file}')

print("所有数据处理完成！")




