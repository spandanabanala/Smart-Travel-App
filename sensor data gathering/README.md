# Sensor Data Gathering

Description:

To build a smart city application there is a need of real time or historical data. We need servers which can store and process large amount of data without data traffic issues. cloud is virtual data Center which are used to store, process data and give faster response to end user. By using cloud, we avoid data issues as well as Capacity of cloud servers vary with data traffic.

Part 1: – Gathering data Collected:

Smartphone application collect real time data of the precise location of the device and
number of steps taken by the person between two locations and the distance travelled which is
stored in cloud firebase.
 Take few steps and stop the device, display shows the location of the device, number of steps
taken, and distance travelled. This information is stored in a database of cloud in the background.

Technical diagram:


Part 2: Gathering open data:

• Dublin City Public Cycle Parking Stands gives the details about location of stands and other
details of location like
expanded_capacity,security_safetyrating,lighting,protection_weather,ease_access,proximity_cyclenetworkwhat type of area like commercial, retail, residential and transportation of the
area, education, recreational, entertainment, restaurant
https://data.gov.ie/dataset/dcc_public_cycle_parking_stands
• Parking Meters location tariffs and zones in Dublin city is the data which provides details
of Coach Bay location Coach Bay locations, further information, finished, x coordinate, y
coordinate, tariff zones.
https://data.gov.ie/dataset/parking-meters-location-tariffs-and-zones-in-dublin-city
• The above two data points are not real time data they are historical data provided by Dublin city
council.

Technical diagram:


URL for Cloud database: https://console.firebase.google.com/u/0/project/urban-computingf949f/database/data
Script: python script used to convert csv to json
