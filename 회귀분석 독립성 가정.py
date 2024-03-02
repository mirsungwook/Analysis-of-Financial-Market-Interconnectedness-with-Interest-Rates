import pandas as pd
import statsmodels.api as sm

# 데이터 불러오기
data = pd.read_excel('data.xlsx')

# 종속 변수와 독립 변수 선택
y_columns = ['FOOD', 'MEDI', 'TRAFF', 'COMMU']
X_column = 'IR'

# 더빈-왓슨 통계량 계산
for column in y_columns:
    X = data[X_column]
    X = sm.add_constant(X)  # 상수 항 추가
    model = sm.OLS(data[column], X).fit()
    
    # 더빈-왓슨 통계량 계산
    durbin_watson_statistic = sm.stats.durbin_watson(model.resid)
    
    # 결과 출력
    print(f"{column} vs. {X_column} 더빈-왓슨 통계량 = {durbin_watson_statistic:.4f}")
