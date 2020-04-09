#!/usr/lib/python
from __future__ import division
import math
import time
import csv
import xlsxwriter 



#x number of people straight
x=1
#y number of people turn
y=1
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
while x < 5:
	#print x
	while y < 5:
	#	print y
		if x < y:
			temp = [{"number straight" : x,
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
					}]
			#print temp
		elif x > y:
			temp = [{"number straight" : x,
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
					}]
			#print temp
		elif x==y:
			temp = [{"number straight" : x,
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
					}]
		#print (temp)
		results.append(temp)
		count = count + 1
		with open('resultsCSV.csv', mode='w',newline='') as results_file:
			#results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			results_writer = csv.writer(results_file)
			results_writer.writerows(temp)
		
		y=y+1
	x=x+1
row=0
col=0
workbook = xlsxwriter.Workbook('results.xlsx') 
worksheet = workbook.add_worksheet("My sheet") 
for i in (results): 
    worksheet.write(row, col, i) 
    row += 1

	#test