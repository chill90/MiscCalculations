#!/usr/local/bin/python

import numpy                    as np
from   matplotlib import pyplot as plt
import matplotlib.colors        as cl
import scipy.constants          as const

#Bose occupation number
#'temp' = temperature of thermal source
#'freq' = observation/emission frequency of detector/thermal source
def n(temp, freq):
    h  = 6.62e-34
    kB = 1.38e-23
    return 1./(np.exp((h*freq)/(kB*temp)) - 1)

# (1) Make plots of occupation number vs frequency for various temperatures
temps = np.array([2.725, 4., 10., 30.])
freqs = np.linspace(1e9, 1000e9, 1000)

plt.figure(0)
for temp in temps:
    plt.plot(freqs*1e-9, n(temp, freqs), label=str(temp))
#plt.title("Bose Occupation Number")
plt.xlabel("Frequency [GHz]")
plt.ylabel("Occupation Number")
plt.xscale('log')
plt.yscale('log')
plt.legend(title="Temperatures", loc="best")
plt.savefig("PDF/OccPlots_multiCurve.pdf")

# (2) Make plots of occupation number vs frequency as a contour plot
temps = np.linspace(1., 50., 1000)
x, y = np.meshgrid(temps, freqs)
z = n(x, y)
levels = np.logspace(np.amin(z), np.amax(z), 1000)
ticks  = np.logspace(np.amin(z), np.amax(z), 5   )
plt.figure(1)
p = plt.contourf(x, y*1.e-9, z, levels=levels, norm=cl.LogNorm())
#plt.title("Bose Occupation Number")
plt.xlabel("Frequency [GHz]")
plt.ylabel("Source Temperature [K]")
plt.colorbar(p, ticks=ticks)
plt.savefig("PDF/OccPlots_contour.pdf")
