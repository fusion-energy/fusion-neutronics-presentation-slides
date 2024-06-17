import openmc

material = openmc.Material(name='Li2TiO3')

material.add_element('Li', 2.0, percent_type='ao', enrichment=60.0, enrichment_target='Li6')
material.add_element('Ti', 1.0, percent_type='ao')
material.add_element('O', 3.0, percent_type='ao')
material.set_density('g/cm3', 3.43)

import matplotlib.pyplot as plt

openmc.plotter.plot_xs(
    reactions = {
        material: ['total', 'elastic', '(n,Xt)', '(n,2n)'],
    },
    energy_axis_units='MeV'
)
plt.title = 'Total cross section'
plt.savefig('macroscopic_cross_sections.png', dpi=400)