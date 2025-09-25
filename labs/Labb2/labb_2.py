import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re



def load_testpoints(filename):
    points = []
    with open(r"labs\Labb2\testpoints.txt", "r") as file:
        
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
    with open(r"labs\Labb2\datapoints.txt", "r") as file:
        
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

    dp_coords = dp[:2]               #anpassning för att bara få med två första värden
    dp_label = dp[2]                 #anpassning få med label som enskilt värde

    euclidean_distance(tp, dp_coords)


    distance = euclidean_distance (tp, dp_coords)
    print (f"[TEST] tp={tp} dp={dp_coords} avstånd={distance:.3f} label={dp_label}")

pichu_coords = [(width, height) for (width, height, label) in datapoints if label == 0]
pikachu_coords = [(width, height) for (width, height, label) in datapoints if label == 1]

#test att att alla datapoints är med:
print(f"Pichu {len(pichu_coords)} + {len(pikachu_coords)} = {len(datapoints)}")  


plt.scatter(
    [w for (w, h) in pichu_coords],
    [h for (w, h) in pichu_coords],
    color = "blue",
    label ="Pichu"
)

plt.scatter(
    [w for(w, h) in pikachu_coords],
    [h for (w, h) in pikachu_coords],
    color ="yellow",
    label ="Pikachu"
)

plt.xlabel = ("Width")
plt.ylabel = ("Height")
plt.legend()

plt.title("Pichu or Pikachu?")

plt.show()

#gör datan till tabell med kolumner:
datapoints_array = np.array(datapoints)

coords =  datapoints_array[:,:2]              #alla rader, upp till, men inte 2 inräknad.
labels = datapoints_array[:,2].astype(int)    # alla rader, bara kolumn 2 - (label). heltal.













 






