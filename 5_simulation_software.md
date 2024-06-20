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
- Monte Carlo Radiation transport
- Geometry conversion software

---

# Inventory codes

Solving the Bateman equation

| Name of software | Group / community / country | 
|  ----- | -----| 
| ACAB | UNED, Spain | 
| ALARA | Wisconsin, US | 
| Aburn | North China Electrical Power | 
| OpenMC | MIT, ANL, community | 
| Origen | LANL, US | 
| Serpent | VTT, Finland | 
| Fispact | CCFE / UKAEA | 
| Fornax | Silver Fir Software, US | 


---

# Radiation transport

Sampling the Boltzman transport equation

- Stochastic / Monte Carlo is most widely used method in fusion
- Track individual particle histories through phase space
- Random sampling of particle behavior at each event
- Accumulate contributions to the mean behavior from each history
- Variance reduction used to speed up simulation


---

# Monte Carlo Simulations

| Name of software | Group / community / country | 
|  ----- | -----| 
| FLUKA | CERN |
| GEANT | CERN |
| MCNP | LANL | 
| OpenMC | MIT, ANL and open source community |
| Serpent | VTT, Finland |
| TopMC | China |
| TRIPOLI | France |
| SCONE | Cambridge UK |
| MC DC | US |

---

# Geometry for Monte Carlo


<div class="columns">
<div>

CAD to DAGMC convertors
  - cad-to-dagmc
  - cad-to-openmc
  - stl-to-dagmc
  - stellermesh
  - Cubit

![width:190px](images/dagmc_model.png)

</div>
<div>

CAD to CSG convertors
  - GeoUned
  - McCAD
  - TopMC

![width:350px](https://upload.wikimedia.org/wikipedia/commons/8/8b/Csg_tree.png)

</div>
<div>


---


# Geometry conversion

[Link to flowchat](https://www.mermaidchart.com/raw/bfea01f7-56e6-4780-9687-0a6c99e58b74?theme=light&version=v0.1&format=svg)

![mermaid](images/cad-toneutronics-routes.png)


---

# Software distribution

Open source codes such as OpenMC and DAGMC are distributed via GitHub, conda.

Some codes used in neutronics are controlled codes under export control

Distribution in the US by RSICC and in the EU by the NEA databank.

![RSICC](images/rsicc.png)
[RSICC](http://rsicc.ornl.gov/Default.aspx)

<!-- ![RSICC](images/nea.png)
[NEA databank](https://www.oecd-nea.org/dbcps/) -->

---

# Questions

# 📧 mail@jshimwell.com
# ![width:60](images/github.png) @shimwell


---