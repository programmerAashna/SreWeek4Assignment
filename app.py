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

print("2. Pie chart for response code ")

rc_count = myCsv['rcode'].value_counts()
rc_count.plot.pie(figsize = (10,10))
plt.show()
#plt.savefig('piechart.png')

# Question 3: How many different, unique clients accessed this service?
print("3. Unique clients")
unique_clients = myCsv['clientloc'].nunique()
print("The number of unique clients = ",unique_clients)

# Question 4: Which client accessed the service the most? How many times did that client access the service?
print("4. Client that used the service the most and how many times was it used")
client_count = myCsv['clientloc'].value_counts()
used_service_most = client_count.keys().tolist()[0]
print("The client who used the service the most is : ",used_service_most)

count_of_most_used = client_count[0]
print("Number of times that the service was used = ",count_of_most_used)

#Question 5: For the 5 clients with the most requests,
# show a bar chart of how many times each client accessed the service
print("5. For the 5 clients with the most requests bar chart of how many times each client accessed the service")
first_5_clients = myCsv['clientloc']
five_clients_count = first_5_clients.value_counts().head()
print("First five clients : \n",five_clients_count)

#printing the count values from value_counts
#for idx,keys in enumerate(five_clients_count.index.tolist()):
#        myCountValue = five_clients_count[idx]
#        print(myCountValue)

five_clients_count.plot(kind='bar',x='Clients', y='Count')
plt.title('Clients who used the service the most')
plt.show()
#plt.savefig('barplot.png')
