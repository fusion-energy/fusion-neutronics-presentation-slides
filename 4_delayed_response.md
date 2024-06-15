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



---


# Delayed response


<div class="columns"  style="font-size: 30px;">
<div>

  - activation
  - activity build up and decay (shark fin)
  - emission spectra
    - shut down dose
    - waste
  - decay heat vs time

</div>
<div>

  - analysis needed to lift or cool components
  - activated coolant
  - impact of burn up
    - TBR
    - shielding
  - pulsed irradiation / constant irradiation

</div>
<div>

---

# Activation of materials

Neutron induced reactions lead to unstable radioactive products.

<h1>https://www.w3schools.com/graphics/svg_line.asp</h1>
<html>
<body>

<div style="width: 100%; text-align: center">
  <rect width="100" height="100" x="0" y="0" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="100" y="0" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="200" y="0" stroke="darkblue" stroke-width="4" fill="lightgrey" />

  <rect width="100" height="100" x="0" y="100" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="100" y="100" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="200" y="100" stroke="darkblue" stroke-width="4" fill="lightgrey" />

  <rect width="100" height="100" x="0" y="200" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="100" y="200" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  <rect width="100" height="100" x="200" y="200" stroke="darkblue" stroke-width="4" fill="lightgrey" />
  
  <text x="5" y="15" fill="red">I love SVG!</text>

 <line x1="50" y1="50" x2="150" y2="150" style="stroke:red;stroke-width:2" />
  <line x1="150" y1="50" x2="150" y2="150" style="stroke:red;stroke-width:2" />
 <line x1="250" y1="50" x2="150" y2="150" style="stroke:red;stroke-width:2" />

 
 <line x1="50" y1="150" x2="150" y2="150" style="stroke:red;stroke-width:2" />
 <line x1="50" y1="250" x2="150" y2="150" style="stroke:red;stroke-width:2" />

  <line x1="250" y1="150" x2="150" y2="150" style="stroke:red;stroke-width:2" />
 <line x1="250" y1="250" x2="150" y2="150" style="stroke:red;stroke-width:2" />
 <line x1="150" y1="250" x2="150" y2="150" style="stroke:red;stroke-width:2" />

</div>
 
</body>
</html>

<!-- slide from neutronics workshop isotope chart with arrows -->

---

# Build up, saturation and decay

<!-- slide from neutronics workshop shark fin -->

---

# Emission during decay

<!-- plot gamma emission spectra as a function of time -->

---

# Shut down dose rate

heating effect on components
resulting in reduced strength during lifts

---

# Decay heat vs time

cooling components analysis

---

# Activated coolant

---

# Burn up

---

# Pulsed irradiation and steady state

---