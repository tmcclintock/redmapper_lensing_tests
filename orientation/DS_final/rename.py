import os
import numpy as np

h = 0.7
y1zs = np.loadtxt("Y1_meanz.txt")

zs = ["0.2", "0.35", "0.5", "0.65"]
ls = ["20", "30", "45", "60", "10000"]

inpath = "DeltaSigma_same_mass_redshift_distribution_z_%s_%s_lam_%s_%s.dat"
outpath = "DS_MASSSELECTION_l%d_z%d.txt"

#NOTE - I need to add two more blank columns to the output data...
for i in range(len(zs)-1):
    for j in range(len(ls)-1):
        z = y1zs[i, j+3]
        print z
        ip = inpath%(zs[i],zs[i+1],ls[j],ls[j+1])
        op = outpath%(j+3,i)
        data = np.loadtxt(ip)
        zeros = np.zeros(len(data))
        r, DS, DSe = data.T
        r *= h*(1+z)
        DS /= h*(1+z)**2 #comoving into Msun/pc^2 physical
        DSe /= h*(1+z)**2
        data = np.array([r, DS, DSe]).T
        d = np.vstack((data.T, zeros)).T
        d = np.vstack((d.T, zeros)).T
        np.savetxt(op, d)
        #os.system("cp %s %s"%(ip,op))
        
