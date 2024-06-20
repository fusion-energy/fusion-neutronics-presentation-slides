# This example plots the exiting neutron energy distribution for different incident neutron energies.

import openmc
import matplotlib.pyplot as plt
from pprint import pprint
import matplotlib
font = {'size'   : 14}
matplotlib.rc('font', **font)
import matplotlib.pyplot as plt

# change this path to point to your nuclide of choice
nuc_path = "/nuclear_data/neutron/Be9.h5"

beryllium = openmc.data.IncidentNeutron.from_hdf5(nuc_path)

# prints all the nuclear reactions available, MT numbers
print('\n All the reactions available')
pprint(list(beryllium.reactions.values()))

# selects the neuron multiplication cross section (MT number 16) 
beryllium_elastic = beryllium[16]

# prints out the products of the reaction
print('\n Products of the elastic reaction', beryllium_elastic.products)

neutron_out = beryllium_elastic.products[0]

distribution = neutron_out.distribution[0]

incident_neutron_energy = distribution.energy
outgoing_neutron_energy = distribution.energy_out

fig, ax = plt.subplots()

# # This loops through the incident neutron energies and outgoing neutron energies
# # This loop also uses some python list slicing syntax
# # As there are a lot of data points for lots of energies we are plotting every 4th neutron energy with [::4] part
for incident_energy, outgoing_energy in zip(incident_neutron_energy[::5], outgoing_neutron_energy[::5]):
    ax.semilogy(outgoing_energy.x/1e6, outgoing_energy.p, label=f"incident neutron energy={incident_energy/1e6}MeV")


plt.xlabel("Outgoing energy [MeV]")
plt.ylabel("Probability/eV")
plt.title("Neutron energy distribution of Be9(n,2n) reactions")
plt.legend()
plt.savefig("angle_energy_be9.png", bbox_inches="tight", dpi=300)
print('written angle_energy_be9.png')