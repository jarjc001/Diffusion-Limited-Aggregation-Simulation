import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

df = pd.read_csv('3000read.csv')

df["Rm_mean"] = 0.0
#df["Rm_max"] = 0.0
#df["Rm_min"] = 0.0
df["Rm_sd"] = 0.0
df["ln_Na"] = 0.0
df["ln_Rm"] = 0.0
df["ln_Rm_mean"] = 0.0
df["ln_Rm_SD"] = 0.0
df["grad_Ln_n/r"]= 0.0
df["grad_Ln_n/r_mean"]= 0.0
#df["grad_Ln_n/r_sd"]= 0.0

for index, row in df.iterrows():
    
    df.at[index, 'ln_Na'] = math.log(df.Na[index])
    df.at[index, 'ln_Rm'] = math.log(df.Rm[index])

for index, row in df.iterrows():
    
    R_mean_sum = 0.0
    R_sq_mean_sum = 0.0
    
    ln_mean_sum = 0.0
    ln_sq_mean_sum = 0.0
    
    i=0.0
    a=0.0
    while i < len(df):
        if (df.Na[i] == row['Na']):
        
            R_mean_sum = R_mean_sum + df.Rm[i]
            R_sq_mean_sum = R_sq_mean_sum + df.Rm[i]**2
            
            ln_mean_sum = ln_mean_sum + df.ln_Rm[i]
            ln_sq_mean_sum = ln_sq_mean_sum + df.ln_Rm[i]**2
            
            a = a+1
            i = i+1
        else:
            i = i+1
            
    R_mean = R_mean_sum/a
    R_sd = np.sqrt((R_sq_mean_sum/a)-((R_mean_sum/a)**2))
    
    ln_mean = ln_mean_sum/a
    ln_sd = np.sqrt((ln_sq_mean_sum/a)-((ln_mean_sum/a)**2))
     

    df.at[index, 'Rm_mean'] = R_mean
    df.at[index, 'Rm_sd'] = R_sd
    
    df.at[index, 'ln_Rm_mean'] = ln_mean
    df.at[index, 'ln_Rm_SD'] = ln_sd
    

    
for index, row in df.iterrows(): #gradeint 
    
    if (df.Na[index] != 10 and df.Na[index] != 3000):
        
        ln_grad = ((df.ln_Na[index+1]-df.ln_Na[index-1])/((df.ln_Rm[index+1]-df.ln_Rm[index-1])))
        ln_grad_mean = ((df.ln_Na[index+1]-df.ln_Na[index-1])/((df.ln_Rm_mean[index+1]-df.ln_Rm_mean[index-1])))
        
        df.at[index, 'grad_Ln_n/r'] = ln_grad
        df.at[index, 'grad_Ln_n/r_mean'] = ln_grad_mean
            
    #take out those who are more than 2sd away from mean
for index, row in df.iterrows():
      if (df.ln_Rm[index] > (df.ln_Rm_mean[index] + 2*df.ln_Rm_SD[index]) or df.ln_Rm[index] < (df.ln_Rm_mean[index] - 2*df.ln_Rm_SD[index])):
        df = df.drop(labels=index, axis=0)
        
        
print(df)
df.to_csv("3000_prosseced.csv", index=True)








