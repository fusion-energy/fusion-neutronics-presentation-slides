import openmc
import openmc.data


from openmc.data import REACTION_NAME, REACTION_MT

library = openmc.data.DataLibrary.from_xml("/nuclear_data/cross_sections.xml")
for cross_section in library:
    if cross_section['type'] == 'neutron':
        path = cross_section['path']
        if cross_section['materials'][0] == 'Pb204':
            print(cross_section['materials'])
            xs = openmc.data.IncidentNeutron.from_hdf5(path)
            for reaction in xs.reactions:
                # if xs[reaction].q_value != 0.0:
                    print('    ',reaction, REACTION_NAME[reaction], xs[reaction].q_value/1e6)

def get_reaction_q_value(nuclide, reaction: int):
    library = openmc.data.DataLibrary.from_xml("/nuclear_data/cross_sections.xml")
    nuc_libary = library.get_by_material(name=nuclide, data_type='neutron')
    xs = openmc.data.IncidentNeutron.from_hdf5(nuc_libary['path'])
    if isinstance(reaction, str):
        reaction = REACTION_MT[reaction]
    print(nuclide, REACTION_NAME[reaction], xs[reaction].q_value/1e6)
    return xs[reaction].q_value

get_reaction_q_value('Li6', '(n,t)')
get_reaction_q_value('Be9', '(n,2n)')
get_reaction_q_value('Pb208', '(n,2n)') # -7.36788

# https://www.nndc.bnl.gov/qcalc/

# Reaction Products	Q-Value (keV)	Threshold (keV)
# NN means n
# Li7(n, α + n + t)	-2467.622	4		2822.762	5	
# Li6(α + t)	4783.47173	15		0	
# Be9 (2NN + 2α)	-1572.70	8		1748.90	9	
# Pb208 (207Pb + 2NN)	-7367.9	16		7403.6	16	


# Pb204 (82p, 122n) proton change -3, neutron change -4 Au197 (79p 118n)  (n,2a) this makes gold from lead
# Pb206 (82p, 124n) -3,-6 Au197 (79p 118n)
# Pb207 (82p, 125n) -3,-7 Au197 (79p 118n)
# Pb208 (82p, 126n) -3,-8 Au197 (79p 118n)

# Au197 + n