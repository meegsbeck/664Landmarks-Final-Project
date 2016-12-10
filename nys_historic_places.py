import csv
import json

nys_historic_places = {}

with open('National_Register_of_Historic_Places.csv','r') as f:

	reader = csv.reader(f)
	
	for row in reader:
		
		landmark_name = row[0]
		county_name = row[1]
		location = row[6]
		
		if county_name not in nys_historic_places:
		
			nys_historic_places[county_name] = {}
		
		if location not in nys_historic_places[county_name]:
		
			nys_historic_places[county_name][location] = []
		
		if landmark_name not in nys_historic_places[county_name][location]:
		
			nys_historic_places[county_name][location].append(landmark_name)
		
		
with open('scraped_state_landmarks.json', 'w') as f:
	f.write(json.dumps(nys_historic_places,indent=4))	