# Nicholas Newman
# CS 551SE HW2
# 09-16-2018

from geopy.geocoders import Nominatim 
from geopy.distance import geodesic 
from geopy import distance

geolocator = Nominatim(user_agent="TheGeodesicDistanceCalculator")

print '\n'
print 'Hello, Welcome to the Geodesic Distance Calculator!..'
print 'Please Enter your two addresses below in the following format..'
print 'Address Example #1: 1314 chavez st, Las Vegas, NM'
print 'Address Example #2: 1701 bryant st, Denver, CO'
print '\n'

query1 = raw_input('Enter Address #1 ==> ')
query2 = raw_input('Enter Address #2 ==> ') 

location1 = geolocator.geocode(query1)
location2 = geolocator.geocode(query2)

print'\n','Query Address #1 ==> ',(location1.address) 
print'Query Address #2 ==> ',(location2.address),'\n'
print'Query Address #1 (Latitude, Longitude) ==> ',(location1.latitude, location1.longitude)
print'Query Address #2 (Latitude, Longitude) ==> ',(location2.latitude, location2.longitude),'\n'

Add1 = (location1.latitude, location1.longitude)
Add2 = (location2.latitude, location2.longitude)

print'The Distance between the two Addresses is ==> ',(distance.geodesic(Add1,Add2).miles),' Miles'
print'Thank You for using the Geodesic Calculator! '
print '\n'