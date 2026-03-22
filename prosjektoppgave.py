#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Oppgave del a av support dashboard
import pandas as pd
import os

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values #variabelnavn på ukedag
kl_slett = df['Klokkeslett'].values #variabelnavn på klokkeslett
varighet = df['Varighet'].values #variabelnavn på varighet
score = df['Tilfredshet'].values #variabelnavn på score


print(df.to_string()) # printer ut datasettet på skjerm


# In[7]:


# Oppgave del b
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values

#Summen av alle ukedagene
sum_mandag = 0
sum_tirsdag = 0
sum_onsdag = 0
sum_torsdag = 0
sum_fredag = 0

for ukedag in u_dag:
    if ukedag == 'Mandag':
        sum_mandag += 1
       
    if ukedag == 'Tirsdag':
        sum_tirsdag += 1
        
    if ukedag == 'Onsdag':
        sum_onsdag += 1
        
    if ukedag == 'Torsdag':
        sum_torsdag += 1

    if ukedag == 'Fredag':
        sum_fredag += 1

#printer ut summen av alle henvendelsene for hver av de fem ukedagene
print('antall mandager:', sum_mandag) 
print('antall tirsdager:',sum_tirsdag)
print('antall onsdager:', sum_onsdag)
print('antall torsdager:',sum_torsdag)
print('antall fredager:',sum_fredag) 

x = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']
y = [sum_mandag,sum_tirsdag, sum_onsdag, sum_torsdag, sum_fredag]

plt.bar(x,y) 
plt.show()


# In[15]:


# oppgave del c
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime, timedelta

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values

lengste = timedelta(0) #datetime.min
format = '%H:%M:%S'
korteste = timedelta(10000) #datetime.max

for var in varighet:
    var = datetime.strptime(var, format)
    var = timedelta(hours=var.hour, minutes=var.minute, seconds=var.second)
    if var > lengste:
        lengste = var #den husker den største verdien
    if var < korteste:
        korteste = var #den husker den minste verdien

#printer ut minste og lengste samtaletiden med informativ tekst
print(korteste, 'dette er den minste samtaletiden')
print(lengste, 'dette er den lengste samtaletiden')


# In[13]:


# krevende oppgave del d
# summen delt på henvendelser, telle antall henvendelser

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values

format = '%H:%M:%S'
sum = timedelta(0)

for var in varighet:
    var = datetime.strptime(var, format)
    var = timedelta(hours=var.hour, minutes=var.minute, seconds=var.second)
    sum += var
print(sum)
n= len(varighet)
print(n)

gjennomsnitt = sum/n
print('dette er gjennomsnitt av samtaletid:', gjennomsnitt)


# In[19]:


# oppgave del e
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values

#Supportvaktene delt i to-timers bolker, definert to ganger i start og slutt
format = '%H:%M:%S' #hour, minute, second

start_bolk_en = datetime.strptime('08:00:00', format) #datetime(hour = 8) #kl.8
slutt_bolk_en = datetime.strptime('10:00:00', format) #datetime(hour = 10) #kl.10
start_bolk_to = datetime.strptime('10:00:00', format) #datetime(hour = 10) #kl.10
slutt_bolk_to = datetime.strptime('12:00:00', format) #datetime(hour = 12) #kl.12
start_bolk_tre = datetime.strptime('12:00:00', format) #datetime(hour = 12) #kl.12
slutt_bolk_tre = datetime.strptime('14:00:00', format) #datetime(hour = 14) #kl.14
start_bolk_fire = datetime.strptime('14:00:00', format) #datetime(hour = 14) #kl.14
slutt_bolk_fire = datetime.strptime('16:00:00', format) #datetime(hour = 16) #kl.16

bolk_en = 0 #kl.8-10
bolk_to = 0 #kl.10-12
bolk_tre = 0 #kl.12-14
bolk_fire = 0 #kl.14-16

for tid in kl_slett:
    tid = datetime.strptime(tid, format)
    if start_bolk_en <= tid < slutt_bolk_en:
        bolk_en += 1
       
    if start_bolk_to <= tid < slutt_bolk_to:
        bolk_to += 1
        
    if start_bolk_tre <= tid < slutt_bolk_tre:
        bolk_tre += 1
        
    if start_bolk_fire <= tid < slutt_bolk_fire:
        bolk_fire += 1

print('klokkeslett 8-10:', bolk_en)
print('klokkeslett 10-12:', bolk_to)
print('klokkeslett 12-14:', bolk_tre)
print('klokkeslett 14-16:', bolk_fire)

labels = ['8-10', '10-12', '12-14', '14-16']
y = [bolk_en, bolk_to, bolk_tre, bolk_fire]

plt.pie(y, labels = labels)
plt.show()


# In[181]:


#del f

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#print(os.getcwd())
df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag'].values
kl_slett = df['Klokkeslett'].values
varighet = df['Varighet'].values
score = df['Tilfredshet'].values

#Kundens tilfredshet er delt i score
score_en = 0 #score 1-6, misfornøyd 
score_to = 0 #score 7-8, nøytralt 
score_tre = 0 #score 9-10, svært fornøyd 

score_en_start = 1.0 #score 1
score_en_slutt = 6.0 #score 6
score_to_start = 7.0 #score 7
score_to_slutt = 8.0 #score 8
score_tre_start = 9.0 #score 9
score_tre_slutt = 10.0 #score 10

for tilfredshet in score:
    if score_en_start <= tilfredshet <= score_en_slutt:
        score_en += 1

    if score_to_start <= tilfredshet <= score_to_slutt:
        score_to += 1

    if score_tre_start <= tilfredshet <= score_tre_slutt:
        score_tre += 1
        
print('Kundens tilfredshet er score 1-6:', score_en)
print('Kundens tilfredshet er score 7-8:', score_to) 
print('Kundens tilfredshet er score 9-10:', score_tre)


# In[183]:


sum = score_en + score_to + score_tre
print(sum) #summen av alle scorene


# In[174]:


prosent_en = score_en * 100/sum #regner i prosent
print('prosent for misfornøyde kunder:', prosent_en, '%')


# In[176]:


prosent_to = score_to * 100/sum #regner i prosent
print('prosent for nøytrale kunder:', prosent_to, '%')


# In[178]:


prosent_tre = score_tre * 100/sum #regner i prosent
print('prosent for svært fornøyde kunder:', prosent_tre, '%')


# In[192]:


nps = prosent_tre - prosent_en #positive kunder minus negative kunder
print('dette er nps av postive kunder minus negative kunder:', nps, '%')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




