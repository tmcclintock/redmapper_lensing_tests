raise Exception("Cannot run this script, since the chains aren't included in this repository. Email Tom for the chains.")


import numpy as np
import pandas as pd
from chainconsumer import ChainConsumer
import matplotlib.pyplot as plt

labels = [r"$\log_{10}M_{\rm 200m}$", r"$c_{\rm 200m}$", r"$\tau_{\rm mis}$", r"$f_{\rm mis}$", r"$\mathcal{A}_{m}$", r"$B_0^{\rm cl}$", r"$R_s^{\rm cl}$"]

y1zlabels = [r"$z\in[0.2;0.35)$", r"$z\in[0.35;0.5)$", r"$z\in[0.5;0.65)$"]
y1llabels = [r"$\lambda\in[5;10)$",r"$\lambda\in[10;14)$",r"$\lambda\in[14;20)$",
             r"$\lambda\in[20;30)$",r"$\lambda\in[30;45)$",r"$\lambda\in[45;60)$",
             r"$\lambda\in[60;\infty)$"]

def make_corner(zi, lj, withold=False, show=False):
    inpath = "chain_full_Y1_SAC_z%d_l%d.orientation"%(zi, lj)
    df = pd.read_table(inpath, header=None, delimiter=" ")
    chain = df.values
    #Remove some burn in
    chain = chain[32*100:]
    c = ChainConsumer()
    c.add_chain(chain, parameters=labels, name="%s %s w/ Orientation"%(y1zlabels[zi], y1llabels[lj]))


    #Add on old chain
    if withold:
        inpath = "unblinded_normal_full_chains/unblinded_chain_full_Y1_SAC_z%d_l%d.npy"%(zi, lj)
        chain = np.load(inpath)
        c.add_chain(chain, parameters=labels, name="%s %s normal Y1 model"%(y1zlabels[zi], y1llabels[lj]))

    c.configure(kde=False, legend_color_text=False, tick_font_size=10, label_font_size=24, max_ticks=4, sigmas=[0,1,2])

    fig = c.plotter.plot(legend=True)
    plt.savefig("corner_comparison_z%d_l%d.png"%(zi, lj), dpi=300)
    if show:
        plt.show()
    else:
        plt.clf()
    print chain.shape
    return

for zi in range(3):
    for lj in range(3, 7):
        make_corner(zi, lj, True)
        print("corner made for z%d l%d"%(zi, lj))
        continue
    continue
