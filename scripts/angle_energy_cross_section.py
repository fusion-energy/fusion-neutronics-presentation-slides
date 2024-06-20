# This example plots the probability of scattering angle for different incident neutron energies.

import openmc
import matplotlib.pyplot as plt
from pprint import pprint
import matplotlib
font = {'size'   : 14}
matplotlib.rc('font', **font)
import matplotlib.pyplot as plt

# change this path to point to your nuclide of choice
nuc_path = "/nuclear_data/neutron/C12.h5"

gold = openmc.data.IncidentNeutron.from_hdf5(nuc_path)

# prints all the nuclear reaactions avaialble, MT numbers
print('\n All the reactions available')
pprint(list(gold.reactions.values()))

# selects the elastic cross section (MT number 2) 
gold_elastic = gold[2]

# prints out the products of the reaction
print('\n Products of the elastic reaction', gold_elastic.products)

neutron_out = gold_elastic.products[0]

distribution = neutron_out.distribution[0]

neutron_energy = distribution.angle.energy

fig, ax = plt.subplots()

# This loops through the incident neutron energies and the angular distributions
# This loop also uses some python list slicing syntax
# As the nuclear data goes to high energies (150MeV) we skip the last 15 entries of the list with the [:-15] part
# As there are a lot of data points for lots of energies we are plotting every 100th neutron energy with [:::50] part
# mu is the cosine of the scattering angle
for energy, angle in zip(distribution.angle.energy[:-15][::100], distribution.angle.mu[:-15][::100]):
    ax.plot(angle.x, angle.p, label=f"neutron energy={energy/1e6}MeV")


plt.xlabel("Cosine of scattering angle")
plt.ylabel("Probability")
plt.title("Neutron energy angle distribution of C12")
plt.legend()
plt.savefig("angle_energy_cross_section.png", bbox_inches="tight", dpi=300)
print('written angle_energy_cross_section.png')