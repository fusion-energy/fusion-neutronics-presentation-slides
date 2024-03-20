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
 - reactions
    - transmutation
    - Q values
    - thresholds
    - Fusion fuels

- nuclear data
  - reactions
    - isotope chart
    - transmutation reactions
    - Q values
    - reaction rate equation
  - cross sections
     - microscopic
     - macroscopic
     - exfor data
     - how cross sections are measured
     - regions of plot
     - multigroup / continuous energy
     - group strucutres
     - libraries (endf, tendl etc)
  - scattering
    -  energy angle plot
    - energy energy plot
    - equation for logarithmic energy loss
    - pathlength
    - thermailisation
  - transmutation
  - neutrons
    - energy distribution from DT
  - photons
    - energy distribution from radioactive material
  - electrons
  - other particles
---

# Reactions

## Neutron induced reactions
 - Over 800 reactions channels with unique reaction IDs (MT numbers)
 - MT 16 is neutron multiplication (n,2n)
 - MT 205 is tritium production multiplication (n,2n)
 - MT 444 is damage energy
 
 ### Be9(n,2n)2He4

---