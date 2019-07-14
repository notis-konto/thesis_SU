#!/usr/lib/python
from __future__ import division
import math
import time

p_ahead = int(raw_input( " Please specify the number of people ahead: "))
p_side = int(raw_input( " Please specify the number of people in the side: "))
selection = int(raw_input( " Which direction should match? (straight = 0, turn = 1): "))

print ("\n")
P1=0.00
P2=0.00
step = 0.01
EV1 = p_ahead * P1
EV2 = p_side * P2
EV1_array = []
EV2_array = []
P1_array = []
P2_array = []
data = []
c = 0

while P1 < 1.01:
	check = False
	EV1_array = []
	P1_array = []
	EV1=p_ahead * P1
	EV1_array.append(EV1)
	P1_array.append(P1)
	while P2 < 1.01:
		EV2 = p_side * P2
		EV2_array = []
		P2_array = []
		EV2_array.append(EV2)
		P2_array.append(P2)
		if str(EV1) == str(EV2):
			check = True
			
			#at this point we check the contitions. One check is to keep stable P1 and increase P2 and the other is to keep stable P2 and increase P1
			if selection == 0:
				print ("PROBABILITIES TO GO AHEAD")
				if EV1 < (p_side * (P2+step)) and EV1 > (p_side * (P2-step)):		
					print ("P1:" + str(P1) + ", P2: (" + str(P2) + ", 1]")
					c = c + 1
				elif EV1 > (p_side * (P2+step)) and EV1 < (p_side * (P2-step)):
					print ("P1:" + str(P1) + " , P2: (0," + str(P2) + ")")
					c = c + 1
				if (p_ahead * (P1+step)) < EV2 and (p_ahead * (P1-step)) > EV2:
					print ("P1: (" + str(P1) + ", 1] , P2: " + str(P2) )
					c = c + 1
				elif (p_ahead * (P1+step)) > EV2 and (p_ahead * (P1-step)) < EV2:
					print ("P1: (0," + str(P1) + ") , P2: " + str(P2) )
					c = c + 1
				else:
					print ("ZONG")
				
			if selection == 1:
				print ("PROBABILITIES TO TURN")
				if EV1 < (p_side * (P2+step)) and EV1 > (p_side * (P2-step)):		
					print ("P1: " + str(P1) + " , P2: (0," + str(P2) + ")")
					c = c + 1
				elif EV1 > (p_side * (P2+step)) and EV1 < (p_side * (P2-step)):
					print ("P1: " + str(P1) + " , P2: (" + str(P2) + ", 1] ")
					c = c + 1
				if (p_ahead * (P1+step)) < EV2 and (p_ahead * (P1-step)) > EV2:
					print ("P1: (0," + str(P1) + ") , P2: " + str(P2) )
					c = c + 1
				elif (p_ahead * (P1+step)) > EV2 and (p_ahead * (P1-step)) < EV2:
					print ("P1: (" + str(P1) + ", 1] , P2 :" + str(P2))
					c = c + 1
				else:
					print ("ZONG")	
				
		P2 = P2 + step
	if check == False:
		if EV1 > EV2 and selection == 0:
			print ("P1: " + str(P1) + " , P2: (0,1]")
			c = c + 1
		elif EV1 < EV2 and selection == 1:
			print ("P1: " + str(P1) + " , P2: (0,1]")
			c = c + 1
	P2 = 0.00
	P1 = P1 + step

d=0
while P2 < 1.01:
	check = False
	EV2_array = []
	P2_array = []
	EV2=p_side * P2
	EV2_array.append(EV2)
	P2_array.append(P2)
	while P1 < 1.01:
		EV1 = p_ahead * P1
		EV1_array = []
		P1_array = []
		EV1_array.append(EV1)
		P1_array.append(P1)
		if str(EV1) == str(EV2):
			check = True
			
		P1 = P1 + step
	if check == False:
		if EV1 > EV2 and selection == 0:
			print ("P1: [0,1] , P2: " + str(P2))
			c = c + 1
		elif EV1 < EV2 and selection == 1:
			print ("P1: [0,1] , P2: " + str(P2))
			c = c + 1
	P1 = 0.00
	P2 = P2 + step
print ("TOTAL ROWS: " + str(c) )
