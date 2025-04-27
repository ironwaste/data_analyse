import pandas as pd
import plotly.express as px
import plotly.subplots as sp
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 读取所有数据表（替换为实际文件路径）
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


# 数据预处理函数
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


# --------------------------
# 经济维度
# --------------------------
经济 = load_data(data_path['经济'], skiprows=1, usecols="A,H,I,P,Q")
# 经济 = pd.read_excel(data_path['经济'],skiprows=1,usecols="A,B,G,H,M,O,P")
经济 = 经济.rename(columns={
    '人均生产总值(元)': '人均GDP',
    '社会消费品零售总额(亿元)': '消费总额',
    '城镇居民人均可支配收入(元)': '城镇居民收入',
    '农村居民人均可支配收入(元)': '农村居民收入'
})



# --------------------------
# 环境维度
# --------------------------
# 气温
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

# --------------------------
# 基础设施维度
# --------------------------
教育 = load_data(data_path['基础设施_教育'],skiprows=1)
教育 = 教育.rename(columns={'普通中学(万人)': '普通中学在校生', '小学(万人)': '小学在校生'})


交通 = load_data(data_path['基础设施_交通'],skiprows=1)
交通.rename(columns={'客运量(万人)':'公路、水路','Unnamed:2':'轨道交通（万人次）','Unnamed:3':'航空','货运量(万吨)':'公路、水路.1','Unnamed:5':'航空.1'},inplace=True)
交通 = 交通[['城市', '公路、水路' , '轨道交通（万人次）', '航空']]  # 选取关键指标

# --------------------------
# 社会文化维度
# --------------------------
文化卫生 = load_data(data_path['社会文化'],skiprows=1)
文化卫生 = 文化卫生.rename(columns={
    '博物馆数（个）': '博物馆数量',
    '医院床位数(张)': '医院床位数',
    '医生数(人)': '医生数量'
})
# --------------------------
# 生活便利维度
# --------------------------
互联网 = load_data(data_path['生活便利_互联网'],skiprows=1)
互联网 = 互联网.rename(columns={
    '移动互联网用户(万户)': '移动互联网用户',
    '（固定）互联网宽带接入用户(万户)': '宽带用户'
})


ICT = load_data(data_path['生活便利_ICT'],skiprows=1)
ICT = ICT[['城市', '每百人使用计算机数(台)', '每百家企业拥有网站数(个)']]


# --------------------------
# 可视化
# --------------------------
def create_visualization():
    # 调整子图布局为4行2列
    fig = make_subplots(
        rows=4, cols=2,
        specs=[
            [{"type": "bar"}, {"type": "bar"}],  # 经济与环境指标分两列
            [{"type": "bar"}, {"type": "bar"}],  # 基础设施
            [{"type": "bar"}, {"type": "bar"}],  # 社会文化
            [{"type": "bar"}, {"type": "bar"}],  # 生活便利
        ],
        subplot_titles=(
            "经济指标对比", "环境指标-气温与降水",
            "教育基础设施", "交通基础设施",
            "医疗资源", "文化资源",
            "互联网普及", "数字化程度"
        )
    )

    # 经济指标 (第一行左)
    metrics = ['人均GDP', '消费总额', '城镇居民收入']
    for metric in metrics:
        fig.add_trace(
            go.Bar(x=经济['城市'], y=经济[metric], name=metric),
            row=1, col=1
        )

    # 环境指标 (第一行右)
    fig.add_trace(
        go.Bar(x=环境['城市'], y=环境['年平均气温'], name='年平均气温(℃)'),
        row=1, col=2
    )
    fig.add_trace(
        go.Bar(x=环境['城市'], y=环境['年降水量'], name='年降水量(mm)'),
        row=1, col=2
    )

    # 教育基础设施 (第二行左)
    fig.add_trace(
        go.Bar(x=教育['城市'], y=教育['普通中学在校生'], name='普通中学在校生(万人)'),
        row=2, col=1
    )

    # 交通基础设施 (第二行右)
    fig.add_trace(
        go.Bar(x=交通['城市'], y=交通['轨道交通（万人次）'], name='轨道交通客运量'),
        row=2, col=2
    )

    # 医疗资源 (第三行左)
    fig.add_trace(
        go.Bar(x=文化卫生['城市'], y=文化卫生['医院床位数'], name='医院床位数'),
        row=3, col=1
    )

    # 文化资源 (第三行右)
    fig.add_trace(
        go.Bar(x=文化卫生['城市'], y=文化卫生['博物馆数量'], name='博物馆数量'),
        row=3, col=2
    )

    # 互联网普及 (第四行左)
    fig.add_trace(
        go.Bar(x=互联网['城市'], y=互联网['移动互联网用户'], name='移动互联网用户(万户)'),
        row=4, col=1
    )

    # 数字化程度 (第四行右)
    fig.add_trace(
        go.Bar(x=ICT['城市'], y=ICT['每百人使用计算机数(台)'], name='每百人计算机数'),
        row=4, col=2
    )

    # 调整布局
    fig.update_layout(
        height=1600,
        width=1200,
        title_text="杭州、宁波、温州宜居性对比分析",
        showlegend=True,
        barmode='group'  # 同类指标分组显示
    )
    fig.show()


# 执行可视化
create_visualization()