#!/usr/lib/python
from __future__ import division
import math
import time
import csv
import xlsxwriter 
#import pandas
import itertools
from openpyxl import Workbook

def write_xls(filename, data):
	wb = Workbook(write_only=True)
	ws = wb.create_sheet()
	#print (data)
	#for i in data:
	headers = list(set(itertools.chain.from_iterable(data)))
	ws.append(headers)

	for elements in data:
		ws.append([elements.get(h) for h in headers])

	wb.save(filename)

#x number of people straight
x=0
#y number of people turn

Pall = 1


'''
#MIT output
Ppedestrian > Ppassenger
Pfit > Plarge
Pfemale > Pmale
Phighstatus > Plowerstatus
Plawful > Punlawful
Pyoung > Pelder
Pmore > Pless
Phumans > Ppets
'''
temp = []
results = []
count = 0
while x < 15:
	#print (x)
	y=0
	while y < 15:
	#	print y
		if x < y:
			temp = {"number straight" : x,
					"number turn" : y,
					"outcome_rational" : "turn",
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femalaeVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "turn",
					"outcome_MIT_humansVSpets" : "turn"
					}
			#print temp
		elif x > y:
			temp = {"number straight" : x,
					"number turn" : y,
					"outcome_rational" : "straight",
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femalaeVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "turn",
					"outcome_MIT_humansVSpets" : "turn"
					}
			#print temp
		elif x==y:
			temp = {"number straight" : x,
					"number turn" : y,
					"outcome_rational" : "no decision",
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femalaeVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "turn",
					"outcome_MIT_humansVSpets" : "turn"
					}
		#print (temp)
		results.append(temp)
		count = count + 1
		#with open('resultsCSV.csv', mode='w',newline='') as results_file:
		#	#results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		#	results_writer = csv.writer(results_file)
		#	results_writer.writerows(temp)
		
		y=y+1
	x=x+1
row=0
col=0
print (results)
write_xls("resultsCVS.csv",results)

'''
csv_columns = ['number straight','number turn','outcome_rational','outcome_MIT_PedestrianVSpassengers','outcome_MIT_fitVSlarge','outcome_MIT_femalaeVSmale','outcome_MIT_hightStatusVSlowerStatus','outcome_MIT_lawfulVSunlawful','outcome_MIT_youngVSelder','outcome_MIT_moreVSless','outcome_MIT_humansVSpets']
csv_file = "resultsCVS.csv"
for i in (results): 
	print(i)
	try:
		with open(csv_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			writer.writeheader()
			for data in i:
				writer.writerow(data)
	except IOError:
		print("I/O error")
'''