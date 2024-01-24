import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv('df_p.csv')


p = df["p"].tolist() 
slope = df["df"].tolist() 
error = df["error"].tolist() 
#ln_p = df["ln_p"].tolist() 
#ln_df = df["ln_df"].tolist() 
#ln_error = df["ln_error"].tolist() 
#graph_info= df["graph_m_c"].tolist() 


#r=np.linspace(-3,1,1000)
#m_ = graph_info
#cplus_ = graph_info
#
#map_lnNa_ = (m_*r)+cplus_


#plt.plot(p,df,'sr',label='1$^{st}$ Cluster',markersize=6)           #points
plt.errorbar(p,slope,yerr = error,fmt ='k.',capsize=4, elinewidth=1,markersize=7,label='Mean R')


plt.show
plt.xlabel('p',fontsize=15)          #labels x axis as 'r (μm)'
plt.ylabel('d$_{f}$',fontsize=15)    #labels y axis as 'Intensity (Wm^-2)'
#plt.xlim(2.5,4.1)                 #x axis is from -25 to 25 μm
#plt.ylim(4.5,7)                          #y axis is from 0 to 1
#plt.xticks([2.5,3,3.5,4])   #changes labels of x axis to 2 s.f.
#           [r'$-2π$',r'$-π$',r'$0$',r'$π$',r'$2π$',]) 
#plt.yticks([4.5,5,5.5,6,6.5,7,])  #changes labels of y axis to 1 d.p.
#plt.rcParams["axes.labelsize"] = 12
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#plt.legend(loc='upper right')
plt.savefig("df_by_p.png")  