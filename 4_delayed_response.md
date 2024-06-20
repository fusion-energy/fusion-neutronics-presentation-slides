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

  - Activation
  - Activity build up and decay
  - Emission spectra
  - Shut down dose
    <!-- - Waste -->
  <!-- - Decay heat vs time -->

</div>
<div>

  - Analysis needed to lift or cool components
  <!-- - Activated coolant -->
  - Impact of burn up on TBR
    <!-- - Shielding -->
  <!-- - Pulsed irradiation / constant irradiation -->

</div>
<div>

---

# Activation reactions


![bg 50%](images/reaction-directions.png)

---


# Build up and saturation

<div class="columns">
<div>

<span style="color:green;">

- New isotopes created during irradiation

</span>

<span style="color:orange;">

- Radioactive isotopes decay and will eventually reach a point where decay rate is equal to activation rate.

</span>

<span style="color:red;">

- Decay is more noticeable once the plasma is shutdown.

</span>

- The activity is related to the irradiation time and the nuclide half life.

</div>
<div>


![height:550px](images/activation-cooldown.png)

</div>
<div>

---

# Activation pathways

![width:800px](images/activation-directions-fe56.png)

---
# Activation products


<div class="columns">
<div>

- High energy neutron activation
![](images/isotope_chart_high_activation.png)

</div>
<div>

- Low energy neutron activation
![](images/isotope_chart_low_activation.png)

</div>
<div>

---


# Activation products from fission

- Fission of large atoms (e.g. U235)
- Results in two fission products far from stability

![bg 60%](images/isotope_chart_fission_activation.png)


---

# Emission during decay


<div class="columns">
<div>

- Characteristic gamma energies and intensities emitted
- Reduces with half life of unstable isotope
- Problematic sources in fusion Co60
- Neutrons also emitted by isotopes such as N17 found which is formed by Oxygen irradiation in water

</div>
<div>

![](images/gamma_spec2.png)

</div>
<div>

---

# Shut down dose rate

<div class="columns">
<div>

- Post irradiation gamma and even neutron emission from radioactive isotopes continues.
- Gamma and neutrons emitted cause dose field that makes human maintenance difficult.
- This causes components to generate self heating
- Reduced strength of components due to temperature, lift carefully
- Activated coolant pumped outside of the bio-shield



Image source [Eurofusion](https://scipub.euro-fusion.org/wp-content/uploads/eurofusion/WPBBPR17_17590_submitted.pdf)

</div>
<div>

![width:450](images/shutdown-dose-rate.png)

</div>
<div>

---

![bg](images/million-solid.png)

<!-- # Decay heat vs time

cooling components analysis -->

---
