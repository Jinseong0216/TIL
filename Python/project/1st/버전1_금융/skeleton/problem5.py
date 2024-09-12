import requests
from datetime import datetime, timedelta

# API 요청
url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {'q': 'Busan', 'appid': '2d8501186892b0c24d8f51e105e591db', 'units': 'metric'}
response = requests.get(url, params=params)
data = response.json()

# 현재 날짜로부터 5일 후 계산
current_date = datetime.now()
target_date = (current_date + timedelta(days=5)).date()

# 5일 후의 날씨 데이터 필터링
weather_data = []
for forecast in data['list']:
    forecast_date = datetime.fromtimestamp(forecast['dt']).date()
if forecast_date == target_date:
    weather_data.append(forecast)

# 결과 출력
print('='*100)
for weather in weather_data:
    print('받아온 데이터는 다음과 같습니다.')
    print(weather)
print('='*100)




# 날짜와 시간 정보 추출
date_time = weather['dt_txt']
# 주요 날씨 정보 추출
temperature = weather['main']['temp']
feels_like = weather['main']['feels_like']
humidity = weather['main']['humidity']
description = weather['weather'][0]['description']
# 바람 정보 추출 및 방향 변환
wind_speed = weather['wind']['speed']
wind_deg = weather['wind']['deg']
# 바람의 방향을 텍스트로 변환하는 함수
def get_wind_direction(deg):
    if deg >= 337.5 or deg < 22.5: return '북'
    elif 22.5 <= deg < 67.5: return '북동'
    elif 67.5 <= deg < 112.5: return '동'
    elif 112.5 <= deg < 157.5: return '남동'
    elif 157.5 <= deg < 202.5: return '남'
    elif 202.5 <= deg < 247.5: return '남서'
    elif 247.5 <= deg < 292.5: return '서'
    elif 292.5 <= deg < 337.5: return '북서'

wind_direction = get_wind_direction(wind_deg)

result = (f"이 데이터를 바탕으로 해당 시간대의 날씨를 종합해 보면, "
          f"{date_time}에는 {description}이고, "
          f"기온은 약 {temperature}도, 체감 온도는 {feels_like}도, "
          f"습도는 {humidity}%, 바람은 {wind_direction}쪽에서 시속 {wind_speed}미터로 불고 있습니다.")

print(result)
