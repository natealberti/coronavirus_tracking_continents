import bs4
from bs4 import BeautifulSoup
import requests

### setup ###
endpoint = 'https://www.worldometers.info/coronavirus/'
request = requests.get(endpoint)
soup = bs4.BeautifulSoup(request.content, 'html.parser')
all_global_data = soup.find_all('tr')

class region:

    # key is the index of this region in all_global_data
    def __init__(self, key):
        self.key = key
        self._region_data = all_global_data[self.key].find_all('td')

    ### data formatted for easy use ###
    def get_region_name(self):
        _region_name = self._region_data[1].text
        return _region_name.replace('\n', '')

    def get_total_cases(self):
        _total_cases = self._region_data[2].text
        return float(_total_cases.replace(',', ''))

    def get_new_cases(self):
        _new_cases = self._region_data[3].text
        return float(_new_cases.replace(',', ''))

    def get_total_deaths(self):
        _total_deaths = self._region_data[4].text
        return float(_total_deaths.replace(',', ''))

    def get_new_deaths(self):
        _new_deaths = self._region_data[5].text
        return float(_new_deaths.replace(',', ''))

    def get_total_recovered(self):
        _total_recovered = self._region_data[6].text
        return float(_total_recovered.replace(',', ''))

    def get_recovered_today(self):
        _recovered_today = self._region_data[7].text
        return float(_recovered_today.replace(',', ''))

    def get_active_cases(self):
        _active_cases = self._region_data[8].text
        return float(_active_cases.replace(',', ''))

    def get_critical_cases(self):
        _critical_cases = self._region_data[9].text
        return float(_critical_cases.replace(',', ''))

    # N/A on continent data
    #def get_cases_per_1Mpop(self):
        _cases_per_1Mpop = self._region_data[10].text
        return float(_cases_per_1Mpop.replace(',', ''))

    # N/A on continent data
    # def get_deaths_per_1Mpop(self):
        _deaths_per_1Mpop = self._region_data[11].text
        return float(_deaths_per_1Mpop.replace(',', ''))

    # my functions!
    def get_mortality_rate(self):
        f = self.get_total_deaths() / self.get_total_cases()
        return round(f * 100, 2)

    def get_percent_critical(self):
        f = self.get_critical_cases() / self.get_active_cases()
        return round(f * 100, 3)

