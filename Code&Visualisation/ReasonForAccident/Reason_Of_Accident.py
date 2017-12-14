# Do testing for all the hypothesis
# Compare final total on the basis of column on all 3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m

df = pd.read_csv("/Users/Devang/Desktop/Data_Analytics/Database/reasonOfAccident.csv",index_col=0)
df.dropna(axis=0,how='any',inplace=True)

#Total Killed for each reason 
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
UT=UT*3
plt.bar(UT-0.6,df['Fault of Driver-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Driver')
plt.bar(UT-0.4,df['Fault of Driver of other vehicles-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='black',align='center',label='Other driver\'s')
plt.bar(UT-0.2,df['Fault of Pedestrian-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Pedestrian')
plt.bar(UT,df['Defect in Condition of Motor Vehicle-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Condition of Vehicle')
plt.bar(UT+0.2,df['Defect in Road Condition-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Road Condition')
plt.bar(UT+0.4,df['Weather Condition-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Weather Condition')
plt.bar(UT+0.6,df['Fault of Passenger-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Passenger')
plt.bar(UT+0.8,df['Poor light-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='orange',align='center',label='Poor light')
plt.bar(UT+1.0,df['Falling of boulders-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='pink',align='center',label='Boulders')
plt.bar(UT+1.2,df['Other causes/causes not known-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='cyan',align='center',label='Other Causes')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title("Number of Persons Killed for each reason per 1L people of that state")
plt.show()

#Total Injured for each reason
plt.bar(UT-0.6,df['Fault of Driver-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Driver')
plt.bar(UT-0.4,df['Fault of Driver of other vehicles-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='black',align='center',label='Other driver\'s')
plt.bar(UT-0.2,df['Fault of Pedestrian-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Pedestrian')
plt.bar(UT,df['Defect in Condition of Motor Vehicle-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Condition of Vehicle')
plt.bar(UT+0.2,df['Defect in Road Condition-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Road Condition')
plt.bar(UT+0.4,df['Weather Condition-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Weather Condition')
plt.bar(UT+0.6,df['Fault of Passenger-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Passenger')
plt.bar(UT+0.8,df['Poor light-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='orange',align='center',label='Poor light')
plt.bar(UT+1.0,df['Falling of boulders-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='pink',align='center',label='Boulders')
plt.bar(UT+1.2,df['Other causes/causes not known-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='cyan',align='center',label='Other Causes')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title("Number of Persons Injured for each reason per 1L people of that state")
plt.show()

#Total Accidents for each reason
plt.bar(UT-0.6,df['Fault of Driver-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='r',align='center',label='Driver')
plt.bar(UT-0.4,df['Fault of Driver of other vehicles-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='black',align='center',label='Other driver\'s')
plt.bar(UT-0.2,df['Fault of Pedestrian-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Pedestrian')
plt.bar(UT,df['Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='b',align='center',label='Condition of Vehicle')
plt.bar(UT+0.2,df['Defect in Road Condition-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Road Condition')
plt.bar(UT+0.4,df['Weather Condition-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Weather Condition')
plt.bar(UT+0.6,df['Fault of Passenger-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Passenger')
plt.bar(UT+0.8,df['Poor light-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='orange',align='center',label='Poor light')
plt.bar(UT+1.0,df['Falling of boulders-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='pink',align='center',label='Boulders')
plt.bar(UT+1.2,df['Other causes/causes not known-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='cyan',align='center',label='Other Causes')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title("Number of Accidents for each reason per 1L people of that state")
plt.show()

# ALL Data for fault of driver
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
plt.bar(UT-0.2,df['Fault of Driver-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Fault of Driver-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Fault of Driver-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for fault of driver per 1L people of that state")
plt.show()

# ALL Data for fault of driver of other vehicle
plt.bar(UT-0.2,df['Fault of Driver of other vehicles-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Fault of Driver of other vehicles-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Fault of Driver of other vehicles-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for fault of driver of other vehicles per 1L people of that state")
plt.show()

# ALL Data for fault of pedestrian
plt.bar(UT-0.2,df['Fault of Pedestrian-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Fault of Pedestrian-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Fault of Pedestrian-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for fault of pedestrian per 1L people of that state")
plt.show()

# ALL Data for Defect in Condition of Motor Vehicle
plt.bar(UT-0.2,df['Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Defect in Condition of Motor Vehicle-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Defect in Condition of Motor Vehicle-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Defect in Condition of Motor Vehicle per 1L people of that state")
plt.show()

# ALL Data for Defect in Road Condition
plt.bar(UT-0.2,df['Defect in Road Condition-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Defect in Road Condition-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Defect in Road Condition-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Defect in Road Condition per 1L people of that state")
plt.show()

# ALL Data for Weather Condition
plt.bar(UT-0.2,df['Weather Condition-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Weather Condition-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Weather Condition-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Weather Condition per 1L people of that state")
plt.show()

# ALL Data for Fault of Passenger
plt.bar(UT-0.2,df['Fault of Passenger-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Fault of Passenger-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Fault of Passenger-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for fault of Passenger per 1L people of that state")
plt.show()

# ALL Data for Poor light
plt.bar(UT-0.2,df['Poor light-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Poor light-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Poor light-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Poor light per 1L people of that state")
plt.show()

# ALL Data for Falling of boulders
plt.bar(UT-0.2,df['Falling of boulders-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Falling of boulders-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Falling of boulders-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Falling of boulders per 1L people of that state")
plt.show()

# ALL Data for Other causes/causes not known
plt.bar(UT-0.2,df['Other causes/causes not known-Total No. of Road Accidents - 2014 per 1L people'],width=0.2,color='g',align='center',label='Accidents')
plt.bar(UT,df['Other causes/causes not known-Number of Persons-Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Injured')
plt.bar(UT+0.2,df['Other causes/causes not known-Number of Persons-Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Road Accidents, Injured, Killed Total for Other causes/causes not known per 1L people of that state")
plt.show()

df['Sum Total Road Accidents - 2014 per 1L people']=df['Fault of Driver of other vehicles-Total No. of Road Accidents - 2014 per 1L people']+df['Fault of Pedestrian-Total No. of Road Accidents - 2014 per 1L people']+df['Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014 per 1L people']+\
	df['Defect in Road Condition-Total No. of Road Accidents - 2014 per 1L people']+df['Weather Condition-Total No. of Road Accidents - 2014 per 1L people']+df['Fault of Passenger-Total No. of Road Accidents - 2014 per 1L people']+\
	df['Poor light-Total No. of Road Accidents - 2014 per 1L people']+df['Falling of boulders-Total No. of Road Accidents - 2014 per 1L people']+df['Other causes/causes not known-Total No. of Road Accidents - 2014 per 1L people']+\
	df['Fault of Driver-Total No. of Road Accidents - 2014 per 1L people']

df['Sum Total Number of Persons Killed - 2014 per 1L people']=df['Fault of Driver of other vehicles-Number of Persons-Killed - 2014 per 1L people']+df['Fault of Pedestrian-Number of Persons-Killed - 2014 per 1L people']+df['Defect in Condition of Motor Vehicle-Number of Persons-Killed - 2014 per 1L people']+\
	df['Defect in Road Condition-Number of Persons-Killed - 2014 per 1L people']+df['Weather Condition-Number of Persons-Killed - 2014 per 1L people']+df['Fault of Passenger-Number of Persons-Killed - 2014 per 1L people']+\
	df['Poor light-Number of Persons-Killed - 2014 per 1L people']+df['Falling of boulders-Number of Persons-Killed - 2014 per 1L people']+df['Other causes/causes not known-Number of Persons-Killed - 2014 per 1L people']+\
	df['Fault of Driver-Number of Persons-Killed - 2014 per 1L people']

df['Sum Total Number of Persons Injured - 2014 per 1L people']=df['Fault of Driver of other vehicles-Number of Persons-Injured - 2014 per 1L people']+df['Fault of Pedestrian-Number of Persons-Injured - 2014 per 1L people']+df['Defect in Condition of Motor Vehicle-Number of Persons-Injured - 2014 per 1L people']+\
	df['Defect in Road Condition-Number of Persons-Injured - 2014 per 1L people']+df['Weather Condition-Number of Persons-Injured - 2014 per 1L people']+df['Fault of Passenger-Number of Persons-Injured - 2014 per 1L people']+\
	df['Poor light-Number of Persons-Injured - 2014 per 1L people']+df['Falling of boulders-Number of Persons-Injured - 2014 per 1L people']+df['Other causes/causes not known-Number of Persons-Injured - 2014 per 1L people']+\
	df['Fault of Driver-Number of Persons-Injured - 2014 per 1L people']

#Plot to show total accidents,injured and killed for all vehicles for each state
plt.bar(UT-0.2,df['Sum Total Road Accidents - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT,df['Sum Total Number of Persons Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Total Injured')
plt.bar(UT+0.2,df['Sum Total Number of Persons Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Total Killed')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.title("Total accidents, killed and injured for each state per 1L people of that state")
plt.legend(loc="best")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Killed - 2014 per 1L people'])
plt.title("Total A vs K per 1L people")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Injured - 2014 per 1L people'])
plt.title("Total A vs I per 1L people")
plt.show()