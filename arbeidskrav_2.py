#!/usr/bin/env python
# coding: utf-8

# In[34]:


år = 2024
alder = int(input('hvilket år er du født?')) #Skriv inn årstall
print('Alderen din er:', år - alder) #printer ut årstall til skjerm og regner ut alder på skjerm



import math 
pizza = 0.25
antall_elever = int(input('Skriv inn antall elever:'))
antall_elever_pizza = antall_elever * pizza
opprundet1 = math.ceil(antall_elever_pizza) # tallet må rundes opp til heltall
print('Du må handle:', opprundet1, 'pizza') #printer ut hvor mye pizza som du må handle og runder opp til nærmeste heltall



import numpy as np
v_grad = float(input('Skriv inn gradtall:'))
v_rad = v_grad*np.pi/180
print(f'graden blir til: {v_rad:0.2f} radianer') #Her brukes stringformatering



data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}
land = str(input("Skriv inn et land: "))
x = data[land]
print(x[0], 'er hovedstaden i',land,'og det er', x[1],' mill. innbyggere i', x[0])



data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}
land = str(input(" Skriv inn nytt land: ")) #Her skriver brukeren inn nytt land
hovedstad = str(input(" Skriv inn nytt hovedstad: ")) #Her skriver brukeren inn hovedstad
innbyggertall = str(input(" Skriv inn nytt innbyggertall: ")) #Her skriver brukeren inn innbyggertall
data[land] = [hovedstad, innbyggertall]
print(data)



import math

def figur_areal_omkrets(a, b):
    pi = 3.14
    # 3.14 * radius * radius
    # radius er halvdelen av en diameter
    r = a/2
    # areal = g * h/2
    areal_halvsirkel = (pi*r*r)/2 #A er areal på en halv sirkel
    areal_trekant = b * a/2
    total_areal = areal_halvsirkel + areal_trekant
    

    omkrets_halvsirkel = pi * r #Omkrets til en sirkel delt på 2
    hypotenusen = math.sqrt(a * a + b * b)
    omkrets_trekant = hypotenusen + b # a er en side i trekanten og den er ikke med fordi a er inne i figuren. 
    total_omkrets = omkrets_trekant + omkrets_halvsirkel
    return total_omkrets, total_areal

omkrets, areal = figur_areal_omkrets(5,4)
print (f'Omkrets og areal av figuren = {omkrets:0.2f}, {areal:0.2f}  ') #Her brukes stringformatering
       



import numpy as np
import matplotlib.pyplot as plt

def akse (x):
   
   y = -2 * x*x - 5
   plt.plot (x, y)
   plt.show()
    
x = np.linspace(-10, 10, 200)
akse(x)
























