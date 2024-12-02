# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:09:36 2024

@author: damjan.jurkovic
"""

#AOC 2024 - Day 1
#Part 1

with open("day_1.txt", "r") as inp:
    file = inp.readlines()
    
list1 = []
list2 = []

for line in file:
    line = line.split()
    for index, num in enumerate(line):
        if index %2 == 0: 
            list1.append(int(num))
        else:
            list2.append(int(num))
            
slist1 = sorted(list1)
slist2 = sorted(list2)

distance = 0
for i in range(len(list1)):
    distance += abs(slist1[i]-slist2[i])

print(distance)


#Part 2
similarity = 0
for num1 in slist1:
    for num2 in slist2:
        if num1 < num2:
            break
        elif num1 == num2:
            similarity += num1

print(similarity)
        
        
    