from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find_all('table')
temp=[]
table_row=star_table[7].find_all("tr")
for tr in table_row:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td] 
    temp.append(row)
star_names=[]
star_distance=[]
radius=[]
mass=[]
for i in range(1,len(temp)):
    star_names.append(temp[i][0])
    star_distance.append(temp[i][5])
    mass.append(temp[i][7])
    radius.append(temp[i][8])
df2=pd.DataFrame(list(zip(star_names,star_distance,mass,radius)),columns=['star_name','star_distance','mass','radius'])    
df2.to_csv('dwarf_stars.csv')