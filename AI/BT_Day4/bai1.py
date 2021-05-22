import requests
import json
class DownloadCovidInfo:
    def __init__(self, url):
        self.data=requests.get(url).json()
    def get_all_data(self):
         print(self.data)
    def get_data_by_country(self):
        countries =self.data['Countries']
        for country in countries:
            print(f"{country['Country']} : {country['TotalDeaths'] } new deaths")
    def save_to_file(self, file):
       with open(f"{file}.json","w") as f:
          json.dump(self.data,f,indent=4)

x=DownloadCovidInfo("https://api.covid19api.com/summary")
x.get_all_data()
x.get_data_by_country()
x.save_to_file("Covid")