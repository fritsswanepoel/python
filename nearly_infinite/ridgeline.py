
import pandas as pd
import numpy as np
from sklearn.neighbors import KernelDensity

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid_spec

data = pd.read_csv("single_count.csv")
#data = pd.read_csv("char_count.csv")
max_value = data.max(numeric_only=True).max()

chars = [x for x in np.unique(data.columns)]
color = '#0000ff'

gs = grid_spec.GridSpec(len(chars),1)
fig = plt.figure(figsize=(16,9))

i = 0

ax_objs = []
for char in chars:
    x = np.array(data[char])
    x_d = np.linspace(0,1, 100)

    kde = KernelDensity(bandwidth=0.03, kernel='gaussian')
    kde.fit(x[:, None])

    logprob = kde.score_samples(x_d[:, None])

    # creating new axes object
    ax_objs.append(fig.add_subplot(gs[i:i+1, 0:]))

    # plotting the distribution
    ax_objs[-1].plot(x_d, x ,color="#f0f0f0",lw=1)
    ax_objs[-1].fill_between(x_d, x, alpha=1)


    # setting uniform x and y lims
    ax_objs[-1].set_xlim(0,1)
    ax_objs[-1].set_ylim(0,max_value)

    # make background transparent
    rect = ax_objs[-1].patch
    rect.set_alpha(0)

    # remove borders, axis ticks, and labels
    ax_objs[-1].set_yticklabels([])

    if i == len(chars)-1:
        ax_objs[-1].set_xlabel("Test Score", fontsize=16,fontweight="bold")
    else:
        ax_objs[-1].set_xticklabels([])

    spines = ["top","right","left","bottom"]
    for s in spines:
        ax_objs[-1].spines[s].set_visible(False)

    adj_char = char.replace(" ","\n")
    ax_objs[-1].text(-0.02,0,adj_char,fontweight="bold",fontsize=14,ha="right")


    i += 1

gs.update(hspace=-0.7)

#fig.text(0.07,0.85,"Distribution of Aptitude Test Results from 18 – 24 year-olds",fontsize=20)

plt.tight_layout()
plt.show()
