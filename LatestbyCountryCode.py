import COVID19Py
covid19 = COVID19Py.COVID19()

code = input("Enter country code: ")

location = covid19.getLocationByCountryCode(code)

for i in location:
    print(i['latest']) 
    
 
#Output
Enter country code: IN
{'confirmed': 11487, 'deaths': 393}
