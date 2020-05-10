"""
Udacity analysis project 
"""
import time
import math
import pandas as pd
import numpy as np
"""
LOAD DATASET
"""
C_D = { 'ch': 'chicago.csv',
              'n_y_c': 'new_york_city.csv',
              'w': 'washington.csv' }
M_D = { 'january': 1,
                'february': 2,
                'march': 3,
                'april': 4,
                'may': 5,
                'june': 6,
                'jan': 1,
                'feb': 2,
                'mar': 3,
                'apr': 4,
                'may': 5,
                'jun': 6}

W_D = { 'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6,
                'mon': 0,
                'tues': 1,
                'wed': 2,
                'thur': 3,
                'fri': 4,
                'sat': 5,
                'sun': 6}
"""
FILTER DATA
"""
def filters():
    """
    Asks to choose a city, month, and day to analyze.
    Returns:
        (string) city - analyze of city
        (string) month - name of the month to filter by, or "all" to apply no month filter
        (string) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        print('Which country\'s should we look for?')
        city = input('ch/CH,  New York City/NYC, or w/WA? ').lower()
        print()
        if city=='ch':
            city='ch'
        if city=='ny' or city=='nyc':
            city='n_y_c'
        if city=='wa' or city=='washington dc':
            city='w'
        if city not in C_D:
            print('Kindly enter a valid city')
            continue
        city = C_D[city]
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        choice = input('Do you want to filter the data by month and/or week? Yes/No ').lower()
        print()
        if choice=='yes' or choice=='y' or choice=='yus':
            choice=True
        elif choice=='no' or choice=='n' or choice=='nope':
            choice=False
        else:
            print('You did not enter a valid choice. Let\'s try again. ')
            continue
        break

    while 1:
        if choice:
            filter=input('You can filter by month / day / both ').lower()
            print()
            if filter=='month':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in M_D:
                    print('Sorry I did not understand that input. Could you try again?')
                    continue
                month = M_D[month]
                day='all'
            elif filter=='day':
                print('Which day\'s data to look at? ')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in W_D:
                    print('Sorry I did not understand that input. Could you try again?')
                    continue
                day = W_D[day]
                month='all'
            elif filter=='both':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in M_D:
                    print('Sorry I did not understand that input. Could you try again?')
                    continue
                month = M_D[month]
                print('And day of the week?')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in W_D:
                    print('Sorry I did not understand that input. Could you try again?')
                    continue
                day = W_D[day]
            else:
                print('Sorry I did not understand that input. Could you try again?')
                continue
            break
        else:
            day='all'
            month='all'
            break

    print('-'*40)
    return city, month, day

def l_d(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Returns:
        dataset - DataFrame containing city data filtered by month and day
    """
    dataset = pd.read_csv(city)
    dataset['day_of_week'] = pd.to_datetime(dataset['Start Time']).dt.dayofweek
    dataset['month'] = pd.to_datetime(dataset['Start Time']).dt.month
    if day != 'all':
        dataset = dataset[dataset['day_of_week'] == day]
    if month != 'all':
        dataset = dataset[dataset['month'] == month]
    dataset.drop('day_of_week',axis=1,inplace=True)
    dataset.drop('month',axis=1,inplace=True)
    return dataset
"""
TIME STATE
"""
def t_s(dataset):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    dataset['day_of_week'] = pd.to_datetime(dataset['Start Time']).dt.dayofweek
    dataset['month'] = pd.to_datetime(dataset['Start Time']).dt.month
    #temporary_dataset = pd.read_csv(city)
    # TO DO: display the most common month
    m_f_m = dataset['month'].mode()[0]
    for num in M_D:
        if M_D[num]==m_f_m:
            m_f_m = num.title()
    print('The most common month for travel is {}'.format(m_f_m))

    # TO DO: display the most common day of week
    m_f_d = dataset['day_of_week'].mode()[0]
    for num in W_D:
        if W_D[num]==m_f_d:
            m_f_d = num.title()
    print('The most common day of week for travel is {}'.format(m_f_d))

    # TO DO: display the most common start hour
    dataset['hour']=pd.to_datetime(dataset['Start Time']).dt.hour
    m_f_h = dataset['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(m_f_h))
    dataset.drop('hour',axis=1,inplace=True)
    dataset.drop('day_of_week',axis=1,inplace=True)
    dataset.drop('month',axis=1,inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
"""
STATE Station
"""
def s_s(dataset):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print('Most commonly used start station as per our data was {}'.format(dataset['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print()
    print('Most commonly used end station as per our data was {}'.format(dataset['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print()
    m_f_s_c = dataset['Start Station'] + ' to ' + dataset['End Station']
    print('The most frequnt combination of start station and end station trip was {}'.format(m_f_s_c.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
"""
trip_duration_stats
"""
    
def t_d_s(dataset):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    """
    travel duration
    """
    td= pd.to_datetime(dataset['End Time']) - pd.to_datetime(dataset['Start Time'])

   
    print()
    """
    calculate sum of seconds ,minutes,hours,days and print total travel time  """
    td_sum = dataset['Trip Duration'].sum()
    seconds = td_sum%60
    minutes = td_sum//60%60
    hours = td_sum//3600%60
    days = td_sum//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(days, hours, minutes, seconds))

    """ calculate mean travel time"""
    print()
    td_mean = math.ceil(dataset['Trip Duration'].mean())
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""
user state
"""
def U_S(dataset):

    print('\nCalculating User Stats...\n')
    start_t = time.time()

    # TO DO: Display counts of user types
    print()
    t_o_u = dataset.groupby('User Type',as_index=False).count()
    print('Number of types of users are {}'.format(len(t_o_u)))
    for i in range(len(t_o_u)):
        print('{}s - {}'.format(t_o_u['User Type'][i], t_o_u['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in dataset:
        print('Shoot, no gender data for this city :(')
    else:
        g_o_u = dataset.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(g_o_u)))
        for i in range(len(g_o_u)):
            print('{}s - {}'.format(g_o_u['Gender'][i], g_o_u['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(dataset)-g_o_u['Start Time'][0]-g_o_u['Start Time'][1]))

    """ TO DO: Display earliest, most recent, and most common year of birth """ 
    print()
    if 'Birth Year' not in dataset:
        print('Data related to birth year of users is not available for this city.')
    else:
        birth = dataset.groupby('Birth Year', as_index=False).count()
        print('Earliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_t))
    print('-'*40)

def D_D(dataset):
    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes' or choice=='y' or choice=='yus':
        choice=True
    elif choice=='no' or choice=='n' or choice=='nope':
        choice=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        D_D(dataset)
        return

    if choice:
        while 1:
            for i in range(5):
                print(dataset.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes' or choice=='y' or choice=='yus':
                continue
            elif choice=='no' or choice=='n' or choice=='nope':
                break
            else:
                print('You did not enter a valid choice.')
                return

def main():
    while True:
        city, month, day = filters()
        dataset = l_d(city, month, day)

        t_s(dataset)
        s_s(dataset)
        t_d_s(dataset)
        U_S(dataset)
        D_D(dataset)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y' and restart != 'yus':
            break

if __name__ == "__main__":
	main()

