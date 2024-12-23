# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:20:25 2024

@author: damjan.jurkovic
"""
#AOC - Day 2
#Part 1

with open('day_2.txt', 'r') as inp:
    file = inp.readlines()

#Data transformation
data = []
for line in file:
    line = line.split()
    for ind, val in enumerate(line):
        line[ind] = int(val)
    data.append(line)

# safe = 0
# for line in data:
#     order = []
#     for ind, val in enumerate(line[:-1]):
#         if abs(line[ind+1] - val) > 3:
#             order.append(0)
#         else:
#             if line[ind+1] > val:
#                 order.append(1)
#             elif line[ind+1] < val:
#                 order.append(-1) 
#             else:
#                 order.append(0)
#     order = set(order)
#     if len(order) == 1:
#         if order != {0}:
#             safe += 1
        
#Part 2      
      
def check(data, safe):
    remaining = []
    for i, line in enumerate(data):
        order = []
        difference = []
        for ind, val in enumerate(line[:-1]):
            diff = line[ind+1] - val
            difference.append(diff)
            if abs(diff) > 3:
                order.append(0)
            else:
                if line[ind+1] > val:
                    order.append(1)
                elif line[ind+1] < val:
                    order.append(-1) 
                else:
                    order.append(0)
                    
        order_set = set(order)
        if len(order_set) == 1:
            if order_set != {0}:
                safe += 1
        #neće raditi ako postoji linija sa svim brojevima koji su jednaki
        else:
            remaining.append((i, difference))
    
    return(safe, remaining)
    
    
safe = 0
safe, remaining = check(data, safe)
        
print(safe)
print(remaining)

data_2 = []
for num, line in remaining:
    positive = 0
    negative = 0
    for ind, val in enumerate(line):
        if abs(val) > 3:
            data[num].pop(ind)
            data_2.append((num,data[num]))
            continue
        if val > 0:
            positive += 1
        if val < 0:
            positive += 1
        else:
            data[num].pop(ind)
            data_2.append((num,data[num]))
            continue
        if positive > negative:
            if negative == 1:
                safe += 1
        else:
            if positive == 1:
                safe += 1
                
        
print(safe)
print(remaining)


