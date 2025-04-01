import test_stationarity
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # 添加 matplotlib.pyplot 导入
from statsmodels.tsa.arima.model import ARIMA
df = pd.read_csv(r'D:\schoolzwu\AI\machine-study\data_analyse\3-30\Report7-AirPassengers.csv', encoding='utf-8', index_col='Month')
df.index = pd.to_datetime(df.index)  # 添加频率信息
ts = df['#Passengers']  # 生成pd.Series对象

ts_log = np.log(ts)
# 差分
# diff_12 = ts_log.diff(12)
# diff_12.dropna(inplace=True)
# diff_12_1 = diff_12.diff(1)
# diff_12_1.dropna(inplace=True)
# test_stationarity.draw_ts(diff_12)
# print(test_stationarity.testStationarity(diff_12_1))

# 分解
# from statsmodels.tsa.seasonal import seasonal_decompose
# decomposition = seasonal_decompose(ts_log, model="additive")

# trend = decomposition.trend
# seasonal = decomposition.seasonal
# residual = decomposition.resid

# test_stationarity.draw_ts(ts_log)
# from statsmodels.tsa.seasonal import seasonal_decompose
# decomposition = seasonal_decompose(ts_log, model="additive")
#
# trend = decomposition.trend
# seasonal = decomposition.seasonal
# residual = decomposition.resid
# # test_stationarity.draw_trend(ts_log, 12)
#
rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
print(test_stationarity.testStationarity(ts_diff_1))
#
ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)

# model = ARMA(ts_diff_2, order=(1, 1))
# result_arma = model.fit( disp=-1, method='css')
#
# 差分操作
def diff_ts(ts, d):
    global shift_ts_list
    #  动态预测第二日的值时所需要的差分序列
    global last_data_shift_list
    shift_ts_list = []
    last_data_shift_list = []
    tmp_ts = ts
    for i in d:
        last_data_shift_list.append(tmp_ts[-i])
        print(last_data_shift_list)
        shift_ts = tmp_ts.shift(i)
        shift_ts_list.append(shift_ts)
        tmp_ts = tmp_ts - shift_ts
    tmp_ts.dropna(inplace=True)
    return tmp_ts


# 还原操作
def predict_diff_recover(predict_value, d):
    if isinstance(predict_value, float):
        tmp_data = predict_value
        for i in range(len(d)):
            tmp_data = tmp_data + last_data_shift_list[-i-1]
    elif isinstance(predict_value, np.ndarray):
        tmp_data = predict_value[0]
        for i in range(len(d)):
            tmp_data = tmp_data + last_data_shift_list[-i-1]
    else:
        tmp_data = predict_value
        for i in range(len(d)):
            try:
                tmp_data = tmp_data.add(shift_ts_list[-i-1])
            except:
                raise ValueError('What you input is not pd.Series type!')
        tmp_data.dropna(inplace=True)
    return tmp_data

# rol_mean = ts_log.rolling(window=12).mean()
# rol_mean.dropna(inplace=True)
# ts_diff_1 = rol_mean.diff(1)
# ts_diff_1.dropna(inplace=True)
# test_stationarity.testStationarity(ts_diff_1)

# diffed_ts = diff_ts(ts_log, d=[12, 1])
# model = arima_model(diffed_ts)
# model.certain_model(1, 1)
# predict_ts = model.properModel.predict()
# diff_recover_ts = predict_diff_recover(predict_ts, d=[12, 1])
# log_recover = np.exp(diff_recover_ts)



model = ARIMA(ts_diff_2, order=(1, 1, 0))  
# order=(p,d,q) 其中 p=1 是 AR 阶数，d=1 是差分阶数，q=1 是 MA 阶数
result_arma = model.fit()
predict_ts = result_arma.predict()
# 一阶差分还原
diff_shift_ts = ts_diff_1.shift(1)
diff_recover_1 = predict_ts.add(diff_shift_ts)
# 再次一阶差分还原
rol_shift_ts = rol_mean.shift(1)
diff_recover = diff_recover_1.add(rol_shift_ts)
# 移动平均还原
rol_sum = ts_log.rolling(window=11).sum()
rol_recover = diff_recover*12 - rol_sum.shift(1)
# 对数还原
log_recover = np.exp(rol_recover)
log_recover.dropna(inplace=True)

ts = ts[log_recover.index]  # 过滤没有预测的记录
plt.figure(facecolor='white')
log_recover.plot(color='blue', label='Predict')
ts.plot(color='red', label='Original')
plt.legend(loc='best')
plt.title('RMSE: %.4f'% np.sqrt(sum((log_recover-ts)**2)/ts.size))
plt.show()



from dateutil.relativedelta import relativedelta
def _add_new_data(ts, dat, type='day'):
    if type == 'day':
        new_index = ts.index[-1] + relativedelta(days=1)
    elif type == 'month':
        new_index = ts.index[-1] + relativedelta(months=1)
    ts[new_index] = dat

def add_today_data(model, ts,  data, d, type='day'):
    _add_new_data(ts, data, type)  # 为原始序列添加数据
    # 为滞后序列添加新值
    d_ts = diff_ts(ts, d)
    model.add_today_data(d_ts[-1], type)

def forecast_next_day_data(model, type='day'):
    if model == None:
        raise ValueError('No model fit before')
    fc = model.forecast_next_day_value(type)
    return predict_diff_recover(fc, [12, 1])

ts_train = ts_log[:'1956-12']
ts_test = ts_log['1957-1':]

diffed_ts = diff_ts(ts_train, [12, 1])
forecast_list = []

for i, dta in enumerate(ts_test):
    if i%7 == 0:
        model = arima_model(diffed_ts)
        model.certain_model(1, 1)
    forecast_data = forecast_next_day_data(model, type='month')
    forecast_list.append(forecast_data)
    add_today_data(model, ts_train, dta, [12, 1], type='month')

predict_ts = pd.Series(data=forecast_list, index=ts['1957-1':].index)
log_recover = np.exp(predict_ts)
original_ts = ts['1957-1':]

