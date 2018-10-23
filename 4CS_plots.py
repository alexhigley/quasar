
#######################################################################
#                           4CS 2018 plots                            #
#             Learning Object Oriented plotting on python             #
#######################################################################

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


#setting up variables

qr = fits.open('/d/zit1/prog_inst/drq_testing_file.fits')[1].data
wq = np.where((qr['Z_VI'] > 0) & (qr['Z_VI'] < 5.5) & (qr['Z_CONF'] != 0))[0]
#Valid VI inspections of regular QSOs
#All quasars with 0<z<5.5
#excluded galaxies, blazars, human error and -2s.

wt = np.where(qr['Z_VI'] == -2)[0]
#where in Z_VI z = -2

maskr = np.zeros(len(qr), dtype = 'i2')
#making mask for all qr as 0s
maskr[wq] = 1
#making mask where all wq (all quasars with 0<z<5.5) is 1
maskr[wt] = 1
#making mask where all wt (all -2s) is 1
w1 = np.where(maskr == 1)[0]
#defining w1 as where in mask anything is 1
#address
vio = qr['Z_VI'][w1]
#collection of all 0<z<5.5 and -2 in Z_VI

#need to convert -2s into 'Z' correspondant.
we = qr['Z'][wt]
zar = qr['Z_VI'][wq]
wezar = np.concatenate([zar,we], axis=0)
#collection of all 0<z<5.5 in Z_VI and when -2 in Z_VI, Z
unzar = qr['Z'][w1]
#array like zar, but with the Z_PIPE z values coressponding to w1

dif = np.abs(unzar-wezar)
diff = 299792*((dif)/(1+wezar))
real_diff = dif/(1+wezar)

#now object oriented
import matplotlib
import matplotlib.ticker as ticker

#######################################################################

print('Z_VI - Z_PIPE vs Z_PIPE SCATTER PLOT:')
matplotlib.rc('text',usetex=True)
matplotlib.rc('font',size=15)
fig1,ax1 = plt.subplots(figsize=(10,8)) #for spec, 15x12
#spec class.py on brad git
    #tick params
    #ax1, fig 1

ax1.scatter(unzar,rel_diff,marker='.',color='black')
    #ax1.set_yscale('log',nonposy='clip')
#Making scatter plot of relative difference to z (VI)

ax1.set_xlabel(r'z$_{\textrm{p}}$',fontsize=25)
ax1.set_ylabel(r'$\Delta$ z',fontsize=25)
#Setting labels
#Was messed up before because need to write in latex code

ax1.tick_params(axis='both',direction='in')
ax1.tick_params(axis='both',which='minor',direction='in')
ax1.tick_params(top=True,right=True)
ax1.tick_params(which='minor',top=True,right=True)
#ticks pointing in

ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#spacing of both major and minor tickers

fig1.savefig('z_diff_scat.png',format='png')
#saving first graph as a png

fig2,ax2 = plt.subplots(figsize=(10,8))
ax2.hist(rel_diff,bins=100,histtype='stepfilled',color='slategrey')
#Making histogram of frequency vs relative diff

ax2.tick_params(axis='both',direction='in')
ax2.tick_params(axis='both',which='minor',direction='in')
ax2.tick_params(top=True,right=True)
ax2.tick_params(which='minor',top=True,right=True)
#Setting up picks, pointing in

ax2.set_xlabel(r'$\Delta$ z',fontsize=25)
ax2.set_ylabel('Frequency',fontsize=25)
#Labeling axes, again, in latex code

fig2.savefig('freq_err_hist.png',format='png')
#saving second graph as a png
