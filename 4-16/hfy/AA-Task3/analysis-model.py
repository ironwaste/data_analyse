import numpy as np
from scipy.stats import spearmanr

# 提取杭州、温州、宁波的数据，并按维度整理
data = {
    '经济': {
        '杭州': {
            '就业人员': 770.02,  # 2023年数据
            '消费价格指数': 100.2,
            '人均生活消费支出': 58879,  # 2023年城镇居民数据
            '国民经济主要指标': 20768.46  # 2023年GDP数据
        },
        '温州': {
            '就业人员': 555.36,
            '消费价格指数': 100.5,
            '人均生活消费支出': 45356,
            '国民经济主要指标': 8029.86
        },
        '宁波': {
            '就业人员': 607.38,
            '消费价格指数': 100.4,
            '人均生活消费支出': 56564,
            '国民经济主要指标': 15704.33
        }
    },
    '环境': {
        '杭州': {
            '平均气温': 18.7,
            '降水量': 1335.4,
            '日照时数': 1440.0,
            '空气指标': 89.7
        },
        '温州': {
            '平均气温': 19.2,
            '降水量': 1736.2,
            '日照时数': 1461.6,
            '空气指标': 92.3
        },
        '宁波': {
            '平均气温': 18.5,
            '降水量': 1313.0,
            '日照时数': 1541.6,
            '空气指标': 90.2
        }
    },
    '基础设施': {
        '杭州': {
            '学校在校生': 217.44,
            '客运量': 11320
        },
        '温州': {
            '学校在校生': 166.43,
            '客运量': 6336
        },
        '宁波': {
            '学校在校生': 137.03,
            '客运量': 7235
        }
    },
    '社会文化': {
        '杭州': {
            '文化和卫生事业主要指标': 5348
        },
        '温州': {
            '文化和卫生事业主要指标': 2427
        },
        '宁波': {
            '文化和卫生事业主要指标': 3336
        }
    },
    '生活便利维度': {
        '杭州': {
            '互联网主要指标': 2222.22,
            '信息通信技术': 1684.21
        },
        '温州': {
            '互联网主要指标': 504.62,
            '信息通信技术': 442.11
        },
        '宁波': {
            '互联网主要指标': 867.57,
            '信息通信技术': 631.58
        }
    }
}
# 设计权重分配方案（这里简单假设各维度内指标等权重，各维度权重根据经验设定）
weights = {
    '经济': 0.4,
    '环境': 0.2,
    '基础设施': 0.15,
    '社会文化': 0.15,
    '生活便利维度': 0.1
}
# 计算各城市各维度得分
city_scores = {}
for city in ['杭州', '温州', '宁波']:
    city_scores[city] = {}
    for dimension in weights.keys():
        num_metrics = len(data[dimension][city])
        dimension_weight = weights[dimension]
        metric_weight = dimension_weight / num_metrics
        dimension_score = 0
        for metric in data[dimension][city].keys():
            dimension_score += metric_weight * data[dimension][city][metric]
        city_scores[city][dimension] = dimension_score
# 计算各城市综合得分
city_overall_scores = {}
for city in city_scores.keys():
    overall_score = 0
    for dimension in city_scores[city].keys():
        overall_score += city_scores[city][dimension]
    city_overall_scores[city] = overall_score
print("各城市各维度得分：")
for city in city_scores.keys():
    print(city, city_scores[city])
print("\n各城市综合得分：")
for city in city_overall_scores.keys():
    print(city, city_overall_scores[city])
# 进行敏感性分析（改变权重，看综合得分排名是否稳定）
num_trials = 100  # 试验次数
stability_count = 0  # 排名稳定的次数
original_ranking = np.argsort(list(city_overall_scores.values()))[::-1]
for _ in range(num_trials):
    # 随机生成权重（各维度权重在±20%范围内变动）
    new_weights = {}
    for dimension in weights.keys():
        new_weight = weights[dimension] * (1 + np.random.uniform(-0.2, 0.2))
        new_weights[dimension] = new_weight
    total_weight = sum(new_weights.values())
    for dimension in new_weights.keys():
        new_weights[dimension] = new_weights[dimension] / total_weight
    # 重新计算各城市综合得分
    new_city_overall_scores = {}
    for city in city_scores.keys():
        new_overall_score = 0
        for dimension in city_scores[city].keys():
            new_overall_score += new_weights[dimension] * city_scores[city][dimension]
        new_city_overall_scores[city] = new_overall_score
    new_ranking = np.argsort(list(new_city_overall_scores.values()))[::-1]
    # 计算斯皮尔曼等级相关系数
    rho, p_value = spearmanr(original_ranking, new_ranking)
    if rho > 0.8 and p_value < 0.05:  # 假设相关系数大于0.8且p值小于0.05认为排名稳定
        stability_count += 1
stability_ratio = stability_count / num_trials
print(f"\n敏感性分析结果：排名稳定的比例为 {stability_ratio * 100:.2f}%")