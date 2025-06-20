import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df  = pd.read_csv('ave_spectra.dat', delimiter=r"\s+") 
df2 = pd.read_csv('exp_data.csv', delimiter=';', names=['expx','expspec']) 

print(df['300.0'].max())
specmax1 = df['300.0'].max()
print('specmax1=',specmax1)
specmax2 = df2['expspec'].max()
print('specmax2=',specmax2)
scale = specmax1 / specmax2 
print('scale=',scale)


df2['expspec'] = df2['expspec'] * scale
print(df2['expspec'].max())


#print(df2)
#
c1 = df2["expx"]
#df = df.join(c1)
c2 = df2["expspec"]
#df = df.join(c2)

#print(df)
fig, ax = plt.subplots() 

count = 0
for (columnName, columnData) in df.iteritems():
   if (count==0):
      x = df[columnName]
   else:
      y = df[columnName]+count*1
      plt.plot(x, y)
   count+=1



names=df.columns[1:].tolist()
for i in range(len(names)-1):
    names[i] = names[i] + ' K'

names[-1] = 'Infinite T'
names.append('exp')

plt.legend(names, loc='upper right')
print(names)
plt.xlabel('Shift (ppm)')
plt.ylabel('NMR spectra (a.u.)')
plt.title('x=0.375  Sigma=0.94ppm  GrandCanonical')
plt.savefig('x375_b0p93_GCan.png')
plt.plot(c1,c2)
plt.xlim(-620.0, -680.0)
ax.invert_xaxis()   
plt.show()
