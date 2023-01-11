#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    blist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            blist[count] = True
        else:
            blist[count] = False
    return(blist)

"Write a function that finds all multiples of 2 in a list."
