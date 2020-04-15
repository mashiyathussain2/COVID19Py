import COVID19Py
covid19 = COVID19Py.COVID19()

location = covid19.getLocationByCountryCode("IN")

print(location)


#output:-

[{'id': 131, 'country': 'India', 'country_code': 'IN', 'country_population': 1173108018, 'province': '', 'last_updated': '2020-04-15T10:58:36.007765Z', 'coordinates': {'latitude': '21', 'longitude': '78'}, 'latest': {'confirmed': 11487, 'deaths': 393, 'recovered': 0}}]
