import re

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

myDataFile = 'C:/Users/AASHNA/OneDrive/Desktop/nasa_access_log_500K.csv'
myCsv = pd.read_csv(myDataFile, parse_dates = ['timestamp'])
#print(myCsv)

# Question 1: Date range for access log
print ("1. Calculate date range")
mindate = min(myCsv['timestamp']).date()
maxdate = max(myCsv['timestamp']).date()
print(f"Date range is {mindate} to {maxdate}")

# Question 2:  Display a pie chart in which each pie slice
# represents a response code and the size of the pie piece
# is proportional to the number of responses with that code.

print("\n2. Pie chart for response code ")

rc_count = myCsv['rcode'].value_counts()
rc_count.plot.pie(figsize = (10,10))
#plt.show()
#plt.savefig('piechart.png')

# Question 3: How many different, unique clients accessed this service?
print("\n3. Unique clients")
unique_clients = myCsv['clientloc'].nunique()
print("The number of unique clients = ",unique_clients)

# Question 4: Which client accessed the service the most? How many times did that client access the service?
print("\n4. Client that used the service the most and how many times was it used")
client_count = myCsv['clientloc'].value_counts()
used_service_most = client_count.keys().tolist()[0]
print("The client who used the service the most is : ",used_service_most)

count_of_most_used = client_count[0]
print("Number of times that the service was used = ",count_of_most_used)

#Question 5: For the 5 clients with the most requests,
# show a bar chart of how many times each client accessed the service

print("\n5. For the 5 clients with the most requests bar chart of how many times each client accessed the service")
first_5_clients = myCsv['clientloc']
five_clients_count = first_5_clients.value_counts().head()
print("First five clients with the most requests:\n",five_clients_count)

five_clients_count.plot(kind='bar',x='Clients', y='Count')
plt.title('Clients who used the service the most')
#plt.show()
#plt.savefig('barplot.png')

#Question 6: Which resource (which path) was accessed the most?
print("\n6. The path that was accessed the most")
path = myCsv['path']
countOfPath = path.value_counts()
mostAccessedPath = countOfPath.keys().tolist()[0]
print("The most accessed path was: ",mostAccessedPath)

#Question 7: The first element in the path indicates a resource class. List all of the accessed resource classes.
print("\n 7. List all of the resource classes")
pathString = repr(countOfPath)
pattern = "/(.*?)/"
print("All the resource classes : ")
for element in path :
    resourceClass = re.findall(pattern,element)
    # still need to try and print unique resorce class names
    print(resourceClass)
    
#Question 9: Which day of the week typically had the most requests?
print("9. Fiinding the day of the week with the most requests")
dateTimestamp = pd.to_datetime(myCsv['timestamp'])
# dateTimeStamp.dt.dayofweek - day of the week in numbers
dayOfTheWeek = dateTimestamp.dt.day_name()
dayWithMostRequests = dayOfTheWeek.value_counts().keys().tolist()[0]
print("The day that received the most requests: ",dayWithMostRequests)

#Question 10: During which hour of the day did the site typically serve the most data?
print("10. Finding the hour of day that served the most data")
hourOfDay = dateTimestamp.dt.hour
hourOfDayServingMostData = hourOfDay.value_counts().keys().tolist()[0]
print("The hour of day that served the most data: ",hourOfDayServingMostData,"th hour")
