import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ave_spectra.dat', delimiter=r"\s+") 
#print(df,'\n')

fig, ax = plt.subplots() 

count = 0
for (columnName, columnData) in df.iteritems():
#   print('Colunm Name : ', columnName,type(columnName),'count=',count)
   if (count==0):
#      print('doing:', columnName)
      x = df[columnName]
#      print('read x=', x)
   else:
#      print('doing:', columnName)
#      print('type=',type(df[columnName]))
      y = df[columnName]+count*0.5
#      y = df[columnName]+count*0.5
      plt.plot(x, y)
   count+=1



#plt.legend(df.columns[1:])
names=df.columns[1:].tolist()
for i in range(len(names)-1):
    names[i] = names[i] + ' K'

names[-1] = 'Infinite T'

plt.legend(names, loc='upper right')
print(type(names))
print(names)
plt.xlabel('Shift (ppm)')
plt.ylabel('NMR spectra (a.u.)')
ax.invert_xaxis()   
plt.title('x=0.875  Sigma=0.94ppm  GCanonical')
#plt.xlim([-670,-630])
#plt.invert_xaxis()
plt.savefig('x875_b0p93_GCan.png')
#plt.ax.invert_xaxis()

#plt.show()
