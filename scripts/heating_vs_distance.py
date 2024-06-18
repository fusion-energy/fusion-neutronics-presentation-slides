import openmc


my_material = openmc.Material()
my_material.add_element('H', 1, percent_type='ao')
my_material.add_element('O', 2, percent_type='ao')
my_material.set_density('g/cm3', 1)
my_materials=openmc.Materials([my_material])
inner_surface = openmc.Sphere(r=10000, boundary_type='vacuum')

surfaces = []
for i, r in enumerate(range(1, 5), start=1):
    surf1 = openmc.Sphere(surface_id= i, r=10000+r)
    surfaces.append(surf1)
surfaces[-1].boundary_type='vacuum'
regions = openmc.model.subdivide(surfaces)

cells = []
for i, region in enumerate(regions):
    cell = openmc.Cell(cell_id=i, region=region)
    if i != 0:
        cell.fill = my_material
    cells.append(cell)

my_geometry = openmc.Geometry(cells)

# Instantiate a Settings object
my_settings = openmc.Settings()
my_settings.batches = 10
my_settings.particles = 1000
my_settings.run_mode = 'fixed source'

# Create a DT point source
my_source = openmc.IndependentSource()
my_source.space = openmc.stats.Point((0, 0, 0))
my_source.angle = openmc.stats.Isotropic()
my_source.energy = openmc.stats.Discrete([14e6], [1])
my_settings.source = my_source

# sets up filters for the tallies
neutron_particle_filter = openmc.ParticleFilter(['neutron'])

tallies = []
for cell in cells:
    # setup the filters for the cell tally
    cell_filter = openmc.CellFilter(cell) 

    # create the tally
    cell_spectra_tally = openmc.Tally(name=f'cell_heating_{cell.id}')
    cell_spectra_tally.scores = ['flux']
    cell_spectra_tally.filters = [cell_filter, neutron_particle_filter]
    tallies.append(cell_spectra_tally)
my_tallies = openmc.Tallies(tallies)

# combine all the required parts to make a model
model = openmc.model.Model(my_geometry, my_materials, my_settings, my_tallies)

# remove old files and runs OpenMC
results_filename = model.run()

# open the results file
results = openmc.StatePoint(results_filename)

#extracts the tally values from the simulation results
tallies_results = []
for cell in cells:
    cell_tally = results.get_tally(name=f'cell_heating_{cell.id}').mean.flatten()[0]
    tallies_results.append(cell_tally)


