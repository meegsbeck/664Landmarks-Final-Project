import csv
import json

landmarks = {}

with open('nhl_links.csv','r') as f:

	reader = csv.reader(f)
	
	for row in reader:
		
		new_york_landmarks = row[1]
		county_name = row[2]
		city_name = row[3]
		landmark_name = row[4]
		
		
		#trying to pull out just NY landmarks
		#then append county, city, and landmark name to it
		if "NEW YORK" in new_york_landmarks:
			
			#landmarks[new_york_landmarks.strip()] = county_name.strip(), city_name.strip(), landmark_name.strip()
			#print(landmarks)
			
			if new_york_landmarks not in landmarks:
			
				landmarks[new_york_landmarks] = {}
				#county_dict = {}
				
			if county_name not in landmarks[new_york_landmarks]:
				
				landmarks[new_york_landmarks][county_name] = {}
				
			if city_name not in landmarks[new_york_landmarks][county_name]:
			
				landmarks[new_york_landmarks][county_name][city_name] = []	
				
			landmarks[new_york_landmarks][county_name][city_name].append(landmark_name.strip())
			
			#landmarks[new_york_landmarks].append(county_name.strip())
			#landmarks[new_york_landmarks].append(city_name.strip())
			#landmarks[new_york_landmarks].append(landmark_name.strip())	
			
			
#	print(landmarks)

with open('scraped_landmarks.json', 'w') as f:
	f.write(json.dumps(landmarks,indent=4))	