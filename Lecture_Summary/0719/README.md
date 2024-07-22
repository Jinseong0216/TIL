## 관통 PJT

#### 부울경_1반 최진성(금융 프로젝트)

- **학습 및 새로 알게된 내용**

    1. 서버를 통해 데이터를 호출하여 json 형태로 변환하였을 때, 눈으로 자료를 확인하는데 많은 어려움이 있었음.

        그러나, pprint 모듈을 사용하여 출력한다면 자료의 구조를 직관적으로 파악 할 수 있음을 알게 됨.
    
    2. json 자료를 파이썬을 통해 다루는 것이 아주 용이함(dictionary를 활용)을 알게 됨.
    
    3. 필요한 라이브러리를 명확히 파악하는 것, 프롬프트 엔지니어링의 중요성을 알게 됨.

        - 특히, 필요한 라이브러리를 파악하는 과정에서 openai의 활용하였을 때 많은 시간을 줄일 수 있었다.

        - openai를 활용하며 지난 주 학습하였던 프롬프트 엔지니어링을 사용하었는데, 그 결과 필요한 라이브러리의 사용 방법을 금방 파악 할 수 있었다.

        ```
        from datetime import datetime, timedelta
        
        # 현재 날짜로부터 5일 후 계산
        current_date = datetime.now()
        target_date = (current_date + timedelta(days=5)).date()

        # 5일 후의 날씨 데이터 필터링
        weather_data = []
        for forecast in data['list']:
            forecast_date = datetime.fromtimestamp(forecast['dt']).date()
        if forecast_date == target_date:
            weather_data.append(forecast)
        ```


- **어려웠던 부분**

    1. pprint를 사용하여 많은 시간을 줄였지만, 그럼에도 불구하고 시간이 오래 걸렸음.
    
        - 관통 PJT 금융의 선택과제들을 진행 할 때, 호출한 데이터가 기존에 비해 더 복잡해 졌었고 여기에서 시간을 오래 사용하였음.
    2. 효율적으로 프로그래밍 하는 것에 어려움을 느낌.
    
        - 관통 PJT 금융의 선택과제4 또한, 단순히 데이터를 가공하는 것이었는데. 이를 해결하기 위해 for문을 과도하게 사용하게 되었음.


- **아쉬운 점들**

    관통 PJT 금융의 필수와 선택과제5는 생성형 AI를 활용하는 것이었는데,

    openai의 token이슈로 인해 원하는 기능을 구현하지 못함.