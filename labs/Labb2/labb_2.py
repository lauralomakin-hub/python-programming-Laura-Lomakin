import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re



def load_testpoints(filename):
    points = []
    with open(filename, "r") as file:
        
        for line in file:
            nums = re.findall(r"\((\d+\.?\d*),\s*(\d+\.?\d*)\)", line)
            if nums:
                w_str, h_str = nums[0]
                width, height = float(w_str), float(h_str)
                points.append((width, height))
                
    return points
testpoints = load_testpoints("testpoints.txt")

# test  print(testpoints[:1])

# separate function for datapoints



def load_datapoints(filename): 
    points = []
    with open(filename, "r") as file:
        
        for line in file:
            nums = re.findall(r"^\s*(\d+\.?\d*)\s*,\s*(\d+\.?\d*)\s*,\s*([01])\s*$", line)
            if nums:
                w_str, h_str, l_str = nums[0]
                width, height, label = float(w_str), float(h_str), int(l_str)
                points.append((width, height, label))
               
    return points
datapoints = load_datapoints("datapoints.txt")
# Test remove     print(datapoints[:1])     

import math
def euclidean_distance (testpoint_coords, datapoint_coords):
    return math.sqrt(
        ((testpoint_coords[0]-datapoint_coords[0])**2)+((testpoint_coords[1] - datapoint_coords[1])**2)
        )

#test

if testpoints and datapoints:
    tp = testpoints[0]
    dp = datapoints[0]

    dp_cord = dp[:2]
    dp_label = dp[2]

    euclidean_distance(tp, dp_cords)
    print (f"[TEST] tp={tp} dp={dp_cords} avstånd={d:.3f} label={dp_label}")





