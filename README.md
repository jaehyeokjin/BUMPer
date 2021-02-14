# BUMPer CG Model Generator
**BUMPer**: Bottom-Up Many-body Projected Water Coarse-Grained Model

**Authors**: Jaehyeok Jin (Main Author) and Gregory A. Voth (Corresponding Author)
![BUMPer Concept Art](https://github.com/jaehyeokjin/BUMPer/blob/master/BUMPer_Schematic.png)

# Introduction and Citation
BUMPer is pairwise bottom-up CG water model that includes an effectively projected three-body interactions.
This work is based on the following two-series papers. Please refer to them for more detail. Also, if you use BUMPer in your publications, please cite the following references.

(1) **BUMPer theory**
> Jaehyeok Jin, Yining Han, Alexander J. Pak, Gregory A. Voth, "A new one-site coarse-grained model for water: Bottom-up many-body projected water (BUMPer). I. General theory and model," _Journal of Chemical Physics_, **154**, 044104 (2021).

[![DOI](https://img.shields.io/badge/J.Chem.Phys.-10.1063/5.0026651-FA8072.svg)](https://doi.org/10.1063/5.0026651)

(2) **Temperature transferable BUMPer**
> Jaehyeok Jin, Yining Han, Alexander J. Pak, Gregory A. Voth, "A new one-site coarse-grained model for water: Bottom-up many-body projected water (BUMPer). II. Temperature transferability and structural properties at low temperature," _Journal of Chemical Physics_, **154**, 044105 (2021).

[![DOI](https://img.shields.io/badge/J.Chem.Phys.-10.1063/5.0026652-FA8072.svg)](https://doi.org/10.1063/5.0026652)

This Github page will provide the BUMPer CG models at different temperatures (as an input)

# Usage
The current code simply generates the effective CG interactions at the given temperatures. The files are pre-generated from BUMPer interactions at different temperatures under constant volume conditions. For technical discussions, please refer to References.

Clone the repository:
<pre><code>git clone git://github.com/jaehyeokjin/BUMPer</pre></code>

No further make/setup is required. Simply run:
<pre><code>python bumper.py [FF type] [Temperatures]</pre></code>

Results will be generated under ./results folder.

**FF type**: (type exactly) SPCE, SPCFw, TIP4P2005, TIP4PIce

**Temperatures**: any temperatures in liquid range (280-360 K) can be interpolated

**Usage**: The generated BUMPer FF is compatible with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) MD engine.

_Note that the force fields provided here are obtained from the equilibrium volume at 300 K, 1 atm._

**Any questions?** Feel free to send email to: _jhjin@uchicago.edu_ (Jaehyeok Jin)
