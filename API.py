import requests

#COVID-19 Deaths

URL = "https://covid19.mathdro.id/api/deaths"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

#COVID-19 Confirmed
URL2= "https://covid19.mathdro.id/api/confirmed"

res2=requests.get(URL2)
res2=res2.json()

#COVID-19 Recovered

URL3= "https://covid19.mathdro.id/api/recovered"

res3=requests.get(URL3)
res3=res3.json()

#COVID-19 Daily

URL4="https://covid19.mathdro.id/api/daily"

res4=requests.get(URL3)
res4=res4.json()


print (" Would you like to see data about COVID-19 DEATHS, CONFIRMED infections, RECOVERED patients, or DAILY recordings?")
ans = input()
#If input "DEATHS" was typed:
if ans== ("DEATHS"):
    print("Type in a country: ")
    ans=input()
    for d in res:
        if ans== d["countryRegion"]:
            print(" ")
            print("Confirmed: " + str(d["confirmed"]) + " " + "Deaths: " + str( d["deaths"]))
    else:
        print("*NOTE* If nothing came up, that means that we were unable to find the country typed in. Please restart program to try again.") 

#If input "CONFIRMED" was typed:
if ans==("CONFIRMED"):
    print("Type in a country: ")
    ans=input()
    for c in res2:
        if ans == c["countryRegion"]:
            print(" ")
            print("Confirmed: " + str(c['confirmed']) + " " + "Deaths: " + str( c['deaths']))
    else:
        print("*NOTE* If nothing came up, that means that we were unable to find the country typed in. Please restart program to try again.") 
#If input "RECOVERED" was typed:
if ans==("RECOVERED"):
    print("Type in a country: ")
    ans=input()
    for r in res3:
        if ans== r["countryRegion"]:
            print(" ")
            print("Recovered: " + str(r['recovered']))  
    else:
        print("*NOTE* If nothing came up, that means that we were unable to find the country typed in. Please restart program to try again.")  
# if input "DAILY" was typed:
if ans == ("DAILY"):
    print("Type in a country: ")
    ans=input()
    for q in res4:
        if ans== q["countryRegion"]:
            print(" ")
            print("Confirmed: " + str(q["confirmed"]) + " " + "Deaths: " + str( q["deaths"]))
    else:
        print("*NOTE* If nothing came up, that means that we were unable to find the country typed in. Please restart program to try again.")        
             