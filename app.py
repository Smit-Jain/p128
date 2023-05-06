import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')
temp_list = []
star_names = []
distance = []
mass = []
radius = []
table_rows = star_table[7].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['star_name','distance','mass','radius'])
df2.to_csv("dwarfstar.csv")