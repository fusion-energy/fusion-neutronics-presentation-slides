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


Delayed responses

---

- delayed response
  - activation
  - activity vs time (shark fin)
  - emission spectra
    - shut down dose
    - waste
  - decay heat vs time
    - analysis needed to lift or cool components
  - activated coolant
  - impact of burn up
    - TBR
    - shielding
  - pulsed irradiation / constant irradiation

---

# Activation of materials

Neutron induced reactions lead to unstable radioactive products.

<!-- slide from neutronics workshop isotope chart with arrows -->

# Build up, saturation and decay

<!-- slide from neutronics workshop shark fin -->

# Emission during decay

<!-- plot gamma emission spectra as a function of time -->

# Shut down dose rate

heating effect on components
resulting in reduced strength during lifts

# Decay heat vs time

cooling components analysis

# Activated coolant


# Burn up

# Pulsed irradiation and steady state