#Do testing for all the hypothesis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m

df = pd.read_csv("/Users/Devang/Desktop/Data_Analytics/Database/laneAccidents.csv",index_col=0)
df.dropna(axis=0,how='any',inplace=True)

#Total Accidents
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
plt.bar(UT-0.2,df['Single Lane - Accident - 2014 per 1L people'],width=0.2,color='b',align='center',label='Single Lane')
plt.bar(UT,df['Two Lanes - Accident - 2014 per 1L people'],width=0.2,color='g',align='center',label='Double lane')
plt.bar(UT+0.2,df['3 Lanes or more w.o Median - Accident - 2014 per 1L people'],width=0.2,color='r',align='center',label='3 Lanes or more w.o Median')
plt.bar(UT+0.4,df['4 Lanes with Median - Accident - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='4 Lanes with Median')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Accidents for each lane per 1L people of that state")
plt.legend(loc="best")
plt.show()

#injured
plt.bar(UT-0.2,df['Single Lane - Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Single Lane')
plt.bar(UT,df['Two Lanes - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Double lane')
plt.bar(UT+0.2,df['3 Lanes or more w.o Median - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='3 Lanes or more w.o Median')
plt.bar(UT+0.4,df['4 Lanes with Median - Injured - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='4 Lanes with Median')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Injured for each lane per 1L people of that state")
plt.legend(loc="best")
plt.show()

#Killed.
plt.bar(UT-0.2,df['Single Lane - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Single Lane')
plt.bar(UT,df['Two Lanes - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Double lane')
plt.bar(UT+0.2,df['3 Lanes or more w.o Median - Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='3 Lanes or more w.o Median')
plt.bar(UT+0.4,df['4 Lanes with Median - Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='4 Lanes with Median')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Killed for each lane per 1L people of that state")
plt.show()

# ALL Data for Single lane
plt.bar(UT-0.2,df['Single Lane - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Injured')
plt.bar(UT,df['Single Lane - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Killed')
plt.bar(UT+0.2,df['Single Lane - Accident - 2014 per 1L people'],width=0.2,color='yellow',align='center',label="Accidents")
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Persons Injured, Killed; Road Accidents Total for Single Lane per 1L people of that state")
plt.legend(loc="best")
plt.show()

# ALL Data for 2 lane
plt.bar(UT-0.2,df['Two Lanes - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Injured')
plt.bar(UT,df['Two Lanes - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Killed')
plt.bar(UT+0.2,df['Two Lanes - Accident - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Accidents')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Persons Injured, Killed; Road Accidents Total for Double Lane per 1L people of that state")
plt.legend(loc="best")
plt.show()

# ALL Data for 3 lane
plt.bar(UT-0.2,df['3 Lanes or more w.o Median - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Injured')
plt.bar(UT,df['3 Lanes or more w.o Median - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Killed')
plt.bar(UT+0.2,df['3 Lanes or more w.o Median - Accident - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Accidents')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Persons Injured, Killed; Road Accidents Total for 3 Lanes or more w.o Median per 1L people of that state")
plt.legend(loc="best")
plt.show()

# ALL Data for 4 lane
plt.bar(UT-0.2,df['4 Lanes with Median - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Injured')
plt.bar(UT,df['4 Lanes with Median - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Killed')
plt.bar(UT+0.2,df['4 Lanes with Median - Accident - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Accidents')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Number of Persons Injured, Killed; Road Accidents Total for 4 Lanes with Median per 1L people of that state")
plt.legend(loc="best")
plt.show()


#Plot to show total accidents,injured and killed for each state
#See places where green is higher than blue and red is higher than green
df['Sum Total Number of Persons Killed - 2014 per 1L people']=df['Single Lane - Killed - 2014 per 1L people']+df['Two Lanes - Killed - 2014 per 1L people']+df['3 Lanes or more w.o Median - Killed - 2014 per 1L people']+df['4 Lanes with Median - Killed - 2014 per 1L people']
df['Sum Total Number of Persons Injured - 2014 per 1L people']=df['Single Lane - Injured - 2014 per 1L people']+df['Two Lanes - Injured - 2014 per 1L people']+df['3 Lanes or more w.o Median - Injured - 2014 per 1L people']+df['4 Lanes with Median - Injured - 2014 per 1L people']
df['Sum Total Road Accidents - 2014 per 1L people']=df['Single Lane - Accident - 2014 per 1L people']+df['Two Lanes - Accident - 2014 per 1L people']+df['3 Lanes or more w.o Median - Accident - 2014 per 1L people']+df['4 Lanes with Median - Accident - 2014 per 1L people']

plt.bar(UT-0.2,df['Sum Total Road Accidents - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT,df['Sum Total Number of Persons Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Total Injured')
plt.bar(UT+0.2,df['Sum Total Number of Persons Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Total Killed')
plt.xticks(UT,df['State/UT'],rotation='vertical')
plt.title("Total accidents, injured and killed for each state per 1L people of that state")
plt.legend(loc="best")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Killed - 2014 per 1L people'])
plt.title("Total A vs K per 1L people")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Injured - 2014 per 1L people'])
plt.title("Total A vs I per 1L people")
plt.show()