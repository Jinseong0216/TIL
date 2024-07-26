## 07/26(금) - 관통 PJT-02

#### Ver.1 금융
- 어려웠던 부분
    - 주어진 데이터의 전처리 과정에서 단순하게 구현 할 수 있었던 부분을 복잡하게 구현 한 것 같음.

        ```
        x_axis = [f'{2021}-{month}' for month in str_months_2021] + [f'{2022}-{month}' for month in str_months_2022]
        y_axis = []
        for month in months_2021:
            df_filtered_year = df[df['Date'].dt.year == 2021]
            month_price = df_filtered_year.loc[df_filtered_year['Date'].dt.month == month, ['Close']]
            month_price = np.mean(month_price['Close'])
            y_axis.append(month_price)

        for month in months_2022:
            df_filtered_year = df[df['Date'].dt.year == 2022]
            month_price = df_filtered_year.loc[df_filtered_year['Date'].dt.month == month, ['Close']]
            month_price = np.mean(month_price['Close'])
            y_axis.append(month_price)


        df_monthly = pd.DataFrame(y_axis, x_axis)
        df_monthly.columns = ['Monthly Average Close Price']
        ```
    
- 아쉬운 점들
    -  관통 PJT 영화에 집중한 결과로, 다양한 회사의 주가를 다뤄보지 못함.

    - 기회가 된다면, 다음에는 csv가 아닌 다른 타입의 데이터를 다뤄보고자 다짐.
        - 특히, NetCDF데이터를 다뤄보고자 함.
        
    - 잠시 ChatGPT4 결제를 중단하였던 여파로 이번 관통 PJT를 진행하며 필요했던 유료 기능을 사용하지 못하여 아쉬움을 느낌.

#### Ver.2 영화
- 학습 및 새로 알게된 내용
    - 현실의 데이터에 생각보다 정말 많은 에러가 존재함을 알게 되었다.

        특히, 이번 알라딘 Open API를 다루면서 받아온 책 저자 이름의 형식이 너무 다양하여 번거로운 절차를 거쳐야만 했음. 

        그럼에도 불구하고, 많은 경우에 저자를 나누는 기준이 (지은이)임을 발견하여 적절히 해결 할 수 있었음.

        `position = response['item'][0]['author'].index(' (지은이)')`

- 어려웠던 부분
    - json 파일을 다루는 것 보다, 주어진 Open API 매뉴얼을 뒤져보는 것에서 다소 어려움을 느끼게 됨.

