import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv('df_p.csv')


p = df["p"].tolist() 
#df = df["slope"].tolist()  #dosent work ?
error_ = df["error"].tolist() 
ln_p = df["ln_p"].tolist() 
ln_df = df["ln_df"].tolist() 
ln_error = df["ln_error"].tolist() 
graph_info = df["graph_m_c"].tolist() 


r=np.linspace(-5,1,1000)
m_ = graph_info[0]
cplus_ = graph_info[1]

trend_ = (m_*r)+cplus_


#plt.plot(ln_p,ln_df,'sr',label='1$^{st}$ Cluster',markersize=6)           #points
plt.errorbar(ln_p,ln_df,yerr = ln_error,fmt ='k.',capsize=4, elinewidth=1,markersize=9,label='Mean R')
plt.plot(r,trend_,'r--',label='Trendline',linewidth=2)           #line of best fit

plt.show
plt.xlabel('ln p',fontsize=15)          #labels x axis as 'r (μm)'
plt.ylabel('ln d$_{f}$',fontsize=15)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(-3.1,0.1)                 #x axis is from -25 to 25 μm
plt.ylim(0.49,0.681)                          #y axis is from 0 to 1
#plt.xlim(-5,0.1)                 #x axis is from -25 to 25 μm
#plt.ylim(0.49,0.74)   
#plt.xticks([2.5,3,3.5,4])   #changes labels of x axis to 2 s.f.
#           [r'$-2π$',r'$-π$',r'$0$',r'$π$',r'$2π$',]) 
#plt.yticks([4.5,5,5.5,6,6.5,7,])  #changes labels of y axis to 1 d.p.
#plt.rcParams["axes.labelsize"] = 12
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#plt.legend(loc='upper right')
plt.savefig("lndf_by_lnp.png")  