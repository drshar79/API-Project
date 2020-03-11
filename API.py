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


#COVID-19 Recovered

URL3= "https://covid19.mathdro.id/api/recovered"

res3=requests.get(URL3)
res3=res3.json()

#COVID-19 Daily

URL4="https://covid19.mathdro.id/api/daily"

res4=requests.get(URL3)
res4=res4.json()

print ("COVID-19 is rapidly spreading across the world, and a lot of data has been recorded. Would you like to see data about COVID-19 DEATHS, CONFIRMED infections, RECOVERED patients, or DAILY infections?")
ans = input()
if ans== ("DEATHS"):
    print("Type in a country: ")
    ans=input()
#deathnum= ans == c["deaths"]
#confirmnum= ans == c[]
    for c in res:
        if ans== c["countryRegion"]:
            print(print("Confirmed: ")) + str(c["confirmed"]) + " " +(print("Deaths: ")) + str( c["deaths"])
    # if ans== res["countryregion"] in range (res):
    #     print(input)