import openmc
import matplotlib.pyplot as plt

# we pass in a blank axis as we want to modify it afterwards
fig, ax = plt.subplots()

fig = openmc.plot_xs(
    axis=ax,
    reactions = {
        "H": ["(n,2n)"],
        "He": ["(n,2n)"],
        "Li": ["(n,2n)"],
        "Be": ["(n,2n)"],
        "B": ["(n,2n)"],
        "C": ["(n,2n)"],
        "N": ["(n,2n)"],
        "O": ["(n,2n)"],
        "F": ["(n,2n)"],
        "Ne": ["(n,2n)"],
        "Na": ["(n,2n)"],
        "Mg": ["(n,2n)"],
        "Al": ["(n,2n)"],
        "Si": ["(n,2n)"],
        "Cl": ["(n,2n)"],
        "Ar": ["(n,2n)"],
        "K": ["(n,2n)"],
        "Ca": ["(n,2n)"],
        "Sc": ["(n,2n)"],
        "Ti": ["(n,2n)"],
        "V": ["(n,2n)"],
        "Cr": ["(n,2n)"],
        "Mn": ["(n,2n)"],
        "Fe": ["(n,2n)"],
    },
    energy_axis_units='MeV'
)
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
# modify the axis afterwards to make the data clearer
ax.set_xscale('linear')
ax.set_yscale('linear')
ax.set_xlim(0, 15)  # set the x axis limits from 0 to 15MeV

plt.savefig('all_neutron_multi.png', bbox_inches='tight', dpi=400)
