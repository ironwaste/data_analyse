import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import os
import numpy as np
from PIL import Image
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import random
import imageio.v2 as imageio
import time

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

def generate_dynamic_wordcloud(csv_files, output_dir):
    """为所有CSV文件生成一个动态词云"""
    # 合并所有CSV文件的文本
    all_text = ""
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, encoding='utf-8-sig')
        # 假设第一列是内容列
        text = ' '.join(df.iloc[:, 0].dropna().astype(str).tolist())
        all_text += text + " "
    
    # 使用jieba进行中文分词
    words = ' '.join(jieba.cut(all_text))
    
    # 创建临时目录保存中间图片
    temp_dir = os.path.join(output_dir, 'temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 预定义颜色方案
    color_schemes = [
        {'background_color': 'white', 'colormap': 'viridis'},
        {'background_color': 'white', 'colormap': 'plasma'},
        {'background_color': 'white', 'colormap': 'inferno'},
        {'background_color': 'white', 'colormap': 'magma'},
        {'background_color': 'white', 'colormap': 'cividis'},
        {'background_color': 'black', 'colormap': 'viridis'},
        {'background_color': 'black', 'colormap': 'plasma'},
        {'background_color': 'black', 'colormap': 'inferno'},
        {'background_color': 'black', 'colormap': 'magma'}
    ]
    
    # 生成多个不同颜色的词云图片
    images = []
    for i, scheme in enumerate(color_schemes):
        # 创建词云
        wordcloud = WordCloud(
            font_path='simhei.ttf',  # 使用黑体字体，确保能显示中文
            width=800,
            height=600,
            background_color=scheme['background_color'],
            max_words=100,
            colormap=scheme['colormap'],
            collocations=False
        ).generate(words)
        
        # 保存图片
        temp_file = os.path.join(temp_dir, f'frame_{i}.png')
        wordcloud.to_file(temp_file)
        images.append(temp_file)
    
    # 使用imageio创建GIF
    output_file = os.path.join(output_dir, 'dynamic_wordcloud.gif')
    
    with imageio.get_writer(output_file, mode='I', duration=0.5) as writer:
        for image_path in images:
            image = imageio.imread(image_path)
            writer.append_data(image)
    
    print(f'已生成动态词云，保存为 {output_file}')
    
    # 删除临时文件
    for image_path in images:
        try:
            os.remove(image_path)
        except:
            pass
    try:
        os.rmdir(temp_dir)
    except:
        pass

def main():
    # 当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 创建输出目录
    output_dir = os.path.join(current_dir, 'wordcloud_images')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取当前目录下所有CSV文件
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
    csv_file_paths = [os.path.join(current_dir, f) for f in csv_files]
    
    # 为每个CSV文件生成词云
    for csv_file in csv_files:
        csv_file_path = os.path.join(current_dir, csv_file)
        generate_wordcloud(csv_file_path, output_dir)
    
    # 生成动态词云
    if csv_file_paths:
        generate_dynamic_wordcloud(csv_file_paths, output_dir)

if __name__ == '__main__':
    main()
