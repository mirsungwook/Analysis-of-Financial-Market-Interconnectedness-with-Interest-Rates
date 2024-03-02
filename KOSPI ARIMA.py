import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 데이터 불러오기
data = pd.read_excel("data.xlsx")

# 주제 금리(IR)와 KOSPI 시계열 데이터 선택
ir_series = data['IR']
kospi_series = data['KOSPI']

# ARIMA 모델 적용 
order = (1, 0, 2)  # (p, d, q) 값 설정
model = ARIMA(kospi_series, order=order)
results = model.fit()

# 모델 요약 정보 출력
print(results.summary())

# 예측 결과 시각화
plt.figure(figsize=(12, 6))
plt.plot(kospi_series, label='Observed')
plt.plot(results.fittedvalues, color='red', label='Fitted')
plt.title('ARIMA Model Fit for KOSPI')
plt.legend()
plt.show()
