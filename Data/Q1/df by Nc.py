import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv('3000_mean_plot.csv')


Na = df["Na"][1:30].tolist() 
Rm_mean = df["Rm_mean"].tolist() 
Rm_sd = df["Rm_sd"].tolist() 
ln_Na = df["ln_Na"].tolist() 

ln_Rm_mean = df["ln_Rm_mean"].tolist()  
ln_Rm_SD = df["ln_Rm_SD"].tolist()  
regression = df["regression"][1:30].tolist() 
reg_sd = df["reg_sd"][1:30].tolist()


r=np.linspace(0,3200,1000)
m_=4.42684E-06
cplus_=1.723121936
map_lnNa_ = (m_*r)+cplus_


plt.errorbar(Na,regression,yerr = reg_sd,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)       
#plt.plot(Na,regression,'ks',markersize=5)
plt.plot(r,map_lnNa_,'r--',label='Trendline',linewidth=2.5)           #line of best fit

plt.show
plt.xlabel('N$_{c}$',fontsize=15)          #labels x axis as 'r (μm)'
plt.ylabel('d$_{f}$',fontsize=15)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(0,3100)                 #x axis is from -25 to 25 μm
plt.ylim(1.6,1.79)                          #y axis is from 0 to 1
#plt.xticks([2.5,3,3.5,4])   #changes labels of x axis to 2 s.f.
#           [r'$-2π$',r'$-π$',r'$0$',r'$π$',r'$2π$',]) 
#plt.yticks([1.65,1.7,1.75,1.8])  #changes labels of y axis to 1 d.p.
plt.rcParams["axes.labelsize"] = 12
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#plt.legend(loc='lower right')
plt.savefig("df by Nc.png")  