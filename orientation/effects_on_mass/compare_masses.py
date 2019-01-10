import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc("errorbar", capsize=3)
plt.rc("text", usetex=True)
plt.rc("font", size=14, family="serif")

#Load lams and zs and cutoff low bins
lams = np.loadtxt("Y1_meanl.txt")[:, 3:]
zs = np.loadtxt("Y1_meanz.txt")[:, 3:]

def make_unblind_uncalibrated_Y1means():
    Mmeans = np.zeros((3, 4))
    Muncs = np.zeros((3, 4))
    for zi in range(3):
        for lj in range(4):
            inpath = "unblinded_normal_full_chains/unblinded_chain_full_Y1_SAC_z%d_l%d.npy"%(zi, lj+3)
            chain = np.load(inpath)
            log10M = chain[:, 0]
            M = 10**log10M
            Mmeans[zi, lj] = np.mean(M)
            Muncs[zi, lj] = np.std(M)
            continue
        continue
    np.savetxt("Mmean_Y1fiducial.txt", Mmeans, header="Msun/h")
    np.savetxt("Munc_Y1fiducial.txt", Muncs, header="Msun/h")
    return

def make_means():
    Mmeans = np.zeros((3, 4))
    Muncs = np.zeros((3, 4))
    for zi in range(3):
        for lj in range(4):
            inpath = "chain_full_Y1_SAC_z%d_l%d.orientation"%(zi, lj+3)
            df = pd.read_table(inpath, header=None, delimiter=" ")
            chain = df.values
            #Remove some burn in
            chain = chain[32*100:]
            log10M = chain[:, 0]
            M = 10**log10M
            Mmeans[zi, lj] = np.mean(M)
            Muncs[zi, lj] = np.std(M)
            continue
        continue
    np.savetxt("Mmean_orientation.txt", Mmeans, header="Msun/h")
    np.savetxt("Munc_orientation.txt", Muncs, header="Msun/h")
    return

#make_unblind_uncalibrated_Y1means()
#make_means()

def plot_means():
    Mmnew = np.loadtxt("Mmean_orientation.txt")
    Muncnew = np.loadtxt("Munc_orientation.txt")
    Mmy1 = np.loadtxt("Mmean_Y1fiducial.txt")
    Muncy1 = np.loadtxt("Munc_Y1fiducial.txt")
    
    ratio = Mmnew / Mmy1
    ratio_err = np.sqrt(Muncnew**2/Mmy1**2 + Muncy1**2 * Mmnew**2 / Mmy1**4)

    labs = ["low", "mid", "high"]
    for zi in range(3):
        plt.errorbar(lams[zi], ratio[zi], ratio_err[zi], marker='.', ls='',
                     label="%s-z"%labs[zi])
    plt.xlabel("richness")
    plt.ylabel(r"$M_{\mu}/M_{\rm Y1\ fiducial}$")
    plt.legend(frameon=False)
    plt.axhline(1, c='k', ls='--')
    plt.savefig("mass_changes.png", dpi=300, bbox_inches="tight")
    plt.show()
    return
plot_means()
