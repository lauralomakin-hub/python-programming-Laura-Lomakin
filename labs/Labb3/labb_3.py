import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

all_x = []
all_y = []

with open("labs/Labb3/unlabelled_data.csv", "r") as csv_file:
    for line in csv_file:

        x,y = map(float, line.strip().split(","))

        all_x.append(x)
        all_y.append(y)  

#print(all_x)
#print(all_y)

plt.figure(figsize=(8, 6))
plt.scatter(all_x, all_y) 
plt.xlim(-6, 6)
plt.ylim(-6, 6)     
plt.xlabel("x")
plt.ylabel("y")            
plt.grid(True)              # chatgot, prompt: "alltså jag har kasst ögonmått jag skulle behöva linjal på skärmen och jag har touchskärm"


#

#Jag har punkterna(0,0) och (-2,2) sedan del A: 
#Jag sätter in x-värdena x_values för x och formlen för y=kx+m (k*xi + m) i y_values. (Martin Nilssson)
#Det funkade inte för då skapas bara linjen mellan mina två punkter jag ögonmåttat.
# testar np.linspace() skapar fler x-värden utifrån y=kx+m  (chatGPT och 
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html#sphx-glr-gallery-lines-bars-and-markers-axline-py

k = -1   
m = 0    
x_values = np.linspace(-6, 6, 100)
y_values = [k*x + m for x in x_values] 


plt.plot(x_values, y_values, color='green', label='Separating line', linewidth=2)
plt.plot(x_values, y_values, color ="red", label= "Y = -X")
plt.legend()                   #skapar ruta med text
plt.show()

