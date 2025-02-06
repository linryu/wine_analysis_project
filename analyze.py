import pandas
from sklearn.datasets import load_wine

# Wine 데이터셋 로드
wine_data = load_wine()
df = pandas.DataFrame(data=wine_data.data, columns=wine_data.feature_names)

# 데이터셋의 행과 열 개수 출력
rows, columns = df.shape
print(f"행(row) 개수: {rows}, 열(column) 개수: {columns}")

# 각 특성의 평균과 표준편차 계산
mean_values = df.mean()
std_values = df.std()

# 특정 특성(alcohol)의 최대값과 최소값 출력
max_alcohol = df['alcohol'].max()
min_alcohol = df['alcohol'].min()

# 결과를 output.txt 파일에 저장
with open('output.txt', 'w') as f:
    f.write(f"행(row) 개수: {rows}, 열(column) 개수: {columns}\n")
    f.write("각 특성의 평균:\n")
    f.write(mean_values.to_string() + "\n")
    f.write("각 특성의 표준편차:\n")
    f.write(std_values.to_string() + "\n")
    f.write(f"alcohol의 최대값: {max_alcohol}\n")
    f.write(f"alcohol의 최소값: {min_alcohol}\n")
