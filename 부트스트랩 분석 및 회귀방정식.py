import statsmodels.api as sm
import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
from sklearn.utils import resample
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# 데이터 불러오기
data = pd.read_excel('data.xlsx')

# 종속 변수와 독립 변수 선택
y_columns = ['FOOD', 'MEDI', 'TRAFF', 'COMMU']
X_column = 'IR'

# 부트스트랩 분석 수행
n_iterations = 100  # 부트스트랩 샘플링 횟수
coefs = {column: [] for column in y_columns}  # 종속 변수별 회귀 계수 저장 딕셔너리
r_squared_values = {column: [] for column in y_columns}  # 종속 변수별 설명력 저장 딕셔너리
equations = {column: {'formula': '', 'R-squared': None, 'p-value': None} for column in y_columns}  # 회귀 방정식 정보 저장

for _ in range(n_iterations):
    # 부트스트랩 샘플 생성
    bootstrap_sample = resample(data)

    for column in y_columns:
        # 회귀 모델 구축
        X = bootstrap_sample[X_column]
        X = sm.add_constant(X)  # 상수 항 추가
        bootstrap_model = OLS(bootstrap_sample[column], X).fit()

        # 추정된 회귀 계수 및 R-squared 저장
        coef_dict = {'Intercept': bootstrap_model.params[0]}
        coef_dict[column] = bootstrap_model.params[1]
        
        # 모델에서 rsquared 및 p-value 속성 계산
        ssr = np.sum(bootstrap_model.resid ** 2)
        tss = np.sum((bootstrap_sample[column] - bootstrap_sample[column].mean()) ** 2)
        r_squared = 1 - ssr / tss
        p_value = bootstrap_model.pvalues[1]  # 독립 변수의 p-value

        coef_dict['R-squared'] = r_squared
        coefs[column].append(coef_dict)
        r_squared_values[column].append(r_squared)
        
        # 회귀 방정식 정보 저장
        equation_formula = f"{column} = {coef_dict['Intercept']:.4f} + {coef_dict[column]:.4f} * {X_column}"
        equations[column]['formula'] = equation_formula
        equations[column]['R-squared'] = r_squared
        equations[column]['p-value'] = p_value

# 각 종속 변수별 부트스트랩 결과를 DataFrame으로 변환
bootstrap_results = {column: pd.DataFrame(values) for column, values in coefs.items()}

# 각 종속 변수별 설명력(R-squared) 및 회귀 방정식 출력
print("\nRegression Equations and Statistics:")
for column in y_columns:
    print(f"\n{column} Regression Equation:")
    print(equations[column]['formula'])
    print(f"R-squared: {equations[column]['R-squared']:.4f}")
    print(f"p-value: {equations[column]['p-value']:.4f}")

# 각 종속 변수별 부트스트랩 결과의 신뢰구간 계산
confidence_intervals = {column: result_df.quantile([0.05, 0.95]) for column, result_df in bootstrap_results.items()}
print("\nConfidence Intervals:")
for column, interval_df in confidence_intervals.items():
    print(f"\n{column} Confidence Intervals:")
    print(interval_df)

# 회귀 계수의 분포 및 신뢰 구간 시각화
plt.figure(figsize=(12, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
for i, column in enumerate(y_columns, 1):
    plt.subplot(2, 2, i)
    
    # 95% 신뢰구간 영역
    lower_bound = confidence_intervals[column].loc[0.05][column]
    upper_bound = confidence_intervals[column].loc[0.95][column]
    
    plt.hist(bootstrap_results[column][column], bins=30, edgecolor='black', alpha=0.7)
    
    # 95% 신뢰구간 영역에 배경색 적용
    plt.axvspan(lower_bound, upper_bound, facecolor='lightcoral', alpha=0.3)
    
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
