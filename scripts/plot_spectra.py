#TODO convert to lethargy plot

import numpy as np
import matplotlib.pyplot as plt

# other files for first wall
# "616_WCCB-FW.txt",
# "616_WCLL-FW.txt",
# "616_HCPB-FW.txt",
# "616_HCLL-FW.txt"

files = [
  ("616_HCLL-VV.txt",'Helium cooled lithium lead'),
  ("616_WCCB-VV.txt",'Water cooled ceramic breeder'),
  ("616_WCLL-VV.txt",'Water cooled lithium lead'),
  ("616_HCPB-VV.txt",'Helium cooled pebble bed')
]

for file, name in files:
    energy = np.loadtxt(file, max_rows=616)/1e6 # removing one to get correct length
    values = np.loadtxt(file, skiprows=617, max_rows=616 )
    plt.plot(energy, values, label=name)

plt.yscale('log')
plt.xscale('log')
plt.xlabel('Energy [MeV]')
plt.ylabel('Neutron flux [arbitrary units]')
plt.savefig('blanket_spectra.png')
plt.legend()
plt.savefig('blanket_spectra_legend.png')