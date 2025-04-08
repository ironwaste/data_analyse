import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree
from sklearn.tree import plot_tree

# 加载数据
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# 删除含有空值的行
data = data.dropna()

# 映射职业
occupation_map = {
    'Accountant': 1, 'Doctor': 2, 'Engineer': 3, 'Lawyer': 4,
    'Manager': 5, 'Nurse': 6, 'Sales Representative': 7, 'Salesperson': 8,
    'Scientist': 9, 'Software Engineer': 10, 'Teacher': 11
}
data['Occupation'] = data['Occupation'].map(occupation_map)

# 映射性别
data['Gender'] = data['Gender'].map({'Female': 0, 'Male': 1})

# 映射BMI类别
bmi_map = {
    'Normal': 1, 'Normal Weight': 2, 'Obese': 3, 'Overweight': 4
}
data['BMI Category'] = data['BMI Category'].map(bmi_map)

# 拆分血压数据
data[['Systolic', 'Diastolic']] = data['Blood Pressure'].str.split('/', expand=True)
data['Systolic'] = data['Systolic'].astype(float)
data['Diastolic'] = data['Diastolic'].astype(float)
data = data.drop(['Blood Pressure'], axis=1)

# 特征和目标变量
X = data.drop('Sleep Disorder', axis=1)  # 特征
y = data['Sleep Disorder']  # 目标变量

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树分类器

# 基础模型
#clf = DecisionTreeClassifier(random_state=42)
# 使用信息增益作为分割标准
#clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
# 限制树的最大深度
#clf = DecisionTreeClassifier(max_depth=5, random_state=42)
# 限制寻找最佳分割时要考虑的特征数量
#clf = DecisionTreeClassifier(max_features='sqrt', random_state=42)
# 限制内部节点再划分所需最小样本数
#clf = DecisionTreeClassifier(min_samples_split=10, random_state=42)
# 使用随机分割而不是最佳分割
#clf = DecisionTreeClassifier(splitter='random', random_state=42)
# 组合多个参数
clf= DecisionTreeClassifier(
    criterion='entropy',
    max_depth=4,
    min_samples_split=8,
    min_samples_leaf=4,
    max_features='log2',
    random_state=42
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 评估模型
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)

# 绘制混淆矩阵
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# 绘制决策树
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True)
plt.show()

# 获取特征重要性
importances = clf.feature_importances_

# 排序特征重要性
indices = np.argsort(importances)[::-1]

# 绘制特征重要性图
plt.figure(figsize=(12, 6))
plt.title('Feature Importances')
plt.bar(range(X_train.shape[1]), importances[indices], color='lightblue', align='center')
plt.xticks(range(X_train.shape[1]), X.columns[indices], rotation=45)
plt.xlim([-1, X_train.shape[1]])
plt.show()