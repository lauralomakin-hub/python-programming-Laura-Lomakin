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
print(testpoints[:1])

#-------- gör separat funktion för  -----------datapoints = load_data("datapoints.txt")



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
print(datapoints[:1])



#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

#def load_data(filename):
#    with open (filename, r) as file:
#    for line in file:
#        width, height = map(float(line.strip(),split())

#points.append((width, height))
              
#return points