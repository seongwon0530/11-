# -*- coding: utf-8 -*-
"""과제.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EbxGklbLJXdeempiXUsBpYiYForl45ih
"""

import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

!pip install requests
!pip install bs4
!pip install pandas
!pip install matplotlib

source = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
soup = BeautifulSoup(source.content,"html.parser")

table = soup.find('table',{'class':'table-col'})
data = []

print("#"*30)
print("\nHello! Here's today's weather!\n")
print("#"*30)

for tr in table.find_all('tr'):
  tds = list(tr.find_all('td'))
  for td in tds:
    if td.find('a'):
      point = td.find('a').text
      temp = tds[5].text
      humidity = tds[9].text
      print("{0:<7} {1:<7} {2:<7}".format(point, temp, humidity))
      data.append([point, temp, humidity])