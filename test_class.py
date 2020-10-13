import region
import pandas as pd
import datetime
import time

def main():
    # initial list of region objects
    continents = initialize_regions()

    ### pandas series ###

    # region names
    s = [continents[i].get_region_name() for i in range (len(continents))]
    names = pd.Series(s)

    # total cases
    s = [continents[i].get_new_cases() for i in range(len(continents))]
    total_cases = pd.Series(s).astype('int32')

    # total deaths
    s = [continents[i].get_new_deaths() for i in range(len(continents))]
    total_deaths = pd.Series(s).astype('int32')

    # mortality rate
    s = [str(continents[i].get_mortality_rate()) + '%' for i in range(len(continents))]
    mortality_rate = pd.Series(s).astype('str')


    # constructing the dataframe
    data = {
        'continent' : names,
        'new cases' : total_cases,
        'new deaths' : total_deaths,
        'mortality rate': mortality_rate,
    }
    df = pd.DataFrame(data, columns=['continent', 'new cases', 'new deaths', 'mortality rate'])
    print(df)
    print('\nFROM: ' + str(datetime.date.today()))

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
    return key

# initializes the regions and their keys
def initialize_regions():
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

if __name__ == '__main__':
    main()