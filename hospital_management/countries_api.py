import requests

countries = []
countries_code = dict()
flags = dict()

response = requests.get("https://restcountries.com/v3.1/all")
json_data = response.json()

for i in range(len(json_data)):
    country_name = json_data[i].get("name").get("common")
    # suffixes = json_data[i].get("idd").get('suffixes')
    # country_root = json_data[i].get("idd").get("root")
    # country_code = []
    # if suffixes is not None:
    #     for j in range(len(suffixes)):
    #         country_c = country_root + suffixes[j]
    #         country_code.append(country_c)

    # flag = json_data[i].get("flags").get("png")
    # flags[country_name] = flag
    # countries_code[country_name] = country_code
    countries.append(country_name)

print(countries)
#print(flags)
#print(len(countries_code))