#Do testing for all the hypothesis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m

df = pd.read_csv("/Users/Devang/Desktop/Data_Analytics/Database/typeOfVehicle.csv",index_col=0)
df.dropna(axis=0,how='any',inplace=True)

#Total Accidents for each vehicle type
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
UT=UT*2
plt.bar(UT-0.6,df['Two-Wheelers - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df['Auto-Rickshaws - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df['Cars, Jeeps,Taxis - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df['Buses - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df['Other Motor Vehicles - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df['Other Vehicles/Objects - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Total Accidents for each vehicle type per 1L people of that state")
plt.show()

#Fatal Accidents for each vehicle type
plt.bar(UT-0.6,df['Two-Wheelers - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df['Auto-Rickshaws - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df['Cars, Jeeps,Taxis - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df['Buses - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df['Other Motor Vehicles - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df['Other Vehicles/Objects - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.2,1))
plt.title("Number of Fatal Accidents for each vehicle type per 1L people of that state")
plt.show()

#People Killed for each vehicle type
plt.bar(UT-0.6,df['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df['Auto-Rickshaws - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df['Buses - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df['Other Motor Vehicles - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df['Other Vehicles/Objects - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.25,1))
plt.title("Number of Persons Killed for each vehicle type per 1L people of that state")
plt.show()

#People Injured for each vehicle type
plt.bar(UT-0.6,df['Two-Wheelers - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df['Auto-Rickshaws - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df['Cars, Jeeps,Taxis - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df['Buses - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df['Other Motor Vehicles - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df['Other Vehicles/Objects - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.9,1))
plt.title("Number of Persons Injured for each vehicle type per 1L people of that state")
plt.show()

# ALL Data for 2 wheelers
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
plt.bar(UT-0.4,df['Two-Wheelers - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Two-Wheelers - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Two-Wheelers - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for 2 wheelers per 1L people of that state")
plt.show()

# ALL Data for Auto-rickshaws
plt.bar(UT-0.4,df['Auto-Rickshaws - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Auto-Rickshaws - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Auto-Rickshaws - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Auto-Rickshaws - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Auto-Rickshaws per 1L people of that state")
plt.show()

# ALL Data for Cars, jeeps and taxis
plt.bar(UT-0.4,df['Cars, Jeeps,Taxis - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Cars, Jeeps,Taxis - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Cars, Jeeps,Taxis - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Cars, Jeeps and Taxis per 1L people of that state")
plt.show()

# ALL Data for Buses
plt.bar(UT-0.4,df['Buses - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Buses - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Buses - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Buses - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Buses per 1L people of that state")
plt.show()

# ALL Data for Trucks, Tempos,MAVs,Tractors
plt.bar(UT-0.4,df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Trucks and Tractors per 1L people of that state")
plt.show()

# ALL Data for Other motor vehicles
plt.bar(UT-0.4,df['Other Motor Vehicles - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Other Motor Vehicles - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Other Motor Vehicles - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Other Motor Vehicles - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Other Motor Vehicles per 1L people of that state")
plt.show()

# ALL Data for Other vehicles/objects
plt.bar(UT-0.4,df['Other Vehicles/Objects - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df['Other Vehicles/Objects - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df['Other Vehicles/Objects - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df['Other Vehicles/Objects - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Other Vehicles/Objects per 1L people of that state")
plt.show()

df['Sum Total Road Accidents - 2014 per 1L people']=df['Two-Wheelers - Number of Road Accidents - Total - 2014 per 1L people']+df['Auto-Rickshaws - Number of Road Accidents - Total - 2014 per 1L people']+df['Cars, Jeeps,Taxis - Number of Road Accidents - Total - 2014 per 1L people']+\
	df['Buses - Number of Road Accidents - Total - 2014 per 1L people']+df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Total - 2014 per 1L people']+df['Other Motor Vehicles - Number of Road Accidents - Total - 2014 per 1L people']+\
	df['Other Vehicles/Objects - Number of Road Accidents - Total - 2014 per 1L people']
df['Sum Total Number of Persons Killed - 2014 per 1L people']=df['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people']+df['Auto-Rickshaws - Number of Persons - Killed - 2014 per 1L people']+df['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people']+\
	df['Buses - Number of Persons - Killed - 2014 per 1L people']+df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people']+df['Other Motor Vehicles - Number of Persons - Killed - 2014 per 1L people']+\
	df['Other Vehicles/Objects - Number of Persons - Killed - 2014 per 1L people']
df['Sum Total Number of Persons Injured - 2014 per 1L people']=df['Two-Wheelers - Number of Persons - Injured - 2014 per 1L people']+df['Auto-Rickshaws - Number of Persons - Injured - 2014 per 1L people']+df['Cars, Jeeps,Taxis - Number of Persons - Injured - 2014 per 1L people']+\
	df['Buses - Number of Persons - Injured - 2014 per 1L people']+df['Trucks, Tempos,MAVs,Tractors - Number of Persons - Injured - 2014 per 1L people']+df['Other Motor Vehicles - Number of Persons - Injured - 2014 per 1L people']+\
	df['Other Vehicles/Objects - Number of Persons - Injured - 2014 per 1L people']
df['Sum Total Fatal Road Accidents - 2014 per 1L people']=df['Two-Wheelers - Number of Road Accidents - Fatal - 2014 per 1L people']+df['Auto-Rickshaws - Number of Road Accidents - Fatal - 2014 per 1L people']+df['Cars, Jeeps,Taxis - Number of Road Accidents - Fatal - 2014 per 1L people']+\
	df['Buses - Number of Road Accidents - Fatal - 2014 per 1L people']+df['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Fatal - 2014 per 1L people']+df['Other Motor Vehicles - Number of Road Accidents - Fatal - 2014 per 1L people']+\
	df['Other Vehicles/Objects - Number of Road Accidents - Fatal - 2014 per 1L people']

#Plot to show total accidents, fatal accidents ,injured and killed for all vehicles for each state
plt.bar(UT-0.2,df['Sum Total Number of Persons Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Total Injured')
plt.bar(UT,df['Sum Total Number of Persons Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Total Killed')
plt.bar(UT+0.2,df['Sum Total Road Accidents - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Total Total Accidents')
plt.bar(UT+0.4,df['Sum Total Fatal Road Accidents - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Fatal Accidents')
plt.xticks(UT,df['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Total accidents, fatal accidents, killed and injured for each state per 1L people of that state")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Killed - 2014 per 1L people'])
plt.title("Total A vs K per 1L people")
plt.show()

plt.scatter(df['Sum Total Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Injured - 2014 per 1L people'])
plt.title("Total A vs I per 1L people")
plt.show()

plt.scatter(df['Sum Total Fatal Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Killed - 2014 per 1L people'])
plt.title("Total Fatal vs K per 1L people")
plt.show()

plt.scatter(df['Sum Total Fatal Road Accidents - 2014 per 1L people'],df['Sum Total Number of Persons Injured - 2014 per 1L people'])
plt.title("Total Fatal vs I per 1L people")
plt.show()