import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import cnmaps
import geopandas as gpd
from shapely.geometry import shape

# 读取数据
df = pd.read_csv("./中国地震台数据.csv")
df = df.iloc[:,0:6]
df.drop_duplicates(inplace=True)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形
plt.figure(figsize=(15, 10))

# 获取中国地图数据
china_shapes = cnmaps.get_adm_maps(level='国')
# 提取geometry对象并转换为shapely几何对象
geometries = [shape(item['geometry'].__geo_interface__) for item in china_shapes]
china_gdf = gpd.GeoDataFrame(geometry=geometries, crs="EPSG:4326")

# 绘制中国地图底图
china_gdf.plot(color='lightgray', edgecolor='black', alpha=0.5)

# 创建热力图
x = df['经度'].values
y = df['纬度'].values
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='YlOrRd', alpha=0.6)

# 绘制散点图
scatter = plt.scatter(df['经度'], df['纬度'], 
                     c=df['震级'], 
                     cmap='YlOrRd',
                     s=df['震级']*10,  # 点的大小根据震级变化
                     alpha=0.6)

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('震级')

# 设置图表属性
plt.title('中国地震分布图')
plt.xlabel('经度')
plt.ylabel('纬度')

# 设置坐标轴范围
plt.xlim(73, 135)
plt.ylim(18, 54)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()

# 保存图片
# plt.savefig('地震分布图.png', dpi=300, bbox_inches='tight')



