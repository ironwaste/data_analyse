import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.sans-serif'] = ['simHei']
excel_file = pd.ExcelFile('9-11 按地区分互联网主要指标发展情况（2023年）.xlsx')
sheet_name = excel_file.sheet_names
df = excel_file.parse(sheet_name[0])
df.columns = ['地区', '固定互联网宽带接入端口(万个)', '移动互联网用户(万户)', '移动互联网用户接入流量(万GB)', '(固定)互联网宽带接入用户(万户)']
df = df[2:]
df = df.reset_index(drop=True)
selected_cities = ['杭州市', '宁波市', '温州市']
selected_df = df[df['地区'].isin(selected_cities)]
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
bars_1 = axs[0, 0].bar(selected_df['地区'], selected_df['固定互联网宽带接入端口(万个)'])
axs[0, 0].set_title('固定互联网宽带接入端口(万个)')
for bar in bars_1:
    height = bar.get_height()
    axs[0, 0].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.1f}', ha='center', va='bottom')
bars_2 = axs[0, 1].bar(selected_df['地区'], selected_df['移动互联网用户(万户)'])
axs[0, 1].set_title('移动互联网用户(万户)')
for bar in bars_2:
    height = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.1f}', ha='center', va='bottom')
bars_3 = axs[1, 0].bar(selected_df['地区'], selected_df['移动互联网用户接入流量(万GB)'])
axs[1, 0].set_title('移动互联网用户接入流量(万GB)')
for bar in bars_3:
    height = bar.get_height()
    axs[1, 0].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.1f}', ha='center', va='bottom')
bars_4 = axs[1, 1].bar(selected_df['地区'], selected_df['(固定)互联网宽带接入用户(万户)'])
axs[1, 1].set_title('(固定)互联网宽带接入用户(万户)')
for bar in bars_4:
    height = bar.get_height()
    axs[1, 1].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.1f}', ha='center', va='bottom')
plt.tight_layout()
plt.show()