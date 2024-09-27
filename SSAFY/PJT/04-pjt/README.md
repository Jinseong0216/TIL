## 09/27 관통프로젝트 후기

### 회고
만약 외주를 받은 1인 프리랜서 개발자였다면... 
다른사람의 레퍼런스를 참조하는게 싫어 직접 전부 구현하려하다가
결국 작업을 끝내지 못해 평판이 떨어졌을 것같다.

특히, 장고를 통해 csv파일을 다루는 것을 이전에 해보지는 않았으나...
pandas, netCDF4등.. 다양한 데이터를 다룬 경험이 있어 자신감이 앞섰는데... 결과는 그렇지 않았음.

반성하고, 다음부터는 현실적으로 프로젝트를 진행하는 것을 목표로 해야겠다.

#### 어려웠던 부분
- 직접 csv파일을 뜯어보는 것
  - 결측치 처리에 어려움을 느낌
  - 이번에 제공받은 데이터의경우 21개의 필드가 존재하였는데, 중간에 변수 두개를 하나로 생각하여 디버깅에 정말 많은 시간이 걸림.
    - ex. `WindAvgMPHWindGustMPH`
- 장고의 db가 꼬인 경우, 내가 배운 방법인 db삭제와 migrations 기록 삭제를 했을 때 간혹 원본 데이터가 사리질 수 있음을 몰랐음.

#### 배운점
- 반복 노가다 작업은 그냥 생성형 ai에게 맞기고 검수하는 것이 시간적으로 옳다..
```py
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
```
- 오늘 프로젝트를 통해 직접 배운 것은 없음.. 능력부족. 그러나 내가 부족한 부분이 어딘지를 명확히 알게 됨.
  
##### 반성중...