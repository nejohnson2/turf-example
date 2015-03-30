import pandas as pd
import json
from geojson import Point, Feature, FeatureCollection

'''
Convert data to GeoJson Format
'''

data = pd.read_csv('11222_subset.csv')


# -- Function for creating tuple
def create_geojson(data):
	x = (data['Longitude'], data['Latitude'])
	prop = {
		"created_date": data['Created Date'], 
		"complaint_type": data['Complaint Type'],
		"agency": data['Agency'],
		"agency_name": data['Agency Name'],
		"descriptor": data['Descriptor']
	}
	return [x,prop]
	

# -- Turn function into array
z = [Feature(geometry=Point(i[0], properties=i[1])) for i in data.apply(create_geojson, axis=1)]


# -- File to output
out_file = open("311.geojson","w")


json.dump(FeatureCollection(z), out_file)                                    


# Close the file
out_file.close()