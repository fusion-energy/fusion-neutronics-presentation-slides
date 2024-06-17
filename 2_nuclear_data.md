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



# Nuclear data

<div class="columns"  style="font-size: 30px;">
<div>

  - reactions
  - Isotope chart
  - transmutation reactions
  - Q values
  - threshold reactions
  - fusion fuels (DT,DD ...)
  - energy distribution from DT
  - microscopic cross sections
  - experimental data
  - libraries (ENDF, TENDL, FENDL ...)
</div>
<div>

  - cross section regions
  - multigroup / continuous energy
  - group structures
  - reaction rate equation
  - macroscopic cross sections
  - scattering / thermalisation
  - decay data
  - photons
  - energy distribution from radioactive material

  <!-- - energy angle plot
  - energy energy plot
  - pathlength
  - equation for logarithmic energy loss
  - transmutation to unstable -->
  <!-- - electrons
  - other particles -->

</div>
<div>

---

# Reactions

Nuclear reactions notation

Target nuclei (incident projectile, resulting fragments) resulting nuclei
<html>
  <body>
    <svg height="250" width="100%" xmlns="http://www.w3.org/2000/svg">
      <text x="40%" y="50" fill="red" font-size="35">Be9(n,2n)2He4</text>
      <line x1="40%" y1="60" x2="20%" y2="200" style="stroke:red;stroke-width:2" />
      <line x1="47%" y1="60" x2="40%" y2="200" style="stroke:red;stroke-width:2" />
      <line x1="50%" y1="60" x2="66%" y2="200" style="stroke:red;stroke-width:2" />
      <line x1="60%" y1="60" x2="85%" y2="200" style="stroke:red;stroke-width:2" />
      <text x="15%" y="230" fill="red" font-size="35">Target</text>
      <text x="35%" y="230" fill="red" font-size="35">Projectile</text>
      <text x="60%" y="230" fill="red" font-size="35">Product</text>
      <text x="80%" y="230" fill="red" font-size="35">Product</text>
    </svg> 
  </body>
</html>

---

