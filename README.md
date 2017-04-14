# .osm_Easy
Repository containing a bunch of scripts to obtain certain data from .osm files and write it to .csv files

In the folder Scripts(scripts) there are four modules: 
	OSM_TO_CSV(scripts/OSM_TO_CSV/OSM_to_CSV.py) gets one .osm file as an input and generate two .csv files containing the nodes and Ways(right now it just have info about elements with highway tags) of the .osm file.
	The three scripts contained in waysCSV_TO_Highways(scripts/waysCSV_TO_Highways) do the following: 
		The first script(scripts/waysCSV_TO_Highways/1. waysCSV_to_wayswithtagsincolumnsCSV.py) gets the .csv file containing the Ways and write tags' names to columns.
		The second script(scripts/waysCSV_TO_Highways/2. wayswithtagsCSV_toHighwaysCSV.py) gets the .csv file containing the Ways with tags' names in columns and clean it, leaving just useful 		columns.
		The third script(scripts/waysCSV_TO_Highways/3. highwayswithCoordinates.py) gets the last .csv file containing the Ways and generate .csv file with ways containing its Coordinates

In the folder dataexample(dataexample) an example of the generated data using the different modules can be found. The original .osm file was one of the City of Granada (Spain)
