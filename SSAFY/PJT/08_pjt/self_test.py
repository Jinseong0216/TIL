array_length = 1000
random_range = 5000

# ==================================================
import pandas as pd
import numpy as np
# 전역변수로 DataFrame 미리 설정하기
df = pd.read_csv('./data/test_data.CSV', encoding='cp949')
df_has_null = pd.read_csv('./data/test_data_has_null.CSV', encoding='cp949')
df.columns = df_has_null.columns = ['name', 'age', 'sex', 'job', 'residential_area']

mean_age = round(float(df_has_null[['age']].mean(numeric_only=True)), 2)
df_has_null['age_diff'] = (df_has_null['age'] - mean_age).abs()
# 정렬 후 추출
top_10_diff = df_has_null.sort_values(by='age_diff').head(10)
data = top_10_diff[
    ['name', 'age', 'sex', 'job', 'residential_area']
    ].to_dict('records')
print(data)

# from django.http import JsonResponse
# result = JsonResponse({'data': data})