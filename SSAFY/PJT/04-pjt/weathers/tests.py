from django.test import TestCase
import pandas as pd
# Create your tests here.
dataframe = pd.read_csv('C:/Users/SSAFY/Desktop/pjt_ver1/weathers/templates/weathers/data/austin_weather.csv')
print(dataframe)