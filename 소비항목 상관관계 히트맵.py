import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
data = pd.read_excel('data.xlsx')

# 소비 항목 변수
selected_columns = ['FOOD', 'SMOKE', 'CLOTH', 'MC', 'HG', 'MEDI', 'TRAFF', 'COMMU', 'CULT', 'STUDY', 'DS', 'SERV']
selected_data = data[selected_columns]

# 변수들 간의 상관관계 계산
correlation_matrix = selected_data.corr()

# 상관관계 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
