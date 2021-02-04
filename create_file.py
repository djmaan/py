#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:26:59 2021

@author: djmaan
"""


import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exist!".format(filename))
    sys.exit(1)