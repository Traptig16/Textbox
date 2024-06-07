import requests
from bs4 import BeautifulSoup
import pandas as pd

actorName ="Leonardo DiCaprio" #input("Enter Name of Actor: ")
actorNameWithPlus = "+".join(actorName.split(" "))
url = "https://api.themoviedb.org/3/search/person?api_key=e53f4d41141f3da4a1304027ce8ddf18&query="+actorNameWithPlus
response = requests.get(url).json()
actorID = response["results"][0]['id']
print(actorID)

urlTogetMovies = "https://www.themoviedb.org/person/"+str(actorID)
res = requests.get(urlTogetMovies)

soup = BeautifulSoup(res.text,'lxml')
contentTable = soup.find('table',class_="card credits")
# print(contentTable)

movies_list = []
year_list = []
movies = contentTable.find_all("a",class_="tooltip")

for movie in movies:
    movies_list.append(movie.text)

years = contentTable.find_all('td',class_="year")
for year in years:
    if year.text == "—":
        year_list.append("Upcoming")
    else:
        year_list.append(year.text)


movies_df = pd.DataFrame({'Year':year_list,'Movie':movies_list})
movies_df.to_csv('Movies.csv',index=False)
print(movies_df)