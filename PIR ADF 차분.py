import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# 데이터 불러오기
data = pd.read_excel("data.xlsx")

# 주제 금리(IR)와 PIR 시계열 데이터 선택
ir_series = data['IR']
pir_series = data['PIR']

# ADF 검정을 통한 정상성 확인
def check_stationarity(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])

# PIR 데이터에 대한 ADF 검정 수행
print("PIR ADF Test:")
check_stationarity(pir_series)

# 차분 횟수 계산
diff_count = 0
while adfuller(pir_series.diff(diff_count + 1).dropna())[1] > 0.05:
    diff_count += 1

print("Optimal differencing order:", diff_count)

# 차분된 KOSPI 데이터 시각화
plt.plot(pir_series.diff(diff_count))
plt.title(f'Differenced PIR (Order {diff_count})')
plt.show()
