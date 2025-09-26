#----Importera bibliotek
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import math

#----Datainläsning tets och datapunkter i varsin funktion
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
testpoints = load_testpoints(r"labs\Labb2\testpoints.txt")

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
datapoints = load_datapoints(r"labs\Labb2\datapoints.txt")


#----Funktion för Euclidean distance  


def euclidean_distance (testpoint_coords, datapoint_coords):
    return math.sqrt(
        ((testpoint_coords[0]-datapoint_coords[0])**2)+((testpoint_coords[1] - datapoint_coords[1])**2)
        )

###TEST###

#if testpoints and datapoints:
#    tp = testpoints[0]
#   dp = datapoints[0]

#    dp_coords = dp[:2]               #anpassning för att bara få med två första värden
#    dp_label = dp[2]                 #anpassning få med label som enskilt värde

#    euclidean_distance(tp, dp_coords)


#    distance = euclidean_distance (tp, dp_coords)
#    print (f"[TEST] tp={tp} dp={dp_coords} avstånd={distance:.3f} label={dp_label}")

#----Dela upp data för plottning

pichu_coords = [(width, height) for (width, height, label) in datapoints if label == 0]
pikachu_coords = [(width, height) for (width, height, label) in datapoints if label == 1]

###TEST
# kolla att att alla datapoints är med:

print(f"Pichu {len(pichu_coords)} + {len(pikachu_coords)} = {len(datapoints)}")  


#----Förberedande ARRAY för tabeller kolumner (används inte just nu)
datapoints_array = np.array(datapoints)

coords =  datapoints_array[:,:2]              #alla rader, upp till, men inte 2 inräknad.
labels = datapoints_array[:,2].astype(int)    # alla rader, bara kolumn 2 - (label). heltal.

###TEST 
#testar distansberäkningarna:

for tp in testpoints:                          #klassificera enkild tetspoint
    distances = []
    for (width, height, label) in datapoints:
        dist = euclidean_distance(tp, (width, height))
        distances.append(((width, height, label), dist))

print(distances[:5])                         #kontrollera fem första

print(f"testpoint: {len(testpoints)} datapoints: {len(datapoints)}")


#--- Funktion - Hämta k-NN

def get_neighbors(datapoints, tp, k):                #lista med träningsdata, testdata, antal grannar vi vill hitta
	distances = list()
	for (w, h, label) in datapoints:                 #<---loop-version
		dist = euclidean_distance(tp, (w, h))
		distances.append(((w, h,label), dist))
	distances.sort(key=lambda item: item[1])         #sortera på distans
	neighbors = list()
	for i in range(k):
		neighbors.append(distances[i][0])            #själva punkten - inte distansen
	return neighbors


#note to self:
    #Om du vill optimera för bonusuppgifterna (accuracy, många upprepningar)
    # kan du ersätta loopen ovan med en NumPy-vektoriserad beräkning:
    #   diff = coords - np.array(tp)
    #   dists = np.sqrt(np.sum(diff**2, axis=1))
    #   combined = list(zip(dists, labels))
    # Då får du samma resultat men snabbare när datan blir större.

### TEST med 1-nearest neighbor

label_name = {0: "Pichu", 1: "Pikachu"}
for tp in testpoints:
    neighbors = get_neighbors(datapoints, tp, k=1)    # Hämtar 1-närmsta granne
    neighbor = neighbors[0]
    label = neighbor[2]                               #label/namn från den grannen
    name = label_name[label]
    print(f"Testpunkt: {tp}")
    print(f"Närmsta granne: {neighbors}")
    print(f"Klassificering: {name}")
    print("-"*40)                                     #för läsbarhet i terminalen


from collections import Counter
def majority_vote(neighbors):                         #neighbors listan (w,h; label från get_neighbors)
     labels = [lbl for (_, _, lbl) in neighbors]
     counts = Counter(labels)                         #räknar antal o:or och 1:or
     return counts.most_common(1)[0][0]                #returnerar namnet med flest röster


for tp in testpoints:
    neighbors = get_neighbors(datapoints, tp, k=10)    # Hämtar 1-närmsta granne
    neighbor = neighbors[0]
    label = majority_vote(neighbors)                            #label/namn från den grannen
    name = label_name[label]
    print(f"[k=10], Testpoint {tp} name: {name}")
    print("-"*40)                                     #för läsbarhet i terminalen





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

label_name = {0: "Pichu", 1: "Pikachu"}


for i, tp in enumerate(testpoints):
    neighbors = get_neighbors(datapoints, tp, k=10)
    label = majority_vote(neighbors)
    name = label_name[label]
    x, y = tp

    plt.scatter(
        tp[0],
        tp[1],
        color = "red",
        marker = "*",
        s=150
    )
    plt.text(
        tp[0]+0.1, 
        tp[1]+ 0.1, 
        name,
        fontsize=9, 
        color = "red"
    )

plt.xlabel("Width")
plt.ylabel("Height")
plt.legend()

plt.title("Pichu or Pikachu?")

plt.show()
