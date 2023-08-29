import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

LIST_OF_CITIES  = ['chicago', 'new york city', 'washington']
LIST_OF_MONTHS  = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
#LIST_OF_MONTHS  = ['all', '1', '2', '3', '4', '5', '6']
LIST_OF_DAYS    = ['monday', 'tuesday', 'wensday', 'thursday', 'friday', 'saturday', 'sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please, select the name of the city to analyze (Chicago, New York City or Washington) : ').lower()
    while (city not in LIST_OF_CITIES):
        city = input('The name of the city is not correct, please, select the name of the city to analyze (Chicago, New York City or Washington) : ').lower()
                
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please, select the month to analyze until June ("all" in other cases) : ').lower()
    while (month not in LIST_OF_MONTHS):
        month = input('The name of the month is not correct, please, select the correct month (January to June) or "all" : ').lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please, select the day to analyze ("all" if you don´t have a specific day) : ').lower()
    while (day not in LIST_OF_DAYS):
        day = input('The name of the day is not correct, please, select the correct day or "all" : ').lower()
                
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #print('Nuria ciudad: ' + city + ' mes: ' + month + ' día:  ' + day) 
    
    # read the data acording to de city slected
    df = pd.read_csv(CITY_DATA[city])
    #print('Nuria: load_data ' + CITY_DATA[city])
    
    # All information about data has to be extracted from 'Start Time' column using Panda Date Functions 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # New columns:
    # month
    df['month'] = df['Start Time'].dt.month 
    #print(df['month'])
    
    # day 
    df['day']   = df['Start Time'].dt.weekday_name
    #print(df['day'])
    
    # start hour
    df['start hour']   = df['Start Time'].dt.hour
    
    # appliying the month filter if a month es selected
    if month !=  'all':
        month = LIST_OF_MONTHS.index(month) + 1
        #print ('NM Mes según indice calculado: ' + month)
        df = df[df['month'] == int(month)]
        
    # appliying the day filter if a day es selected
    if day !=  'all':
        df  = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {common_month}'.format(common_month = df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is: {common_day}'.format(common_day=df['day'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is: {common_hour}'.format(common_hour=df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {commonly_start_station}'.format(commonly_start_station = df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: {commonly_end_station}'.format(commonly_end_station = df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is: {commonly_start_end_station}'.format(commonly_start_end_station = (df['Start Station']+ ' - ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {total_travel_time}'.format(total_travel_time = df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is {mean_travel_time}'.format(mean_travel_time = df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of users type:\n{user_types}\n'.format(user_types = df.groupby(['User Type'])['User Type'].count()))
                                                                         
    # TO DO: Display counts of gender
    print('Counts of users gender:')
    try:
          print('{gender}\n'.format(gender = df.groupby(['Gender'])['Gender'].count()))
    except:
          print('It´s no possible to found information about users gender')
          
    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest
    print('The earliest year or bith is:')
    try:
          print('{earliest_year}\n'.format(earliest_year = int(df['Birth Year']).min()))
    except:
          print('It´s no possible to found information about the earliest year of birth\n')
            
    #most recent  
    print('The most recent year or bith is:')
    try:
          print('{most_recent_year}\n'.format(most_recent_year = int(df['Birth Year']).max()))
    except:
          print('It´s no possible to found information about the most recent year of birth\n')

    #most common
    print('The most common year or bith is:')
    try:
          print('{most_common_year}\n'.format(most_common_year = int(df['Birth Year']).mean()))
    except:
          print('It´s no possible to found information about the most common year of birth\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
    
def display_raw_data(df):
    """ Your docstring here """
    df1 = pd.DataFrame(df)
    
    i = 0
    
    # TO DO: convert the user input to lower case using lower() function
    answer = input('\nWould you like to show all data? Enter yes or no.\n').lower()
    
    #pd.set_option('display.max_columns',200)
    max_rows = pd.options.display.max_rows
    print("Initial max_rows value : " + str(pd.options.display.max_rows))

    while True:            
        if answer == 'no':
            break
        elif answer == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            pd.set_option("display.max_rows", i)
            print(df1)       
            
            # TO DO: convert the user input to lower case using lower() function
            answer = input('\nWould you like to show the next 5 rows from data? Enter yes or no.\n').lower()
           
            i += 5
        else:
            answer = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()