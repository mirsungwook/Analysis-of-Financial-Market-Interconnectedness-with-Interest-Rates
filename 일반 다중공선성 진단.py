# 실험 2- 종속변수의 다중공선성 진단
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 데이터 불러오기
data = pd.read_excel('data.xlsx')

# 분석에 사용할 변수 선택
selected_columns = ['FOOD', 'MEDI', 'TRAFF', 'COMMU', 'CULT', 'STUDY']
selected_data = data[selected_columns]

# VIF 계산
vif_data = pd.DataFrame()
vif_data["Variable"] = selected_columns
vif_data["VIF"] = [variance_inflation_factor(selected_data.values, i) for i in range(selected_data.shape[1])]

# 결과 출력
print(vif_data)
