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

- Inventory codes
- Radiation transport
  - Monte Carlo Simulation Codes
  - Deterministic Simulation Codes
- Geometry conversion software

---

# Inventory codes fundamental equation

Bateman equation

Loss terms

Production terms
$\lambda$
---

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

| Name of software | Group / community / country | 
|  ----- | -----| 
| ACAB | UNED, Spain | 
| ALARA | Wisconsin, US | 
| Aburn | North China Electrical Power | 
| OpenMC | MIT, ANL and open source community | 
| Origen | LANL, US | 
| Serpent | VTT, Finland | 
| Fispact | CCFE / UKAEA | 
| Fornax | Silver Fir Software, US | 

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

---

# Monte Carlo Simulations approach

12 slides available


---

# Monte Carlo Simulations

| Name of software | Group / community / country | 
|  ----- | -----| 
| FLUKA | CERN |
| GEANT | CERN |
| MCNP | LANL | 
| OpenMC | MIT, ANL and open source community
| Serpent | VTT, Finland
| TopMC | China
| TRIPOLI | France

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

| Name of software | Group / community / country | 
|  ----- | -----| 
- ATTILA 
- Denovo 
- OpenMOC
- PARTISN 

---

# Variance reduction generators

| Name of software | Group / community / country | 
|  ----- | -----| 
| ADVANTG
| CADIS
| Magic method
| Random Ray

---

# Geometry conversion

Include mermaid diagram of geometry workflows

CAD to DAGMC convertors
  - cad-to-dagmc
  - cad-to-openmc
  - stellermesh
  - Cubit

CAD to CSG convertors
  - GeoUned
  - McCAD
  - TopMC


# Shut down dose rate

Inventory simulations
Transport simulation
      - r2s
      - d1s
Pyne, Silverfir
  
---


Software distirbution

Some codes used in neutronics are controlled codes under export control

Distribution in the US by RSICC and in the EU by the NEA databank.

[RSICC](http://rsicc.ornl.gov/Default.aspx)

[NEA databank](https://www.oecd-nea.org/dbcps/)