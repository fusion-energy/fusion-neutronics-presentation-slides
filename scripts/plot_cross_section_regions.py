import openmc
import matplotlib
font = {'size'   : 14}
matplotlib.rc('font', **font)

openmc.config["cross_sections"]= "/nuclear_data/cross_sections.xml"
material = openmc.Material(name='Uranium dioxide')

material.add_element('U', 1.0, percent_type='ao', enrichment=5)
material.add_element('O', 2.0, percent_type='ao')
material.set_density('g/cm3', 10.97)
print(material)
import matplotlib.pyplot as plt

openmc.plotter.plot_xs(
    reactions = {
        material: ['total', 'fission', '(n,2n)'],#, 'elastic', 'inelastic'],
    },
    energy_axis_units='MeV'
)
plt.title = 'Total cross section'

plt.savefig('cross_section_regions.png', bbox_inches='tight', dpi=300)