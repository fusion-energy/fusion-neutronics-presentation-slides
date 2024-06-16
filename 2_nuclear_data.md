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

Incident nuclei ( incident projectile, resulting fragments) resulting nuclei
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

 [Link to ENDF reaction numbers by NEA](https://www.oecd-nea.org/dbdata/data/manual-endf/endf102_MT.pdf)
 
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

## Q values

Amount of energy absorbed (-ve) or release (+ve) during the nuclear reaction

| Reaction    | Energy release (MeV) |Threshold reaction |
| -------- | ------- |------- |
| Be9(n,2n)   | -1.6   | Yes  |
| Pb208(n,2n) | -7.3   | Yes  |
| Li6(n,t)    |  4.8   | No   |
| Li7(n,nt)   | -2.4   | Yes  |

Mass and Binding energy converted to kinetic energy

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
| D + D -> He$^{3}$+n |        |
| D + D -> T + p |        |
| D + He$^{3}$->He$^{4}$+p | 18.3  *     |

* No neutron emitted

---

## Aneutronic Fusion fuels 

| Reaction  | Energy release (MeV) |
| --------- | ------- |
| D + Li$^{6}$ -> 2He$^{4}$ | 22.4       |
| P + Li$^{6}$ -> He$^{4}$ + He$^{3}$    | 4.0       |
| He$^{3}$ + Li$^{6}$ -> He$^{4}$ + p  | 16.9       |
| He$^{3}$ + He$^{3}$ -> He$^{4}$ + 2p  | 12.86       |
| p + Li$^{7}$ -> 2He$^{4}$ | 17.2       |
| p -> B$^{11}$ -> 3He$^{4}$ | 8.7        |
| p -> N$^{15}$ -> C$^{12}$ + He$^{4}$ |      5.0  |

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
- This reduces down to the neutron flux ($\phi$), nuclide number density ($N_{d}$) and microscopic cross section\sigma_{e}.
- This can be reduced one more stage by making use of the Macroscopic cross section ($\Sigma_{e}$).


$$ RR = \frac{nv\rho N_{a}\sigma_{e} }{M} = \phi N_{d} \sigma_{e} = \phi \Sigma_{e} $$

---

## Macroscopic cross section

lithium with density 
be with density and lead with density

---

## Cross section regions

Reactions often have characteristics
 resonance (resolved and unresolved)
 1/v section
 thresholds
 scattering


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

## Nucler data libraries

There are several groups that produce and distribute nuclear data

- ENDF/B-VIII.0
- TENDL 2023
- FENDL
- JEFF
- JENDL
- CENDL

Others

---