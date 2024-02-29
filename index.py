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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("\n Please enter city that you like to analyse:-(chicago, new york city, washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a Valid City :- \n (chicago, new york city, washington)")         
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        monthes = ['January','February','March','April','May','June','None']
        month = input("\n Which month would you like to Select? ( January, February, March, April, May, June) \n If you don't have monthe to select Please Enter (None)\n").title()
        if month in monthes:
            break
        else:
            print("\n Please enter a Valid month :- \n (January, February, March, April, May, June) OR None")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saterday','Sunday','None']
        day = input("\n Please Enter Day that you like to Select:- \n (Monday ,Tuesday ,Wednesday ,Thursday ,Friday , Saterday , Sunday) Or None if you donot have a spasifice Day to Select \n").title()
        if day in days:
            break
        else:
            print("\n Please enter a Valid Day :- (Monday ,Tuesday ,Wednesday ,Thursday ,Friday , Saterday , Sunday) OR None")

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
                  
# convert the start tuime column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])                   

# extract day and month from start time to create new coulmn
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
                    
#filter data by month
    if month != 'None':
    # Convert Month Name to Its Number like January to be 1
        monthes= ['January','February','March','April','May','June']
        month = monthes.index(month)+1
    
        df = df[df['month']==month]
    
#filter data by day    
    if day != 'None':
        df = df[df['day_of_week']==day.title()]
                                                                                                                                                                                                                   
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Popular_month = df['month'].mode()[0]
    print("\n Most Popular Month:", Popular_month)

    # TO DO: display the most common day of week
    Popular_day = df["day_of_week"].mode()[0]
    print("\n Most Popular Day Of Week:", Popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Popular_start_hour = df['hour'].mode()[0]
    print("\n Most Popular Start Hour:", Popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_start_station = df["Start Station"].mode()[0]
    print("\n Most Popular Start Station:", Popular_start_station)

    # TO DO: display most commonly used end station
    Popular_end_station = df["End Station"].mode()[0]
    print("\n Most Popular End Station:", Popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    group_data_fild = df.groupby(["Start Station" , "End Station"])
    Popular_compination_station =  group_data_fild.size().sort_values(ascending= False ).head(1)
    print("Most Frequent Combination Of Start Station and End Station Trip: \n, Popular_compination_station")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time= df["Trip Duration"].sum()
    print( "Total Travel Time: ", Total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time =  df["Trip Duration"].mean()
    print( "Mean Travel Time:  ",  mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\n Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Count_user_type = df["User Type"].value_counts()
    print(" User Type Stats:  ", Count_user_type)
    

    # TO DO: Display counts of gender
    if city.title() == "Chicago" or city.title() == "New Yourk City":
          Count_gender = df["Gender"].value_counts()
          print ("Count Of Gender Value:  ", Count_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    earlist = int(df['Birth Year'].min())
    print (" \n The Earliest Year of Birth  ", earlist)
        
    most_recent = int(df['Birth Year'].max())
    print (" \n The Most Resent Year of Birth  ", most_recent)
        
    mast_common = int(df["Birth Year"].mode()[0])
    print (" \n The Most Common Users Year of Birth  ", mast_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        Response=["yes" , "no"]
        User_response= input("\n Do you want to see 5 rows of data? \n Please Enter 'Yes' or 'No'").lower()
        if User_response in Response:
            if User_response== "yes":
                start_loc = 0
                end_loc= 5
                data = df.iloc[start_loc:end_loc,:9]
                print (data)
            break
        else:
            print("Pleas Enter Valid data, 'Yes' or 'No'")
    if User_response == "yes":
         while True:
          More_response = input("\n Do you want to see more rows of data? \n Please Enter 'Yes' or 'No'").lower()
          if User_response in Response:
            
             if More_response== "yes":
                start_loc += 5
                end_loc += 5
                data = df.iloc[start_loc:end_loc,:9]
                print (data)
             else:
                break
         else:
            print("Pleas Enter Valid data, 'Yes' or 'No'")






def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()