## Neutron induced reactions

 - 999 reactions channels with unique reaction IDs (MT numbers)
 - MT 3 is elastic scattering (n,'n)
 - MT 16 is neutron multiplication (n,2n)
 - MT 18 is neutron multiplication (n,f)
 - MT 205 is tritium production (n,Xt) where X is a wild card
 - MT 444 is damage energy

 [🔗 ENDF reaction numbers](https://www.oecd-nea.org/dbdata/data/manual-endf/endf102_MT.pdf)
 
 ---

## Transmutation reactions

Reactions that result in a change of the isotope

<div class="columns3"  style="font-size: 30px;">
<div>

###  No transmutation
(n, elastic)
(n, inelastic)
(n, heating)

</div>
<div>

### Element transmutation
(n,p)
(n,alpha)
(n,fission)
Be9(n,2n)2He4


</div>
<div>

### Isotope transmutation

(n, gamma)
Pb208(n,2n)Pb207

</div>
<div>


---

## Transmutation of lead to gold

<div class="columns"  style="font-size: 30px;">
<div>

![gold to lead](images/gold-lead-isotope-chart2.png)

[Image source IAEA](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html)


</div>
<div>

- 1 stable isotope of gold Au$_{79}^{197}$
- 3 natural isotopes of lead
  - Pb$_{82}^{204}$ ⚛ -3 protons, -4 neutrons
  - Pb$_{82}^{206}$ ⚛ -3 protons, -6 neutrons
  - Pb$_{82}^{207}$ ⚛ -3 protons, -7 neutrons 
  - Pb$_{82}^{208}$ ⚛ -3 protons, -8 neutrons
- 2 reactions for converting gold to lead
  - Pb204 (n,3npa) Au197
  - Pb204 (n,nta) Au197
- No cross section data found in ENDF
</div>
<div>


---

## Q values

Amount of energy absorbed (-ve) or release (+ve) during the nuclear reaction

| Reaction    | Energy release [MeV] |Threshold reaction |
| -------- | ------- |------- |
| Be9(n,2n)   | -1.6   | Yes  |
| Pb208(n,2n) | -7.3   | Yes  |
| Li6(n,t)    |  4.8   | No   |
| Li7(n,nt)   | -2.4   | Yes  |

Mass and Binding energy converted to kinetic energy

Online Q value calculator at [NNDC](https://www.nndc.bnl.gov/qcalc/)

---

## Fusion fuels

<div class="columns"  style="font-size: 30px;">
<div>

![](images/fusion-cross-sections.png)

</div>
<div>


Q values of fusion fuel reactions

| Reaction  | Energy release (MeV) |
| --------- | ------- |
| D + T -> He$^{4}$ + n  |  17.6      |
| D + D -> He$^{3}$+n |   3.3     |
| D + D -> T + p |   4.0     |
| D + He$^{3}$->He$^{4}$+p | 18.3  *     |

* No neutron emitted

---

## Aneutronic Fusion fuels 

<div class="columns"  style="font-size: 30px;">
<div>

- Neutrons are not emitted in the primary fuel reaction
- Neutrons can be emitted by reactions with the products
- Energy capture via direct conversion or divertor?

</div>
<div>

| Reaction  | Energy release <br> [MeV] |
| --------- | ------- |
| D + Li$^{6}$ -> 2He$^{4}$ | 22.4       |
| P + Li$^{6}$ -> He$^{4}$ + He$^{3}$    | 4.0       |
| He$^{3}$ + Li$^{6}$ -> He$^{4}$ + p  | 16.9       |
| He$^{3}$ + He$^{3}$ -> He$^{4}$ + 2p  | 12.86       |
| p + Li$^{7}$ -> 2He$^{4}$ | 17.2       |
| p -> B$^{11}$ -> 3He$^{4}$ | 8.7        |
| p -> N$^{15}$ -> C$^{12}$ + He$^{4}$ |      5.0  |

</div>
<div>

---

## Microscopic Cross Section

<div class="columns"  style="font-size: 30px;">
<div>

- Measured in Barns (1 barn = $10^{-28}m^{2}$)
- Energy dependant
- Cross section evaluations exist for:
  - different incident particles
  - different nuclides
  - different interactions.
- Important neutron reactions plotted
  - Tritium breeding
  - Neutron multiplication

</div>
<div>

![](images/important-microscopic-cross-sections.png)

</div>
<div>

---

## Reaction rate equation


- The reaction rate ($RR$) can be found by knowing the number of neutrons per unit volume ($n$), the velocity of neutrons ($v$), the material density ($p$), Avogadro's number ($N_{a}$), the microscopic cross section at the neutron energy ($\sigma_{e}$) and the atomic weight of the material ($M$).
- This reduces down to the neutron flux ($\phi$), nuclide number density ($N_{d}$) and microscopic cross section $\sigma_{e}$.
- This can be reduced one more stage by making use of the Macroscopic cross section ($\Sigma_{e}$).


$$ RR = \frac{nv\rho N_{a}\sigma_{e} }{M} = \phi N_{d} \sigma_{e} = \phi \Sigma_{e} $$

---

## Macroscopic cross section


<div class="columns"  style="font-size: 30px;">
<div>

- Lithium metatitanate has a material density of 3.4 g/cm3
- When plotting materials the Macroscopic cross section accounts for number density of the different isotopes
- Units for Macroscopic cross section are cm$^{-1}$

</div>
<div>

![](images/macroscopic_cross_sections.png)

</div>
<div>

---

## Cross section regions

<div class="columns"  style="font-size: 30px;">
<div>

Reactions have characteristics
- resolved resonance
- unresolved resonance
- 1/v section
- thresholds
- scattering

</div>
<div>

![](images/cross_section_regions.png)

</div>
<div>

---

# Experimental data

<div class="columns"  style="font-size: 30px;">
<div>

Availability of experimental data varies for different reactions and different isotopes.

Typically the experimental data is then interpreted to create evaluation libraries, such as ENDF, JEFF, JENDL, CENDL.



</div>
<div>

[![](images/exfor_be_n_2n.png)](https://nds.iaea.org/dataexplorer/)

Source [IAEA nuclear data services](https://nds.iaea.org/dataexplorer/?target_elem=Au&target_mass=197&reaction=n%2Cg)

</div>
<div>

---

## Nuclear data libraries

There are several groups that produce and distribute nuclear data

- TENDL 2023 🇪🇺
- ENDF/B-VIII.0 🇺🇸
- FENDL 3.2b 🌐
- JEFF 3.3 🇪🇺
- JENDL 5 🇯🇵
- CENDL 3.2 🇨🇳
- BROND 3.1 🇷🇺

---