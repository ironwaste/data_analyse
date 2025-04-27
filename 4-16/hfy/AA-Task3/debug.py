import pandas as pd
import plotly.express as px
import plotly.subplots as sp
from plotly.subplots import make_subplots
import plotly.graph_objects as go
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None) # 设置显示最大行
pd.set_option('display.max_colwidth',500000)
pd.set_option('display.width', 1000000) # 设置字符显示宽度

data_path = {
    '经济': '17-2 各市国民经济主要指标（2023年）.xlsx',
    '环境_气温': '13-5 主要城市平均气温（2023年）.xlsx',
    '环境_降水': '13-6 主要城市降水量（2023年）.xlsx',
    '环境_空气': '13-8 主要城市空气指标（2023年）.xlsx',
    '基础设施_教育': '17-20 各市各类学校在校生数（2023年）.xlsx',
    '基础设施_交通': '17-11 各市客运量和货运量（2023年）.xlsx',
    '社会文化': '17-22 各市文化和卫生事业主要指标（2023年）.xlsx',
    '生活便利_互联网': '9-11 按地区分互联网主要指标发展情况（2023年）.xlsx',
    '生活便利_ICT': '9-13 按地区分信息通信技术应用和数字化转型情况（2023年）.xlsx'
}

def load_data(file, sheet=0, skiprows=2, usecols=None):
    # 动态跳过表头行，确保列名正确读取
    df = pd.read_excel(file, sheet_name=sheet, skiprows=skiprows, usecols=usecols, header=0)

    # 统一处理列名：移除空格和特殊字符
    df.columns = df.columns.str.replace(r'[\s　]+', '', regex=True)
    if '城市' not in df.columns:
        # 尝试模糊匹配列名
        possible_columns = [col for col in df.columns if '市' in col]
        if possible_columns:
            df = df.rename(columns={possible_columns[0]: '城市'})
        else:
            raise KeyError(f"文件 {file} 中未找到有效的城市列")

    # 统一城市名称格式：移除所有空格并去掉末尾的"市"
    df['城市'] = df['城市'].str.replace(r'[\s　]+', '', regex=True).str.rstrip('市')
    allowed_cities = ['杭州', '宁波', '温州']
    df = df[df['城市'].isin(allowed_cities)]
    return df

# 重新加载数据
气温 = load_data(data_path['环境_气温'], usecols="A,N")
气温.columns = ['城市', '年平均气温']

降水 = load_data(data_path['环境_降水'], usecols="A,N")
降水.columns = ['城市', '年降水量']

空气 = load_data(data_path['环境_空气'], skiprows=1)
空气 = 空气[['城市', '细颗粒物(PM2.5)年平均浓度(微克/立方米)', '空气质量达到和好于二级的天数比例(%)']]
空气.columns = ['城市', 'PM2.5', '空气质量优良天数比例']

# 合并环境数据
环境 = pd.merge(气温, 降水, on='城市').merge(空气, on='城市')
print(环境)
