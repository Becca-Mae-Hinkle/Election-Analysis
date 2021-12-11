#break

#import the datetime class from the datetime module
import datetime
#use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
#print("The time right now is ", now)



# Import the datetime class from the datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# print the present time
#print("The time right noe is ", now)

import csv
dir(csv) 

# assign a variable for the file to load and the path
file_to_load = 'Resources/election_results(1).csv'
#open the election results and read the file
election_data = open(file_to_load, 'r')
#
#to do: perform analysis
#close the file
election_data.close()

#open the election results and read the file
with open(file_to_load) as election_data:
    #to do: perform analysis
    print(election_data_)
