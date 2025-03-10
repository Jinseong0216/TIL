import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

key_change = { 'feels_like' : '체감온도', 'humidity' : '습도', 'pressure' : '기압',
              'temp' : '온도', 'temp_max' : '최고온도','temp_min' : '최저온도',
              'description' : '요약','icon' : '아이콘', 'main' : '핵심','id' : '식별자'}

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    parsed_data = requests.get(url).json()
    
    key_change = { 'feels_like' : '체감온도', 'humidity' : '습도', 'pressure' : '기압','temp' : '온도', 
                  'temp_max' : '최고온도','temp_min' : '최저온도','description' : '요약','icon' : '아이콘', 
                  'main' : '핵심','id' : '식별자'}
    result = {}
    main_dict = {}
    weather_dict = {}

    for key in key_change:
        if key in parsed_data['main']:
            main_dict[key_change[key]] = parsed_data['main'][key]
        if key in parsed_data['weather'][0]:
            weather_dict[key_change[key]] = parsed_data['weather'][0][key]

    result['기본'] = main_dict
    result['날씨'] = [weather_dict]

    return result



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '2d8501186892b0c24d8f51e105e591db'

    result = get_weather(api_key)
    pprint(result)
