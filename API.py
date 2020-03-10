import requests

#COVID-19 Deaths

URL = "https://covid19.mathdro.id/api/deaths"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

#COVID-19 Confirmed
URL2= "https://covid19.mathdro.id/api/confirmed"

res2=requests.get(URL2)
res2=res2.json()

#print(res[6])
print(res2)

#COVID-19 Recovered

URL3= "https://covid19.mathdro.id/api/recovered"

res3=requests.get(URL3)
res3=res3.json()

#COVID-19 Daily

URL4="https://covid19.mathdro.id/api/daily"

res4=requests.get(URL3)
res4=res4.json()

