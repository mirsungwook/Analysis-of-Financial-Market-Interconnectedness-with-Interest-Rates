import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 데이터 불러오기
data = pd.read_excel("data.xlsx")

# 주제 금리(IR)와 KOSPI, PIR 시계열 데이터 선택
ir_series = data['IR']
kospi_series = data['KOSPI']
pir_series = data['PIR']

# KOSPI에 대한 ARIMA 모델 적용 
kospi_order = (1, 0, 2)  # (p, d, q) 값 설정
kospi_model = ARIMA(kospi_series, order=kospi_order)
kospi_results = kospi_model.fit()

# PIR에 대한 ARIMA 모델 적용
pir_order = (2, 0, 2)  # (p, d, q) 값 설정
pir_model = ARIMA(pir_series, order=pir_order)
pir_results = pir_model.fit()

# 그래프의 크기 설정
plt.figure(figsize=(12, 12))

# 첫 번째 그래프 (KOSPI)
plt.subplot(2, 1, 1)
plt.plot(kospi_series, label='Observed')
plt.plot(kospi_results.fittedvalues, color='red', label='Fitted')
plt.title('ARIMA Model Fit for KOSPI')
plt.legend()

# 두 번째 그래프 (PIR)
plt.subplot(2, 1, 2)
plt.plot(pir_series, label='Observed')
plt.plot(pir_results.fittedvalues, color='red', label='Fitted')
plt.title('ARIMA Model Fit for PIR')
plt.legend()

# 간격 조정
plt.subplots_adjust(top=0.9)

# 그래프 보이기
plt.show()

