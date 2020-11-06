from coronavirus_tracking import region
import email_text_alerts.alert
import pandas as pd
import datetime
import time

def main():
    # continents dataframe #
    continents = initialize_continents()
    #print_continents(continents)

    # top 10 countries dataframe #
    countries = initialize_top10_countries()
    #print_countries(countries)

    daily_report()

### functions ###

# returns the key of a specified region
def get_region_key(name):
    key = 8
    if (name == 'north america'):
        key = 1
    elif (name == 'asia'):
        key = 2
    elif (name == 'south america'):
        key = 3
    elif (name == 'europe'):
        key = 4
    elif (name == 'africa'):
        key = 5
    elif (name == 'oceania'):
        key = 6
    elif (name == 'global'):
        key = 8
    if (name == 'usa'):
        key = 9
    elif (name == 'india'):
        key = 10
    elif (name == 'brazil'):
        key = 11
    elif (name == 'russia'):
        key = 12
    elif (name == 'spain'):
        key = 13
    elif (name == 'colombia'):
        key = 14
    elif (name == 'argentina'):
        key = 15
    elif (name == 'peru'):
        key = 16
    elif (name == 'mexico'):
        key = 17
    elif (name == 'france'):
        key = 18
    return key

# initializes the continents and their keys
def initialize_continents():
    # region objects connected to their keys
    north_america = region.region(get_region_key('north america'))
    south_america = region.region(get_region_key('south america'))
    europe = region.region(get_region_key('europe'))
    asia = region.region(get_region_key('asia'))
    africa = region.region(get_region_key('africa'))
    oceania = region.region(get_region_key('oceania'))
    globe = region.region(get_region_key('global'))

    # returns list of region objects
    continents = [
        north_america,
        south_america,
        europe,
        asia,
        oceania,
        globe]

    return continents

# initialize the 10 countries with the most cases and their keys
def initialize_top10_countries():
    # region objects connected to their keys
    usa = region.region(get_region_key('usa'))
    india = region.region(get_region_key('india'))
    brazil = region.region(get_region_key('brazil'))
    russia = region.region(get_region_key('russia'))
    spain = region.region(get_region_key('spain'))
    colombia = region.region(get_region_key('colombia'))
    argentina = region.region(get_region_key('argentina'))
    peru = region.region(get_region_key('peru'))
    mexico = region.region(get_region_key('mexico'))
    france = region.region(get_region_key('france'))

    # returns list of region objects
    countries = [
        usa,
        india,
        brazil,
        russia,
        spain,
        colombia,
        argentina,
        peru,
        mexico,
        france]

    return countries

# creates series of continent data, combines them into dataframe, and prints it
def print_continents(continents):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    ### pandas series ###
    # region names
    s = [continents[i].get_region_name() for i in range(len(continents))]
    names = pd.Series(s)

    # total cases
    s = [continents[i].get_total_cases() for i in range(len(continents))]
    total_cases = pd.Series(s).astype('int32')

    # new cases
    s = [continents[i].get_new_cases() for i in range(len(continents))]
    new_cases = pd.Series(s).astype('int32')

    # total deaths
    s = [continents[i].get_total_deaths() for i in range(len(continents))]
    total_deaths = pd.Series(s).astype('int32')

    # new deaths
    s = [continents[i].get_new_deaths() for i in range(len(continents))]
    new_deaths = pd.Series(s).astype('int32')

    # mortality rate
    s = [str(continents[i].get_mortality_rate()) + '%' for i in range(len(continents))]
    mortality_rate = pd.Series(s).astype('str')

    # constructing the dataframe
    data = {
        'continent:': names,
        'total CASES' : total_cases,
        'new CASES': new_cases,
        'total DEATHS' : total_deaths,
        'new DEATHS': new_deaths,
        'mortality rate': mortality_rate,
    }
    df_continents = pd.DataFrame(data, columns=['continent:', 'total CASES', 'new CASES', 'total DEATHS',   'new DEATHS', 'mortality rate'])
    print(df_continents)
    print('\nFROM: ' + str(datetime.date.today()))

# creates series of continent data, combines them into dataframe, and prints it
def print_countries(countries):
    ### pandas series ###
    # region names
    s = [countries[i].get_region_name() for i in range(len(countries))]
    names = pd.Series(s)

    # total cases
    s = [countries[i].get_total_cases() for i in range(len(countries))]
    total_cases = pd.Series(s).astype('int32')

    # new cases
    s = [countries[i].get_new_cases() for i in range(len(countries))]
    new_cases = pd.Series(s)

    # total deaths
    s = [countries[i].get_total_deaths() for i in range(len(countries))]
    total_deaths = pd.Series(s).astype('int32')

    # new deaths
    s = [countries[i].get_new_deaths() for i in range(len(countries))]
    new_deaths = pd.Series(s)

    # mortality rate
    s = [str(countries[i].get_mortality_rate()) + '%' for i in range(len(countries))]
    mortality_rate = pd.Series(s).astype('str')

    # constructing the dataframe
    data = {
        'country:': names,
        'total CASES' : total_cases,
        'new CASES': new_cases,
        'total DEATHS' : total_deaths,
        'new DEATHS': new_deaths,
        'mortality rate': mortality_rate,
    }
    df_countries = pd.DataFrame(data, columns=['country:', 'total CASES', 'new CASES', 'total DEATHS',   'new DEATHS', 'mortality rate'])
    print(df_countries)
    print('\nFROM: ' + str(datetime.date.today()))

# run this to send the daily new cases and new deaths to an email address or phone number
def daily_report():
    # emailing or texting the daily report! #
    phone_number = '{phone}'
    email = '{email}'
    country_names = [initialize_top10_countries()[i].get_region_name() for i in range(10)]
    new_cases = [initialize_top10_countries()[i].get_new_cases() for i in range(10)]
    new_deaths = [initialize_top10_countries()[i].get_new_deaths() for i in range(10)]

    cases_message = str(datetime.date.today())
    for i in range(10):
        cases_message += '\n' + country_names[i] + ': ' + new_cases[i]
    email_text_alerts.alert.email_alert(phone_number, 'New coronavirus cases today', cases_message)

    deaths_message = str(datetime.date.today())
    for i in range(10):
        deaths_message += '\n' + country_names[i] + ': ' + new_deaths[i]
    email_text_alerts.alert.email_alert(phone_number, 'New coronavirus deaths today', deaths_message)


if __name__ == '__main__':
    main()
