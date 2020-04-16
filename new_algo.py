#!/usr/lib/python
from __future__ import division
import math
import time
import csv
import xlsxwriter 
#import pandas
import itertools
from openpyxl import Workbook


P1=0.01
P2=0.01
step = 0.01
P1=float("{:.2f}".format(P1))
P2 = float("{:.2f}".format(P2))
EV1_array = []
EV2_array = []
P1_array = []
P2_array = []
data = []
c = 0

def write_xls(filename, data):
	wb = Workbook(write_only=True)
	
	ws = wb.create_sheet()

	headers = list(set(itertools.chain.from_iterable(data)))
	ws.append(headers)

	for elements in data:
		ws.append([elements.get(h) for h in headers])
	
	wb.save(filename)

#x number of people straight
x=1
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
calc1 = []
calc2 = []
calc3 = []
calc4 = []

results = []
probabilities =[]
count = 0
while x < 150:
	#print (x)
	y=1
	while y < 150:
	#	print y
		if x < y:
			temp = {"number straight" : x,
					"number turn" : y,
					"outcome_rational" : "straight",
					"EV_RAT" : x,
					"EV_MIT" : y,
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femaleVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "straight",
					"outcome_MIT_humansVSpets" : "turn"
					}
			selection = 1
			#print temp
		elif x > y:
			temp = {"number straight" : x,
					"number turn" : y,
					"EV_RAT" : y,
					"EV_MIT" : y,
					"outcome_rational" : "turn",
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femaleVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "turn",
					"outcome_MIT_humansVSpets" : "turn"
					}
			#print temp
			selection = 2
		elif x==y:
			temp = {"number straight" : x,
					"number turn" : y,
					"EV_RAT" : x,
					"EV_MIT" : y,
					"outcome_rational" : "no decision",
					"outcome_MIT_PedestrianVSpassengers" : "turn",
					"outcome_MIT_fitVSlarge" : "turn",
					"outcome_MIT_femaleVSmale" : "turn",
					"outcome_MIT_hightStatusVSlowerStatus" : "turn",
					"outcome_MIT_lawfulVSunlawful" : "turn",
					"outcome_MIT_youngVSelder" : "turn",
					"outcome_MIT_moreVSless" : "no decision",
					"outcome_MIT_humansVSpets" : "turn"
					}
			selection =2
		results.append(temp)
		count = count + 1
		
		p_ahead = x
		p_side = y
		EV1 = p_ahead * P1
		EV2 = p_side * P2
		
		P1=0.01
		#print ("PROBABILITIES TO TURN FOR: Straigt = " + str(x) + ", turn = " + str(y) )

		while P1 < 1.00:
			check = False
			#EV1_array = []
			#P1_array = []
			EV1=p_ahead * P1
			EV1 = float("{:.2f}".format(EV1))
			#EV1_array.append(EV1)
			P2 = 0.01
			#P1_array.append(P1)
			while P2 < 1.00:
				#print ("PROBABILITIES TO TURN FOR: Straigt = " + str(x) + ", turn = " + str(y) )
				EV2 = p_side * P2
				EV2 = float("{:.2f}".format(EV2))
				#EV2_array = []
				#P2_array = []
				#EV2_array.append(EV2)
				#P2_array.append(P2)
				P1 = float("{:.2f}".format(P1))
				P2 = float("{:.2f}".format(P2))
				#if str(EV1) == str(EV2):
					#print ("with probabilities P1=" + str(P1) + " and P2=" + str(P2) + " the EV is the same EV=" + str(EV1))
					#print ("next p side:" + p_side * (P2+step) + " ,previous p side: " + p_side * (P2-step) + " ,next p ahed: " + p_ahead * (P1+step) + " ,previous p ahead:  " + p_ahead * (P1-step) )

					#at this point we check the contitions. One check is to keep stable P1 and increase P2 and the other is to keep stable P2 and increase P1

				if selection == 1:
					#print ("PROBABILITIES TO TURN FOR: Straigt = " + str(x) + ", turn = " + str(y) )
					if EV1 < (p_side * (P2+step)) and EV1 > (p_side * (P2-step)):
						calc1data = "[0.01,"+str(P2)+")"
						calc1 = {"number straight" : x,
								"number turn" : y,
								"P1":P1, 
								"P2": calc1data}
						#print (calc1)
						temp.update( calc1 )
						probabilities.append(calc1)
						#print ("after that point,having the same probability P1 and increasing P2, the EV of the people on the side is higher, so the car should go ahead. Before that point,decreasing P2, the car should have selected to turn. \n")
					elif EV1 > (p_side * (P2+step)) and EV1 < (p_side * (P2-step)):
						#calc2 = print ("2.P1: " + str(P1) + " , P2: (" + str(P2) + ", 1] ")
						calc2data = "("+str(P2)+", 1]"
						calc2 = {"number straight" : x,
								"number turn" : y,
								"P1":P1,
								"P2": calc2data
								}
							#print (calc2)
							#temp.update( calc2 )
						probabilities.append(calc2)
						#	print ("after that point,having the same probability P1 and increasing P2, the EV of the people ahead is higher, so the car should turn. Before,decreasing P2, that point the car should have selected to go ahead. \n")
					if (p_ahead * (P1+step)) < EV2 and (p_ahead * (P1-step)) > EV2:
						#calc3 = print ("3.P1: (0.01," + str(P1) + ") , P2: " + str(P2) )
						calc3data = "(0.01," + str(P1) + ")"
						calc3 = {"number straight" : x,
								"number turn" : y,
								"P1":calc3data,
								"P2":P2
								}
						temp.update( calc3 )
						probabilities.append(calc3)
						#	print ("after that point,having the same probability P2 and increasing P1, the EV of the people on the side is higher, so the car should go ahead.Before,decreasing P1, that point the car should have selected to turn. \n")
					elif (p_ahead * (P1+step)) > EV2 and (p_ahead * (P1-step)) < EV2:
							#calc41 = ("4.P1: (" + str(P1) + ", 1], P2: " + str(P2))
						calc4data = "(" + str(P1) + ", 1]"
						calc4 = {"number straight" : x,
								"number turn" : y,
								"P1":calc4data,
								"P2":P2
								}
							#print (calc4)
							#print (calc41)
							#temp.update( calc4 )
						probabilities.append(calc4)
						#	print ("after that point,having the same probability P2 and increasing P1, the EV of the people ahead is higher, so the car should turn.Before that point,decreasing P1, the car should have selected to go ahead. \n")
					else:
						#print ("ZONG")
						None
				P2 = P2 + step
			P1 = P1 + step


		y=y+1
	x=x+1
#print (probabilities)
#write_xls("resultsCVS.csv",results)
write_xls("results-prob.csv",probabilities)



