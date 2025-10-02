import pandas as np
import matplotlib.pyplot as plt
import numpy as np

#laddat ner csv-fil och delat de i två kategorier x,y

all_x = []
all_y = []

with open("labs/Labb3/unlabelled_data.csv", "r") as csv_file:
    for line in csv_file:

        x,y = map(float, line.strip().split(","))

        all_x.append(x)
        all_y.append(y)  


#räta linjens ekvationy=kx+m --> y=-x  (0,0)  och (-2,2)
# klassificera i 1 eller 0. ???????zip -varför????????

def classify_point(x, y, k=-1, m=0):
    line_y = k*x + m
    if y>line_y:
        return 1
    else:
        return 0
for x,y in zip(all_x, all_y):
    label =classify_point(x, y, k=-1, m=0)          #hur går jag från detta till att få ut klasser på värdena?????????
    print("X: ", x, "Y: ", y, " class: ", label)

labelled_points = []                                #definiera lista
with open("labelled_data.csv", "w") as new_file:
    for x,y in zip(all_x, all_y):
        label =classify_point(x, y, k=-1, m=0) 
        new_file.write(f"{x}, {y}, {label}\n")
        labelled_points.append((x, y, label))        #append. sparar resultaten
    print("X:", x, " Y:", y, " class:",label)

class_0 = [(x, y) for x, y, group in labelled_points if group == 0]
class_1 = [(x, y) for x, y, group in labelled_points if group == 1]

class_0 = np.array(class_0)
class_1 = np.array(class_1)

plt.figure(figsize=(8, 6))
plt.scatter(class_0[:,0], class_0[:,1], color = "blue", label = "To the right from the line")
plt.scatter(class_1[:,0], class_1[:,1], color = "red", label ="To the left from the line")
plt.xlim(-6, 6)
plt.ylim(-6, 6)     
plt.xlabel("x")
plt.ylabel("y")            
plt.grid(True)         


k = -1   
m = 0    
x_values = np.linspace(-6, 6, 100)
y_values = [k*x + m for x in x_values] 


plt.plot(x_values, y_values, color='green', label='Separating line', linewidth=1)
plt.plot(x_values, y_values, color ="red", label= "Y = -X")
plt.legend()                   #skapar ruta med text
plt.show()
