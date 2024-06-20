from f4e_ace import get_energy_cross_section
import matplotlib
font = {'size'   : 14}
matplotlib.rc('font', **font)
import matplotlib.pyplot as plt


local_ace_files = {}
local_ace_files[("Li6", "TENDL-2015")] = {"path": "03Li006.ace"}
local_ace_files[("Li7", "TENDL-2015")] = {"path": "03Li006.ace"}
local_ace_files[("Be9", "TENDL-2015")] = {"path": "04Be009.ace"}


# from f4e_ace.mgxs import GROUP_STRUCTURES
# GROUP_STRUCTURES.keys()
# dict_keys(['CASMO-2', 'CASMO-4', 'CASMO-8', 'CASMO-16', 'CASMO-25', 'CASMO-40', 'VITAMIN-J-42', 'SCALE-44', 'MPACT-51', 'MPACT-60', 'MPACT-69', 'CASMO-70', 'XMAS-172', 'VITAMIN-J-175', 'SCALE-252', 'TRIPOLI-315', 'SHEM-361', 'CCFE-709', 'UKAEA-1102', 'ECCO-1968'])

energy, cross_section = get_energy_cross_section(
    this="Li6",
    types=[105],
    library="TENDL-2015",
    group_structure="VITAMIN-J-42",
    ace_filepaths=local_ace_files,
)
plt.step(energy, cross_section[0], label="Li6 total VITAMIN-J-42")
energy, cross_section = get_energy_cross_section(
    this="Li6",
    types=["total"],
    library="TENDL-2015",
    group_structure="XMAS-172",
    ace_filepaths=local_ace_files,
)


plt.title("Isotope cross section plot with group structure")
plt.step(energy, cross_section[0], label="Li6 MT=105 XMAS-172")
plt.yscale("log")
plt.xscale("log")
plt.ylabel("Microscopic cross section [b]")
plt.xlabel("Energy [eV]")
plt.legend()
plt.savefig("multi_group_isotope.png",bbox_inches='tight', dpi=300)
