import openmc
import openmc.data


from openmc.data import REACTION_NAME, REACTION_MT, DADZ 

library = openmc.data.DataLibrary.from_xml("/nuclear_data/cross_sections.xml")

# Pb204 (82p, 122n) proton change -3, neutron change -4 Au197 (79p 118n)  (n,2a) this makes gold from lead
# Pb206 (82p, 124n) -3,-6 Au197 (79p 118n)
# Pb207 (82p, 125n) -3,-7 Au197 (79p 118n)
# Pb208 (82p, 126n) -3,-8 Au197 (79p 118n)

for lead_isotope in ['Pb204', 'Pb206', 'Pb207', 'Pb208']:


    entry = library.get_by_material(lead_isotope)
    path = entry['path']
    xs = openmc.data.IncidentNeutron.from_hdf5(path)

    # for reaction in xs.reactions:
    #     print('    ',reaction, REACTION_NAME[reaction], xs[reaction].q_value/1e6)

    delta_z_required = openmc.data.zam('Au197')[0]-openmc.data.zam(lead_isotope)[0]
    delta_a_required = openmc.data.zam('Au197')[1]-openmc.data.zam(lead_isotope)[1]

    print(f'DADZ required to get {lead_isotope} to Au197: DA={delta_a_required}, DZ={delta_z_required}')

    for k,v in DADZ.items():
        # print(v, DADZ_required[lead_isotope])
        if v == (delta_a_required, delta_z_required):#DADZ_required[lead_isotope]:
            mt=REACTION_MT[k]
            print(f'  reaction {mt} found that gets {lead_isotope} {k} Au197')
            if mt in xs.reactions.keys():
                print('      found reaction in cross section library')
                route = xs[mt]

# these two options are identified but no reaction data found in endf
# Pb204(n,3npa)Au197
# Pb204(n,nta)Au197
