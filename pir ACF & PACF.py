import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 데이터 불러오기
data = pd.read_excel("data.xlsx")

# 주제 금리(IR)를 독립변수로, KOSPI를 종속변수로 선택
ir_series = data['IR']
pir_series = data['PIR']

# ACF 및 PACF 그래프를 통한 ARIMA 차수 선택
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plot_acf(pir_series, lags=min(20, len(pir_series)-1), ax=plt.gca())
plt.title('Autocorrelation Function (ACF)')

plt.subplot(1, 2, 2)
plot_pacf(pir_series, lags=min(10, len(pir_series)//2), ax=plt.gca())
plt.title('Partial Autocorrelation Function (PACF)')

plt.show()
