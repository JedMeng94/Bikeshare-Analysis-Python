
# coding: utf-8

# ## Bikeshare Project

# In[1]:


print('Hello! Lets Explore some US bikeshare data\nWould you like see data for Chicaco, New York, or Washington?')


# In[2]:


import numpy as npa
import pandas as pd
import time

## Filenames
chicago =  pd.read_csv(r"C:\Users\Jed\mystuff\chicago.csv")
new_york_city = pd.read_csv(r'C:\Users\Jed\mystuff\new_york_city.csv')
washington = pd.read_csv(r'C:\Users\Jed\mystuff\washington.csv')


# In[3]:


def get_sheet():
    city = str(input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')).lower()
    while city not in ('chicago','new york','washington'):
        city = str(input('Please choose a valid city\n')).lower()    
    if city == 'chicago':
        city_input = chicago
    elif city == 'new york':
        city_input = new_york_city
    elif city == 'washington':
        city_input = washington
    
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
    while time_period not in ('month','day','none'):       
        time_period = input('Please choose a valid filter\n').lower()
    #If they answer month
    if time_period == 'month':
        what_month = str(input('\nWhich month? January, February, March, April, May, or June?\n')).lower()
        while what_month not in ('january','february','march','april','may','june'):  
            time_period = input('Please choose a valid month\n').lower
        new = pd.to_datetime(city_input['Start Time'])
        if what_month == 'january':
            return (city_input.loc[(new> '2017-1-1')&(new< '2017-2-1')])
        elif what_month == 'february':
            return (city_input.loc[(new> '2017-2-1')&(new< '2017-3-1')])
        elif what_month == 'march':
            return (city_input.loc[(new> '2017-3-1')&(new< '2017-4-1')])
        elif what_month == 'april':
            return (city_input.loc[(new> '2017-4-1')&(new< '2017-5-1')])
        elif what_month == 'may':
            return (city_input.loc[(new> '2017-5-1')&(new< '2017-6-1')])
        elif what_month == 'june':
            return (city_input.loc[(new> '2017-6-1')&(new< '2017-7-1')])
        
        
    if time_period == 'day':
        what_day = int(input('\nWhat day of the week? Sunday=1\n'))
        while what_day not in (1,2,3,4,5,6,7):
            what_day = input('Please choose a day 1-7')
        new = pd.to_datetime(city_input['Start Time']).dt.dayofweek
        return (city_input.loc[new == what_day])
    
    if time_period == 'none':
        return city_input
    
            
        


# In[4]:


#this is the case for none in the filters
def popular_month(city_file):
    pop_month = city_file.groupby(pd.to_datetime(city_file['Start Time']).dt.month)['Start Time'].agg('count').idxmax()
    if pop_month == 1: return 'January'
    elif pop_month == 2 : return 'February'
    elif pop_month == 3 : return 'March'
    elif pop_month == 4 : return 'April'
    elif pop_month == 5 : return 'June'
    elif pop_month == 6 : return 'July'
    


# In[5]:


def popular_day(city_file):
    pop_day = city_file.groupby(pd.to_datetime(city_file['Start Time']).dt.dayofweek)['Start Time'].agg('count').idxmax()
    if pop_day == 1: return 'Monday'
    elif pop_day == 2 : return 'Tuesday'
    elif pop_day == 3 : return 'Wednesday'
    elif pop_day == 4 : return 'Thursday'
    elif pop_day == 5 : return 'Friday'
    elif pop_day == 6 : return 'Saturday'
    elif pop_day == 7 : return 'Sunday'


# In[6]:


def popular_hour(city_file):
    pop_hour = city_file.groupby(pd.to_datetime(city_file['Start Time']).dt.hour)['Start Time'].agg('count').idxmax()
    return str(pop_hour)


# In[7]:


def trip_duration(city_file):
    total = city_file['Trip Duration'].sum()
    average = city_file['Trip Duration'].mean()
    return total,average


# In[8]:


def popular_stations(city_file):
    pop_start = city_file.groupby(['Start Station'])['Start Station'].agg('count').idxmax()
    pop_end = city_file.groupby(['End Station'])['End Station'].agg('count').idxmax()
    return pop_start, pop_end


# In[9]:


def popular_trip(city_file):
    return city_file.groupby(['Start Station','End Station'])['Start Station'].agg('count').idxmax()


# In[10]:


def users(city_file):
    return city_file['User Type'].value_counts()


# In[11]:


def gender(city_file):  
    return city_file['Gender'].value_counts()


# In[12]:


def birth_years(city_file):
    earliest = (city_file.groupby(['Birth Year'])['Birth Year']).min().idxmin()
    recent = (city_file.groupby(['Birth Year'])['Birth Year']).max().idxmax()
    popular = city_file.groupby(['Birth Year'])['Birth Year'].agg('count').idxmax()
    return earliest,recent,popular


# In[13]:


def display_data(city_file):
    count = 0
    while True:
        display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n').lower()
        
        if display == 'yes':
            count += 5 
            print (city_file[count:(count+5)])
        else:
            break            
    return None


# In[15]:


def statistics():
    # Filter by city (Chicago, New York, Washington)
    city = get_sheet()

    start_time = time.time()

    #TODO: call popular_month function and print the results
    q = input('Would you like to see the most popular month? Yes or No\n').lower()
    if q == 'yes':
        print('Calculating the first statistic...')
        print('The most popular month is '+popular_month(city))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
    else:
        None
    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    
    start_time = time.time()

    # TODO: call popular_day function and print the results
    print('The most popular day of the week is '+popular_day(city))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    print('The most popular hour is '+popular_hour(city))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    
    tots,avg= tuple(trip_duration(city))
    print("Total trip duration is {} seconds\nAverage trip duration is {} seconds".format(tots,avg))    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    start,end = tuple(popular_stations(city))
    print('The most popular start station is {}\nThe most popular end station is {}'.format(start,end))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    begin,end = popular_trip(city)
    print('The most popular trip was {} to {}'.format(begin,end))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    print('The following are counts of users:')
    print(users(city))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    
    # What are the counts of gender?
    # TODO: call gender function and print the results
    try:
        print('The genders are as follows:')
        print(gender(city))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
    except: print('No gender data available')
    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years? earliest,recent,popular
    # TODO: call birth_years function and print the results
    try:
        earliest,recent,popular = birth_years(city)
        print('The earliest birth year is {}\nThe latest birth year is {}\nThe average birth year is {}'.format(earliest,recent,popular))
        print("That took %s seconds." % (time.time() - start_time))
    except: print('No birth data available')
    # Display five lines of data at a time if user specifies that they would like to
    display_data(city)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()
    else:
        None
        


if __name__ == "__main__":
	statistics()
    

