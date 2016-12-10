import csv

with open('National_Register_of_Historic_Places.csv','r') as f:

	reader = csv.reader(f)
	
	for row in reader:

		with open("nys_historic_landmarks_new.csv",'w', newline='') as f:
			writer = csv.writer(f, delimiter=',')
			#output = [county_name]
			for row in reader:
				writer.writerows([[row[1], row[4], row[5], row[0]]])
	
