# BUMPer CG Model Generator
**BUMPer**: Bottom-Up Many-body Projected Water Coarse-Grained Model

**Authors**: Jaehyeok Jin (Main Author) and Gregory A. Voth (Corresponding Author)
![BUMPer Concept Art](https://github.com/jaehyeokjin/BUMPer/blob/master/BUMPer_Schematic.png)

# Introduction
BUMPer is pairwise bottom-up CG water model that includes an effectively projected three-body interactions.
This work is based on the following two series papers. 
* **BUMPer theory**: A New Coarse-Grained Model for Water: Bottom-Up Many-body Projected Water (BUMPer). I. General Theory and Model (Submitted)
* **Temperature transferable BUMPer**: A New Coarse-Grained Model for Water: Bottom-Up Many-body Projected Water (BUMPer). II. Structural and Thermodynamic Properties (Submitted)

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
