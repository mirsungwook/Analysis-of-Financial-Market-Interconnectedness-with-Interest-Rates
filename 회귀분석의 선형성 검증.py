import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 데이터 로드 (가상의 데이터를 사용하므로 실제 데이터로 대체해야 합니다.)
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# 독립 변수(IR) 및 종속 변수(FOOD, MEDI, TRAFF, COMMU) 선택
independent_variable = 'IR'
dependent_variables = ['FOOD', 'MEDI', 'TRAFF', 'COMMU']

# 그래프 그리기
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(8, 16))  # 크기 조정

for i, dependent_variable in enumerate(dependent_variables):
    # 산점도 그리기
    sns.scatterplot(x=df[independent_variable], y=df[dependent_variable], ax=axes[i], label=dependent_variable)

    # 추세선 그리기
    trendline = np.polyfit(df[independent_variable], df[dependent_variable], 1)
    axes[i].plot(df[independent_variable], np.polyval(trendline, df[independent_variable]), color='red', label='Trendline')

    axes[i].set_title(f'{dependent_variable} vs. {independent_variable}')
    axes[i].set_xlabel(independent_variable)
    axes[i].set_ylabel(dependent_variable)
    axes[i].legend(loc='upper right')  # 범례 위치 우측 상단으로 변경

plt.tight_layout()
plt.subplots_adjust(hspace=0.6)  # 상하 간격 조절
plt.show()
