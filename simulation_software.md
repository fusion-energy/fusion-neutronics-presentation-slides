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

# Overview of neutronics simulation software

- Inventory code
- Radiation transport
  - Monte Carlo Simulation Codes
  - Deterministic Simulation Codes


---

# Inventory codes fundamental equation

Bateman equation

# Categories of Inventory codes

    - solving the matrix exponential
      - chain
      - Matrix based ODE

others?
https://www.sciencedirect.com/science/article/abs/pii/S0920379617305331
      - time-marching finite-difference method, transmutation trajectory analysis (TTA)
      - matrix
        - cram

# Inventory Code Simulations approaches

5 slides available

---

# Inventory codes

origen
fispact
ALARA
aburn 
OpenMC
Serpent

---

# Radiation transport fundamental equation

Boltzman transport equation

---

# Categories of  Radiation transport codes

- Deterministic
  - Discretize phase space
  - Solve large matrix representation of radiation transport equation
- Stochastic/Monte Carlo
  - Track individual particle histories through phase space
  - Random sampling of particle behavior at each event
  - Accumulate contributions to the mean behavior from each history
- Varience reduction generators
- Geometry conversion

---

# Monte Carlon Simulations approach

12 slides available


---

# Monte Carlon Simulations

- OpenMC
- MCNP
- TRIPOLI
- Serpent
- FLUKA
- GEANT
- TopMC

---

# Deterministic Simulation approach

13 slides available


    - solving the matrix exponential
      - chain
      - time-marching finite-difference method, transmutation trajectory analysis (TTA)
      - matrix
        - cram
    - example codes
      - alara
      - aburn https://www.sciencedirect.com/science/article/abs/pii/S0920379617305331
      - openmc
      - origen
      - etc

---

# Deterministic Simulation Codes

- PARTISN 
- OpenMOC
- ATTILA 
- Denovo 

---

# Varience reduction generators

CADIS
ADVANTG
Random Ray

---

# Geometry conversion

include mermaid diagram of geometry workflows
DAGMC
GeoUned / McCAD / TopMC (MCAM)
