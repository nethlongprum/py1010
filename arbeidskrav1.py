#!/usr/bin/env python
# coding: utf-8

# In[15]:


forsikring_elbil = 5000 # forsikring per år
forsikring_bensinbil = 7500 # forsikring per år
trafikkforsikringsavgift = 8.38 # kroner per dag for både elbil og bensinbil. Det er 365 dager i året 
drivstoffbruk_elbil = 0.2 # kWh/km
drivstoffbruk_strømpris = 2.00 #kr/kWh
drivstoffbruk_bensinbil = 1.00 #kr/km
bomavgift_elbil = 0.1 #kr/km
bomavgift_bensinbil = 0.3 #kr/km
bilbruk = 10000 #km/år

#Her regner jeg ut drivstoffbruk til bensinbil
#Deretter bomavgift for bensinbil
#Sist summerer totalutgiftene til bensinbil med trafikkforsikringsavgift ganger 365 dager
utgift_drivstoff_bensinbil = drivstoffbruk_bensinbil*bilbruk
utgift_bomavgift_bensinbil = bomavgift_bensinbil*bilbruk
trafikkforsikringsavgift_år = trafikkforsikringsavgift*365

#printer ut totalkostnaden
#ganger med forsikring
total_utgift_bensinbil = utgift_drivstoff_bensinbil+utgift_bomavgift_bensinbil+trafikkforsikringsavgift_år+forsikring_bensinbil
print(total_utgift_bensinbil)


# In[11]:


#Her regner jeg ut drivstoffbruk til elbil med strømpris
#Deretter bomavgift
#Sist summerer totalutgiftene til elbil med trafikkforsikring ganger 365 dager
utgift_drivstoff_elbil = drivstoffbruk_elbil*drivstoffbruk_strømpris*bilbruk
utgift_bomavgift_elbil = bomavgift_elbil*bilbruk
trafikkforsikringsavgift_år = trafikkforsikringsavgift*365

#printer ut totalkostnaden
#ganger med forsikring
total_utgift_elbil = utgift_drivstoff_elbil+utgift_bomavgift_elbil+trafikkforsikringsavgift_år+forsikring_elbil
print(total_utgift_elbil)

