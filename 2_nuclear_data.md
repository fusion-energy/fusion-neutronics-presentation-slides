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

- nuclear data
  - reactions
  <!-- - reactions groups like n, disappearance -->
    - periodic table, isotope chart, 3d isotope chart
    - transmutation reactions
    - Q values
    - threshold reactions
    - fusion fuels (DT,dd ect) reactions in terms of Q values
    - energy distribution from DT
  - cross sections
     - microscopic
     - exfor data
     - libraries (endf, tendl etc)
     - regions of plot
     - multigroup / continuous energy
     - group structures
     - reaction rate equation
     - macroscopic
  - scattering
    - energy angle plot
    - energy energy plot
    - pathlength
    - thermalisation
    - equation for logarithmic energy loss
  - transmutation to unstable
    - decay data
    - photons
      - energy distribution from radioactive material
  - electrons
  - other particles
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

Reactions that result in a change of the element

### Transmutation
(n,p)
(n,alpha)
Be9(n,2n)2He4
(n,fission)


###  No transmutation
(n, elastic)
(n, inelastic)
(n, heating)
(n, gamma)


---

## Q values

Amount of energy absorbed (-ve) or release (+ve) during the nuclear reaction

| Reaction    | Energy release (MeV) |Threshold reaction |
| -------- | ------- |------- |
| Be9(n,2n)  |   -1.6    |  Yes  |
| Pb208(n,2n)  |  -7.3   | Yes |
| Li6(n,t) | 4.8      |  No  |
| Li7(n,nt)    | -2.4     | Yes   |

---

## Fusion fuels


Q values of fusion fuel reactions

Plot cross sections vs energy

---

## Microscopic

Cross section vs energy

todo plot cross sections vs energy (Li6, Li7, Be9)

---

## Reaction rate equation

RR = density X 

---

## Macroscopic cross section

lithium with density 
be with density and lead with density

---

regions of plot

Reactions often have characteristics
 resonance (resolved and unresolved)
 1/v section
 thresholds
 scattering


---

## Exfor data

slide from neutronics workshop

---

## Nucler data libraries

 endf, tendl etc

---