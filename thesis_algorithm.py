#!/usr/lib/python
from __future__ import division
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
tempP1 = None
tempP2 = None
def myFunc(e):
	return e['P2']
#Function to write data to excel
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

#Declaration of tables
temp = []
calc1 = []
calc2 = []
calc3 = []
calc4 = []

results = []
probabilities =[]
count = 0
while x < 51:
	y=1
	while y < 51:
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
					"outcome_MIT_humansVSpets" : "turn",
					"outcome_GEC_moreVSless" : "straight",
					"outcome_GEC_humansVSpets" : "turn",
					"outcome_GEC_lawfulVSunlawfu" : "turn"
					}
			selection = 1
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
					"outcome_MIT_humansVSpets" : "turn",
					"outcome_GEC_moreVSless" : "turn",
					"outcome_GEC_humansVSpets" : "turn",
					"outcome_GEC_lawfulVSunlawfu" : "turn"
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
					"outcome_MIT_humansVSpets" : "turn",
					"outcome_GEC_moreVSless" : "no decision",
					"outcome_GEC_humansVSpets" : "turn",
					"outcome_GEC_lawfulVSunlawfu" : "turn"					
					}
			selection =2
		results.append(temp)
		count = count + 1
		
		p_ahead = x
		p_side = y
		EV1 = p_ahead * P1
		EV2 = p_side * P2
		sorted1 = []
		sorted2 = []
		P1=0.01
		
		tempP2 = None
		while P1 < 1.00:
			check = False
			EV1=p_ahead * P1
			EV1 = float("{:.2f}".format(EV1))
			P2 = 0.01
			while P2 < 1.00:
				EV2 = p_side * P2
				EV2 = float("{:.2f}".format(EV2))
				P1 = float("{:.2f}".format(P1))
				P2 = float("{:.2f}".format(P2))
				if selection == 1:
					if (EV1 < (p_side * (P2+step)) and EV1 > (p_side * (P2-step))) and (EV1 != EV2 and EV1 > EV2 ):
						if (P2-step) > 0 :
							calc1data = "[0.01,"+str(P2)+"]"
							calc1 = {"number straight" : x,
									"number turn" : y,
									"original_outcome_rational" : "straight",
									"new_outcome_rational" : "turn",
									"B2" : "lawfulVSunlawful", 
									"B4" : "PedestrianVSpassengers",
									"B5" : "youngVSelder",
									"B6" : "fitVSlarge",
									"B7" : "femaleVSmale",
									"B8" : "hightStatusVSlowerStatus",
									"LowerLimit" : "0.01",
									"UpperLimit" : str(P2),
									"P1":P1,
									"P2": calc1data,
									"EV1" : str(EV1),
									"EV2" : str(EV2)
									}
							tempP1 = calc1
					if ( (p_ahead * (P1+step)) > EV2) and (EV1 != EV2 and EV1 > EV2):
						if 	(P1-step) > 0:
							calc4data = "[" + str(P1) + ", 1]"
							calc4 = {"number straight" : x,
									"number turn" : y,
									"original_outcome_rational" : "straight",
									"new_outcome_rational" : "turn",
									"B2" : "lawfulVSunlawful", 
									"B4" : "PedestrianVSpassengers",
									"B5" : "youngVSelder",
									"B6" : "fitVSlarge",
									"B7" : "femaleVSmale",
									"B8" : "hightStatusVSlowerStatus",
									"LowerLimit" : str(P1),
									"UpperLimit" : 1,
									"P1":calc4data,
									"P2": P2,
									"EV1" : str(EV1),
									"EV2" : str(EV2)
									}
							if not tempP2:
								tempP2 = calc4
								probabilities.append(tempP2)
					else:
						None
				P2 = P2 + step
			if tempP1:
				probabilities.append(tempP1)
				tempP1 = None
			P1 = P1 + step
		y=y+1
	x=x+1
write_xls("results",results)
write_xls("probabilities",probabilities)
