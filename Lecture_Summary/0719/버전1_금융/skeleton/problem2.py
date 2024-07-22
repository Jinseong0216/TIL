import requests
from pprint import pprint

## grnd_level, sea_leavel

# 문제1. 날씨 데이터의 응답을 json 형태로 변환하여 key 값만 출력하시오.

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    parsed_data = requests.get(url).json()
    result = {'main': parsed_data['main'], 
              'weather_data': parsed_data['weather']}
    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '2d8501186892b0c24d8f51e105e591db'

    result = get_weather(api_key)
    pprint(result)
