import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import os
import numpy as np
from PIL import Image

def generate_wordcloud(csv_file, output_dir):
    # 提取文件名（不含扩展名）作为保存图片的名称
    file_name = os.path.splitext(os.path.basename(csv_file))[0]
    
    # 读取CSV文件
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
    
    # 将所有文本内容合并成一个字符串
    # 假设第一列是内容列
    text = ' '.join(df.iloc[:, 0].dropna().astype(str).tolist())
    
    # 使用jieba进行中文分词
    words = ' '.join(jieba.cut(text))
    
    # 生成词云
    wordcloud = WordCloud(
        font_path='simhei.ttf',  # 使用黑体字体，确保能显示中文
        width=800,
        height=600,
        background_color='white',
        max_words=200,
        collocations=False,
        contour_width=1,
        contour_color='steelblue'
    )
    
    # 生成词云图
    wordcloud.generate(words)
    
    # 显示词云图
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    
    # 保存图片
    output_file = os.path.join(output_dir, f'{file_name}_wordcloud.png')
    plt.savefig(output_file, dpi=300)
    plt.close()
    
    print(f'已生成 {file_name} 的词云图，保存为 {output_file}')

def main():
    # 当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 创建输出目录
    output_dir = os.path.join(current_dir, 'wordcloud_images')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取当前目录下所有CSV文件
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
    
    # 为每个CSV文件生成词云
    for csv_file in csv_files:
        csv_file_path = os.path.join(current_dir, csv_file)
        generate_wordcloud(csv_file_path, output_dir)

if __name__ == '__main__':
    main()
