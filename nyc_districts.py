import csv, json

districts = {}

with open('nyc_historic_districts.csv','r') as f:

	reader = csv.reader(f)
	
	for row in reader:
		
		borough_name = row[2]
		area_name = row[5]	
		
		if borough_name not in districts:
		
			districts[borough_name] = []
				
		districts[borough_name].append(area_name)
		
		
	total = len(districts["MN"]) + len(districts["BK"]) + len(districts["QN"]) + len(districts["BX"]) + len(districts["SI"])

	
	print("There are", total, "historic districts in New York City.")
	
	for boroughs in districts:
		percentage = 0
		percentage = len(districts[boroughs]) * 100 / total
		print(round(percentage), "% are in", boroughs)
	
with open('scraped_districts.json', 'w') as f:
	f.write(json.dumps(districts,indent=4))	
