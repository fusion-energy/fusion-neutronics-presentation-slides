---
marp: true
# theme: gaia
# theme: uncover
# _class: lead
paginate: true
backgroundColor: #fff
title: Neutronics Analysis of Fusion Systems
description: Presentation slides for the fusion energy neutronics workshop
author: Jonathan Shimwell
keywords: fusion,neutronics,neutron,photon,radiation,simulation,openmc,dagmc
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  },
  .columns3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  },
  h1 {
    text-align: center
  }
---

<style>
  :root {
    --color-background: #fff;
    --color-foreground: #333;
    --color-highlight: #f96;
    --color-dimmed: #888;
    font-family: 'Century Gothic';
    color: #3466C2
  }
  {
    font-size: 29px
  }
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
  .columns {
    display: grid;
  }
  h1 {
    justify-content: center;
  }
  section {
    justify-content: start;
  }
  img[alt~="bottom-right"] {
    position: absolute;
    top: 90%;
    right: 1%;
  }
</style>


Prompt responses

---

- prompt responses
  - neutron wall loading
  - heating
  - gamma production
  - damage
    - dpa
    - gas production
    - cascaded, recombination etc
  - tritium breeding
     -  li for t production
       - enrichment
     - be , pb for n,2n
   - dose

---

# Neutron wall loading

- Energy carried by uncollided source neutrons incident on a unit area of first wall per unit time
- Units typically used $MW m^{-2}$ 
- Useful for estimating neutronics results and scaling or comparing results
- For simple source distributions and geometry, can calculate analytically
- Complex source distributions or geometries require more sophisticated methods (e.g Monte Carlo)
![](scripts/wall-loading.png)

---

# Neutron wall example

TODO image of plasma
TODO image of tokamak
TODO plot of wall loading vs angle

- Significant poloidal variation of neutron wall loading occur in toroidal magnetic confinement fusion reactors
- Details in model behind the FW not needed for NWL calculation!

---

# Nuclear Heating

- Energy deposition calculated from the flux using “Kinetic Energy Released in MAterials” (KERMA) factors (sometimes called heating numbers in XS libs)
- Energy lost by a neutron from a collision is assumed to be deposited locally
- Gamma photons produced by neutrons are transported to determine where their energy is deposited (need coupled neutron-photon transport)
- The power density distribution is used in thermal-hydraulics calculations and subsequent structural analysis (e.g. thermal stress)
- Total heating is used for sizing cooling systems
- Nuclear energy multiplication (Mn) is ratio of energy deposited by neutrons and gamma photons in the reactor to neutron energy incident on FW

TODO making into a table
Fusion power
1GW

Neutron power
0.8GW

Heating deposited
1.1GW

Neutron multiplication
1.1

---

# Nuclear Heating depends on material and location

- At same location with same neutron flux, nuclear heating depends on material
- High-Z materials usually yield higher nuclear heating than low-Z materials
- Gamma heating represents ~85% of nuclear heating in high-Z materials and only ~40% in low-Z materials
- Nuclear heating drops rapidly as we move away from FW

TODO
plot of heating vs distance for different materials (H20, Be, Cu, steel)

---

# Detailed nuclear heating example

- Determine nuclear heating to ensure adequate cooling in components
- Nuclear heating will have localized peaks in higher Z materials (e.g. steel) that are adjacent to moderator regions (e.g. water coolant)  
  - good from an engineering perspective

TODO
plot of heating vs distance with steel and water
mesh plot of heating for geometry with water pipes

---

# Radiation Damage of Materials


- Energetic neutrons produce: 
  - interstitials and vacancies (atomic displacement)
  - transmutations (gaseous and metallic)
- Determined using neutron flux with appropriate reaction cross sections
- Evaluation of effects of radiation damage on mechanical and physical properties is a crucial aspect of development of structural materials for fusion 
- Damage parameters greatly influenced by neutron energy spectrum

TODO DPA vs energy plot of Iron
TODO helium production plot in Iron

---

# He/dpa Ratio For Structural Materials

SiC has an order of magnitude higher He/dpa than steel at the FW
He/dpa for V at the FW is lower with modest gradient
SS316 has enhanced He production deep in blanket
Due to 10 wppm B in SS316 along with large Ni content

TODO plot graph of dpa vs depth
TODO plot graph of he production vs depth
TODO plot ratio of dpa to He production
TODO these different materials SiC, steel, Vandium alloy, eurofer

# Instantaneous Dose

Different types of dose, absorbed, equivalent and effective.
Effective dose is typically used for dose maps.
Dose coefficients units of $Sv.cm^2$
neutron flux ($particles.cm{^-2}s^{-1}$)
resulting dose in Sv per second

TODO plot dose maps for different directions
TODO plot dose maps for different libraries
TODO plot dose maps for different particles (photons and neutrons)