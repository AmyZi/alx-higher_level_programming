#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    totalW = 0
    totalScore = 0
    if (len(my_list) <= 0):
        return (0)
    for items in my_list:
        score, weight = item
        totalW += weight
        totalScore += score * weight
    return totalScore / totalW
