"""
Call CLASS and make the power spectrum files.
"""
import sys
import numpy as np
from classy import Class

#Get the mean redshifts
meanz = 0.577 #SPT mean redshift#np.loadtxt("../Y1_meanz.txt")

#Assume cosmology
Ob = 0.05
Om = 0.3
Ocdm = Om - Ob
h = 0.7
params = {
        'output': 'mPk',
        "h":h,
        "A_s":1.9735e-9, #Yields sigma8 = 0.8
        "n_s":0.96,
        "Omega_b":Ob,
        "Omega_cdm":Ocdm,
        'YHe':0.24755048455476272,#By hand, default value
        'P_k_max_h/Mpc':3000.,
        'z_max_pk':1.0,
        'non linear':'halofit'}

cosmo = Class()
cosmo.set(params)
cosmo.compute()
print "sigma8 is:", cosmo.sigma8()

k = np.logspace(-5, 3, base=10, num=4000) #1/Mpc, apparently
np.savetxt("k.txt", k/h) #h/Mpc now
"""for i in range(len(meanz)):
    for j in range(len(meanz[i])):
        z = meanz[i,j]
        Pmm  = np.array([cosmo.pk(ki, z) for ki in k]) 
        Plin = np.array([cosmo.pk_lin(ki, z) for ki in k]) 
        np.savetxt("pnl_z%d_l%d.txt"%(i,j), Pmm*h**3) #Mpc^3/h^3
        np.savetxt("plin_z%d_l%d.txt"%(i,j), Plin*h**3) #Mpc^3/h^3
    print "Done with z%d"%i
"""
for z in [0.577]:
    Pmm = np.array([cosmo.pk(ki, z) for ki in k])
    Plin = np.array([cosmo.pk_lin(ki, z) for ki in k])
    np.savetxt("pnl_z%.2f.txt"%(z), Pmm*h**3) #Mpc^3/h^3
    np.savetxt("plin_z%.2f.txt"%(z), Plin*h**3) #Mpc^3/h^3
    print "done"
