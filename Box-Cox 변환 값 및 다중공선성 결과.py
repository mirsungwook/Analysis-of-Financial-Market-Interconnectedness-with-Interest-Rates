import pandas as pd
from scipy.stats import boxcox
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 데이터 불러오기
data = pd.read_excel('data.xlsx')

# 변환된 데이터 저장
transformed_data = pd.DataFrame()

# Box-Cox 변환을 적용할 변수 선택
selected_columns = ['FOOD', 'MEDI', 'TRAFF', 'COMMU', 'CULT', 'STUDY']

# 선택된 변수에 대해 Box-Cox 변환 수행 및 변환된 값 출력
for column in selected_columns:
    transformed_column, _ = boxcox(data[column])
    transformed_data[column] = transformed_column
    print(f"{column} 변환된 값:\n{transformed_column}\n")

# 다중공선성 계산
vif_data = pd.DataFrame()
vif_data["Variable"] = transformed_data.columns
vif_data["VIF"] = [round(variance_inflation_factor(transformed_data.values, i), 3) for i in range(transformed_data.shape[1])]

# 결과 출력
print("다중공선성 진단 결과:")
print(vif_data)
