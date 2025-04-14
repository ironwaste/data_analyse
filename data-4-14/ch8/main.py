import jieba
import pandas as pd
from nltk import FreqDist
from matplotlib import pyplot as plt
from wordcloud import WordCloud

file_path = open('./商品评价信息.csv')
file_data = pd.read_csv(file_path)
# print(file_data)
file_data.drop(file_data[file_data['评价信息'] == '此用户没有填写评价。'].index,inplace=True)
# print(file_data)

cut_words = jieba.lcut(str(file_data['评价信息'].values),cut_all = False)
print(cut_words)

stop_path = open('./停用词表.txt',encoding='utf-8')
stop_words =stop_path.read()

new_data = []
for word in cut_words :
    if word not in stop_words :
        new_data.append(word)

print(new_data)

freq_list = FreqDist(new_data)

most_common_words = freq_list.most_common()
print(most_common_words)

font = r'C:\Windows\Fonts\STXINGKA.TTF'
wc = WordCloud(font_path = font, background_color = 'white',width = 1000,height = 800).generate(" ".join(new_data))
plt.imshow(wc)
plt.axis('off')
plt.show()


