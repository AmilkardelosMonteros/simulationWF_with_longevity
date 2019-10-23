#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('xtick', labelsize=17) 
mpl.rc('ytick', labelsize=17)

def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none')
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])
    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])
def reverse_colourmap(cmap, name = 'my_cmap_r'):       
    reverse = []
    k = []   
    for key in cmap._segmentdata:    
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []
        for t in channel:                    
            data.append((1-t[0],t[2],t[1]))            
        reverse.append(sorted(data))    
    LinearL = dict(zip(k,reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL) 
    return my_cmap_r

def dibuja_puntos(arreglo):
    x = []
    y = []
    info = []
    for i in range(len(arreglo)):
        v = arreglo[i]
        x.append(v[0])
        y.append(v[1])
        info.append(1-v[2])
    fig, ax = plt.subplots()
    plt.scatter(x,y,s=500,c =info ,alpha = 2)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    adjust_spines(ax, ['left', 'bottom'])
    plt.xlabel('$ s_1 $', fontsize = 32)
    plt.ylabel('$a_1$', fontsize = 32)
    cmap = mpl.cm.jet
    cmap_r = reverse_colourmap(cmap)
    ax1 = fig.add_axes([0.91, 0.1, 0.02, 0.8])
    norm = mpl.colors.Normalize(vmin=0.1, vmax=1)
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap = cmap_r, norm=norm,orientation='vertical')
    plt.show()


dibuja_puntos(x)
