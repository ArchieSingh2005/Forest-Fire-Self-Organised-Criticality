# Forest-Fire-Self-Organised-Criticality
Simulation of Forest Fire Model demonstrating self-organised criticality, avalanche dynamics and power law behaviour.

This project simulates the Forest Fire Model to study Self Organised Criticality (SOC) a concept from complexity science where a system 
naturally evolves to a critical state without any external tuning.
The model is inspired by real forest fire observations, particularly the 1988 Yellowstone fire, where long periso of forest growth were followed by a sudden, massive, system wide fire. The model shows that such catastrophic events are not anomalies, on the contrary they are an inevitable consequence of how the system organizes itself.

What is Self-Organized Criticality ?

In a self organised critical system , small events happen very frequently and large events happen rarely but always remain possible. There is no characteristic event size i.e., the system is scale free.
The frequency of events follows a power law: P(s) ~ s^(−τ).
This project demonstrates all of these properties using a simple gris- based simulation

How the Model Works ?

The forest is represented as a 2D grid where each cell is either empty (0) or occupied by a tree (1).
At each time step, a tree grows at a random location on the grid. After every 40 growth events, a fire is triggered at a random tree.
The fire spreads to all connected neighboring trees (up, down, left, right)
All burned trees become empty and the number of trees burned in one fire = avalanche size
This cycle repeats hundreds of thousands of times. The system self-organizes into a state where fires of all sizes occur naturally.

Key Concepts :

Noise - Random tree growth and random fire ignition

Avalanche - Total number of trees burned in one fire event

Connectivity - How many trees are connected, this determines the fire size

Power Law - Small fires frequent, large fires rare but possible

SOC - System reaches critical state automatically, no tuning needed

Results :

The avalanche size distribution follows a power law:

P(s) ~ s^(−τ)
The critical exponent was estimated as τ ≈ 1.3 – 1.6, consistent with the expected range for self-organized critical systems.
The log-log plot of avalanche size versus probability density shows a clear straight-line region in the intermediate scaling range, confirming scale-invariant behavior.
Deviations at large avalanche sizes are due to finite-size effects which is a natural consequence of simulating a finite lattice.

Simulation Parameters : 

 Grid Size (N) = 120
 
 Growth probability (p) = 0.05
 
 Fire Trigger interval = 40 growth events 
 
 Simulation steps each run = 500000
 
 Number of Independent runs = 3

Files in This Repository :

forest_fire.py - Main Python simulation code

[Project Report (PDF)](2022ch11028_archie_singh_individual%20project.pdf)

2022ch11028_archie_singh_individual project.tex - LaTeX source file for the report

Graph.png - Avalanche size distribution plot (log-log)

How to Run ?

Make sure you have Python installed with the following libraries:

pip install numpy matplotlib

Then run:
python forest_fire.py

The simulation will run and display the avalanche size distribution plot with the fitted power law line and estimated τ value.

References

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of 1/f noise. Physical Review Letters, 59(4), 381–384.

Drossel, B., & Schwabl, F. (1992). Self-organized critical forest-fire model. Physical Review Letters, 69(11), 1629–1632.

Buchanan, M. (2000). Ubiquity: Why Catastrophes Happen. Crown Publishers.


Acknowledgement
This project was developed with assistance from AI tools for code generation, debugging, and some conceptual clarification. 
All scientific interpretations are verified against the cited literature.

Author

Archie Singh

Department of Chemical Engineering

Individual Project — Complexity Science

April 2026
