import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington), month (january...june) or day of week. HINT: Use a while loop to handle invalid inputs
    city = input("Enter chosen city: chicago, new york city or washington: ").lower()
    while True:               
        if city == 'chicago' or city == 'new york city' or city == 'washington' :
                print('Selected city is', city)
                break
        else:
                print('Entered city is not valid')
                city = input("Enter chosen city: chicago, new york city or washington: ").lower()
                
    month = input("Please choose the month from the range (all, january, february, ... , june): ").lower()
    while True:
            if month in ['all','january', 'february', 'march', 'april', 'may', 'june'] :                           
                break
            else:
                print('Selected month doesn\'t exist in the city file')
                month = input("Please choose the month from the range (all, january, february, ... , june): ").lower()
    
    day = input("Please choose the valid weekday or all: ").lower()
    while True:
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
            print("Selected day, {}!".format(day.title()))
            break
        else:
            print('Entered day is not a valid input')
            day = input("Please choose the valid weekday or all: ").lower()
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])  
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print('The Most popular', popular_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print('The Most common day of week:', popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode() 
    print('Most Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds."%(time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('Most Frequent Start Station: ', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('Most Frequent End Station: ', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = (df['Start Station'] + df['End Station']).mode()
    print('Most frequent combination of start station and end station trip: ', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #df['Trip Duration'] = pd.to_datetime(df['Trip Duration'], unit='m')
    travel_time = df['Trip Duration'].sum() 
    print('Total trip duration, hours: ', travel_time // 3600)
    # TO DO: display mean travel time
    average_trip = float(df.loc[:,'Trip Duration'].mean())
    print('Average trip duration, minutes:', average_trip // 60)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if df['User Type'].empty:
        print('The column user_types does not exist in the city file')
    else:
        user_types = df['User Type'].value_counts()
        print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)        
    else: 
        print('The column Gender does not exist in the city file')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_year_min = df['Birth Year'].min()
        print('The earliest year of birth ', birth_year_min)
        birth_year_max = df['Birth Year'].max()
        print('The most recent year of birth ', birth_year_max)
        birth_year_common = df['Birth Year'].mode()
        print('The most common year of birth ', birth_year_common)
    else: 
        print('The column Birth Year does not exist in the city file')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rows_iter(df):
    df = df.reset_index()
    n=0
    while n in range(len(df)):
        user_input = input('Would you like to see raw data?: ')
        if user_input == 'yes':
            print(df.iloc[n:n+5,:])        
            n=n+5
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rows_iter(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
