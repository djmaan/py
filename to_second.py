#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:45:20 2021

@author: djmaan
"""


def to_second(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours:"))
    minutes = int(input("Enter the number of minutes:"))
    seconds = int(input("Enter the number of sconds:"))
    
    print("That's  {} seconds".format(to_second(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue]")
    
print("Good bye!")
