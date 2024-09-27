import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from .models import Weather
from io import BytesIO
import base64

def base(request):
    return render(request, 'weathers/base.html')

def problem1(request):
    try:
        # CSV 파일 읽기
        df = pd.read_csv('C:/Users/SSAFY/Desktop/pjt_ver1/weathers/templates/weathers/data/austin_weather.csv')

        # 데이터 처리 및 저장
        for index, row in df.iterrows():
            if Weather.objects.filter(Date=row['Date']).exists():
                continue
            
            # '-'를 None으로 변환
            row = row.replace('-', pd.NA)
            weather = Weather(
                Date=row['Date'],
                TempHighF=row['TempHighF'],
                TempAvgF=row['TempAvgF'],
                TempLowF=row['TempLowF'],
                DewPointHighF=pd.to_numeric(row['DewPointHighF'], errors='coerce') or 0,
                DewPointAvgF=pd.to_numeric(row['DewPointAvgF'], errors='coerce') or 0,
                DewPointLowF=pd.to_numeric(row['DewPointLowF'], errors='coerce') or 0,
                HumidityHighPercent=pd.to_numeric(row['HumidityHighPercent'], errors='coerce') or 0.0,
                HumidityAvgPercent=pd.to_numeric(row['HumidityAvgPercent'], errors='coerce') or 0.0,
                HumidityLowPercent=pd.to_numeric(row['HumidityLowPercent'], errors='coerce') or 0.0,
                SeaLevelPressureHighInches=pd.to_numeric(row['SeaLevelPressureHighInches'], errors='coerce'),
                SeaLevelPressureAvgInches=pd.to_numeric(row['SeaLevelPressureAvgInches'], errors='coerce'),
                SeaLevelPressureLowInches=pd.to_numeric(row['SeaLevelPressureLowInches'], errors='coerce'),
                VisibilityHighMiles=pd.to_numeric(row['VisibilityHighMiles'], errors='coerce') or 0,
                VisibilityAvgMiles=pd.to_numeric(row['VisibilityAvgMiles'], errors='coerce') or 0,
                VisibilityLowMiles=pd.to_numeric(row['VisibilityLowMiles'], errors='coerce') or 0,
                WindHighMPH=pd.to_numeric(row['WindHighMPH'], errors='coerce'),
                WindAvgMPH=pd.to_numeric(row['WindAvgMPH'], errors='coerce'),
                WindGustMPH=pd.to_numeric(row['WindGustMPH'], errors='coerce'),
                PrecipitationSumInches=row['PrecipitationSumInches'],
                Events=row['Events'] if pd.notna(row['Events']) else ""
            )
            weather.save()

    except Exception as e:
        # 예외 처리
        print(f"Error occurred: {e}")

    weathers = Weather.objects.all()
    context = {
        'weathers': weathers,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    # 데이터베이스에서 모든 날씨 데이터 가져오기
    weathers = Weather.objects.all()

    # 데이터프레임 생성
    data = {
        'Date': [weather.Date for weather in weathers],
        'TempHighF': [weather.TempHighF for weather in weathers],
        'TempAvgF': [weather.TempAvgF for weather in weathers],
        'TempLowF': [weather.TempLowF for weather in weathers],
    }
    df = pd.DataFrame(data)

    # Date 필드를 datetime 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    # 그래프 그리기
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['TempHighF'], label='High Temperature', color='red')
    plt.plot(df['Date'], df['TempAvgF'], label='Average Temperature', color='blue')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature', color='green')
    
    # 그래프 설정
    plt.xlabel('Date')
    plt.ylabel('Temperature (°F)')
    plt.title('Temperature Variation')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    context = {
        'graph_url': graph_url,
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    return render(request, 'weathers/problem3.html')

def problem4(request):
    return render(request, 'weathers/problem4.html')

def problem5(request):
    return render(request, 'weathers/problem5.html')
