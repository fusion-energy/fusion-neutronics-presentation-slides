import openmc
import matplotlib.pyplot as plt

# we pass in a blank axis as we want to modify it afterwards
fig, ax = plt.subplots()

fig = openmc.plotter.plot_xs(
    axis=ax,
    reactions = {
        "H": ["(n,Xt)"],
        "He": ["(n,Xt)"],
        "Li": ["(n,Xt)"],
        "Be": ["(n,Xt)"],
        "B": ["(n,Xt)"],
        "C": ["(n,Xt)"],
        "N": ["(n,Xt)"],
        "O": ["(n,Xt)"],
        "F": ["(n,Xt)"],
        "Ne": ["(n,Xt)"],
        "Na": ["(n,Xt)"],
        "Mg": ["(n,Xt)"],
        "Al": ["(n,Xt)"],
        "Si": ["(n,Xt)"],
        "Cl": ["(n,Xt)"],
        "Ar": ["(n,Xt)"],
        "K": ["(n,Xt)"],
        "Ca": ["(n,Xt)"],
        "Sc": ["(n,Xt)"],
        "Ti": ["(n,Xt)"],
        "V": ["(n,Xt)"],
        "Cr": ["(n,Xt)"],
        "Mn": ["(n,Xt)"],
        "Fe": ["(n,Xt)"],
    },
    energy_axis_units='MeV'
    
)

# modify the axis afterwards to make the data clearer
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
ax.set_xlim(0, 15)  # set the x axis limits from 0 to 15MeV

plt.savefig('all_tritium_multi.png', bbox_inches='tight', dpi=400)
