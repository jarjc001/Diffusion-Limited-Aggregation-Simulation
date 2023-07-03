import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv('3000_mean_plot.csv')


Na = df["Na"][0:10].tolist() 
Rm_mean = df["Rm_mean"][0:10].tolist() 
Rm_sd = df["Rm_sd"][0:10].tolist() 
ln_Na = df["ln_Na"][0:10].tolist() 
ln_Rm_1 = df["ln_Rm_1"][0:10].tolist() 
ln_Rm_2 = df["ln_Rm_2"][0:10].tolist() 
ln_Rm_3 = df["ln_Rm_3"][0:10].tolist() 
ln_Rm_mean = df["ln_Rm_mean"][0:10].tolist()  
ln_Rm_SD = df["ln_Rm_SD"][0:10].tolist()  
regression = df["regression"][0:10].tolist()  

r=np.linspace(2,5,1000)
m_ = df["regression"][10] 
cplus_ = df["regression"][0] 
print(m_)
print(cplus_)
map_lnNa_ = (m_*r)+cplus_


plt.plot(ln_Rm_1,ln_Na,'sr',label='Cluster 1',markersize=6)           #first cluster
#plt.plot(ln_Rm_2,ln_Na,'',label='2$^{nd}$ Cluster',markersize=7)           #2nd cluster
plt.plot(ln_Rm_3,ln_Na,'b^',label='Cluster 2',markersize=9)           #3rd cluster
plt.errorbar(ln_Rm_mean,ln_Na,xerr = ln_Rm_SD,fmt ='k.',capsize=4, elinewidth=1,markersize=9,label='Mean')
plt.plot(r,map_lnNa_,'k--',linewidth=2)           #line of best fit

plt.show
plt.xlabel('ln R',fontsize=15)          #labels x axis as 'r (μm)'
plt.ylabel('ln N$_{c}$',fontsize=15)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(2.5,4.1)                 #x axis is from -25 to 25 μm
plt.ylim(4.5,7)                          #y axis is from 0 to 1
plt.xticks([2.5,3,3.5,4])   #changes labels of x axis to 2 s.f.
#           [r'$-2π$',r'$-π$',r'$0$',r'$π$',r'$2π$',]) 
plt.yticks([4.5,5,5.5,6,6.5,7,])  #changes labels of y axis to 1 d.p.
#plt.rcParams["axes.labelsize"] = 12
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper left')
plt.savefig("lnna_by_lnrm.png")  