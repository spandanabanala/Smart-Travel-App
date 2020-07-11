# Application Development

Description:

 We discussed on the urban data gathering where data collected from the location sensor and the open data from govt.ie is stored on the firebase server. With the present application, I can know about location information, bike stands and information about just-eat bikes.

Part 1: Data fusion and analysis data:

Citizens find difficult to know about current location information (type of location: retail, commercial, residential), Surrounding of location (Restaurants, Entertainment, Recreation) Transportation facilities, Security of the place.

By using the present application, we can know about this information and also it will give information
about bike stands which are about 50 meters radius from the current location to place bikes
It also provides just eat bike stand which in proximity of 50 meters from the current location.


Data Fusion and Algorithm:

The system uses the current location details latitude and longitude and compare with the latitude and
longitude provided by the open data set and provide the details of the location within 20 meters
proximity.

 X,Y(current location) -0.0032<= X,Y(open dataset)<= X,Y(current location) +0.0032

Note:0.0032=20-meter distance
Task 2

Data Visualization Motivation–
To show real time status of current location
To show locations of Sheffield stand and just eat bike details
To show information about the surrounding and type of location 




Technologies used:
• Mit inventor
• GPS sensor (gives location details)
• Pedometer (to know steps taken and distance)

 

