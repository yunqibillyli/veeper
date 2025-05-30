from __future__ import print_function, absolute_import, division, unicode_literals

import os
import numpy as np
import astropy.constants as const

wave=0
flux=0
sigup=0
normwave=0
normflux=0
normsig=0
fitidx=0
fitcoeff=0
fitcovmtx=0
fiterrors=0
origpars=0
origparinfo=0
filename=''
field=''
homedir=os.path.expanduser('~')
spectrum = []  # this will store the spectrum
bad_pixels = []  # this will store bad pixel indices
islocal = False


Todd = True
if Todd:
    lsf='COS_LP1'
    instr=['COS','COS','COS','COS','STIS','COS']
    gratings=['G130M','G160M','G185M','G225M','E230M','G130M']
    slits=['NA','NA','NA','NA','0.2x0.2','NA']
    lsfranges=np.array([[1100,1400],[1400,1800],[1800,2100],[2100,2278],[2278,4100],[950,1250]])
    lps=['1','1','1','1','1','2']
    cen_wave=['1327','1600','1953','2250','2707','1096']
    spectral_gaps = []

else:  # this is for the casual user
    lsf='COS_LP1'
    instr=['COS','COS']
    lsfranges=np.array([[1130,1450],[1450,1800]])
    gratings=['G130M','G160M']
    cen_wave=['1291','1611']
    slits=['NA','NA']
    lps=['2','2']
    spectral_gaps = [[0,1162.5], [1198,1201.5], [1213.3, 1217.93], [1299.3,1321.6],[1596,1612.8],[1782,2000]]

# fundamental constants
echarge = 4.803204505713468e-10 # you want this in cgs, it's staying hardcoded
m_e = const.m_e.to('g').value
c = const.c.to('cm/s').value
c2 = 29979245800.0 # not sure why this one is needed

# store LSFs and FGs
lsfs=[]
fgs=[]
wavegroups=[]
wgidxs=[]
uqwgidxs=[]

outputdir = './'

VPparoutfile = outputdir + field + '_VP.dat'
VPmodeloutfile = outputdir + field + 'VPmodel.fits'
contoutfile = outputdir + 'continua.dat'
largeVPparfile = outputdir + '_VP_log.dat'
defaultcol = 13.1
defaultb = 20.0
defaultvlim = 1000.
lowblim = 4.
upperblim = 85.
upperblim_HI = 210.

# Plotting
ylim = (-0.2, 1.4)
general_fontsize = 10.
xtick_fontsize = 'small'
ytick_fontsize = 'small'
xy_fontsize = 'small'
x_labelpad = 0
y_labelpad = 0
label_ypos = 0.2 * (ylim[0]+ylim[1])
label_fontsize = 10.
residual_markersize = 1
spec_linewidth = 1


# Handy definitions
lyseries=np.array([913.8260,914.0390,914.2860,914.5760,914.919,915.329,915.824,916.429,917.1806,918.1294,919.3514,920.9631,923.1504,926.2257,930.7483,937.8035,949.7431,972.5368,1025.7223,1215.6701])
