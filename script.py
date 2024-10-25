import pandas as pd
import matplotlib.pyplot as plt

# 示例数据集 URL
data_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

# 读取数据
df = pd.read_csv(data_url)

# 简单的可视化
df['Survived'].value_counts().plot(kind='bar')
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()
