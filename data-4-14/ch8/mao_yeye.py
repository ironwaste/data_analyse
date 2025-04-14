import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from matplotlib.animation import FuncAnimation


# 1. 文本预处理
def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 清洗文本 - 移除换行符和多余空格
    text = text.replace('\n', ' ').replace('\r', ' ').strip()

    # 分词处理
    words = jieba.lcut(text)

    # 过滤单字
    words = [word for word in words if len(word) > 1]

    # 词频统计
    word_freq = Counter(words)
    return word_freq

# 2. 动态词云生成
def generate_dynamic_wordcloud(word_freq, output_path):
    # 颜色函数
    def random_color_func(word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):
        h = random_state.randint(0, 360)
        s = random_state.randint(70, 100)
        l = random_state.randint(40, 70)
        return f"hsl({h}, {s}%, {l}%)"

    # 创建词云对象
    wc = WordCloud(
        font_path='simhei.ttf',  # 使用黑体
        background_color='white',
        width=1000,  # 设置画布宽度
        height=700,  # 设置画布高度
        max_words=200,
        max_font_size=150,
        min_font_size=10,
        color_func=random_color_func
    )

    # 生成词云
    wc.generate_from_frequencies(word_freq)

    # 创建图形
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    img = ax.imshow(wc, interpolation='bilinear')

    # 动画更新函数
    def update(frame):
        # 每帧改变颜色和旋转角度
        current_wc = WordCloud(
            font_path='simhei.ttf',
            background_color='white',
            width=1000,
            height=700,
            max_words=200,
            max_font_size=150,
            min_font_size=10,
            color_func=random_color_func,
            prefer_horizontal=0.9 - frame * 0.01  # 动态调整词语方向
        )
        current_wc.generate_from_frequencies(word_freq)
        img.set_array(current_wc.to_array())
        return [img]

    # 创建动画
    ani = FuncAnimation(fig, update, frames=30, interval=200, blit=True)

    # 保存动态图
    ani.save(output_path, writer='pillow', fps=5, dpi=300)
    plt.close()


# 3. 主程序
if __name__ == "__main__":
    # 参数设置
    text_file = 'mao.txt'
    output_gif = 'mao_speech_wordcloud.gif'

    # 处理文本
    word_freq = process_text(text_file)

    # 生成动态词云
    generate_dynamic_wordcloud(word_freq, output_gif)

    print(f"动态词云已生成并保存为 {output_gif}")