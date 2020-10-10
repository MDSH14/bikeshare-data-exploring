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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Please choose the city from Chicago, New york city or Washington:')
    while True:
        city = str(input())
        city = city.lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print("please enter a valid city:")


    print("Do you want to filter the data by month, day or both? type \"none\" for no time filter")
    while True:
        filters = str(input())
        filters = filters.lower()
        if filters == 'month' or filters == 'day' or filters == 'both' or filters == 'none':
            break
        else:
            print("please enter a valid filter:")

    month = 'all'
    day = 'all'
    if filters == 'none':
        return city, month, day

    if filters == 'month' or filters == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
        print('Please choose the month or choose all:')
        while 1:
            month = str(input())
            month = month.lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april'\
                    or month == 'may' or month == 'june' or month == 'all':
                break
            else:
                print("please enter a valid value:")

    if filters == 'day' or filters == 'both':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print('Please choose the day or choose all:')
        while 1:
            day = str(input())
            day = day.lower()
            if day == 'saturday' or day == 'sunday' or day == 'monday' or day == 'tuesday'\
                    or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'all':
                break
            else:
                print("please enter a valid value:")


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['Start to End'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    month = df['month'].mode()[0]
    print('The most common month is: ', months[month].title())

    # TO DO: display the most common day of week
    print('The most common day of the week is:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour is:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is:\n', df['Start to End'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time is:", "%.2f" % ((df['Trip Duration'].sum())/60.00), "Minutes")


    # TO DO: display mean travel time
    print("the average travel time is:", "%.2f" % ((df['Trip Duration'].mean())/60.00), "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, dc):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types are:\n", df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    if dc:
        print("The counts of gender are:\n", df['Gender'].value_counts(), "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if dc:
        print("The earliest birth year is", int(df['Birth Year'].min()))
        print("The most recent birth year is", int(df['Birth Year'].max()))
        print("The most common birth year is", int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if city != 'washington':
            dc = True
        else:
            dc = False
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, dc)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
