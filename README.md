# Assignment 1 — Renewables in Electricity Markets

This repository contains the implementation for **Assignment 1** from the course *Renewables in Electricity Markets* at DTU.

Each Jupyter Notebook (Part1.ipynb to Part6.ipynb) corresponds directly to a step in the assignment instructions. All required data is included in the folder and is accessed using **relative paths** to ensure everything runs smoothly on any machine.

---

## File Structure

- `Part1.ipynb` — Step 1: Copper-plate model (1-hour, no network)
- `Part2.ipynb` — Step 2: Multi-period copper-plate with storage (24-hour)
- `Part3.ipynb` — Step 3: Network-constrained model, nodal/zonal pricing
- `Part4.ipynb` — Step 4: KKT conditions and equilibrium formulation (analytical)
- `Part5.ipynb` — Step 5: Balancing market and one-/two-price schemes
- `Part6.ipynb` — Step 6: Reserve market (EU-style and optional US-style)
- `data.py` — Contains all static input data (e.g., generator costs, limits, demand)
- `day_ahead_bids.csv` — Hourly bid price/quantity data for price-elastic demand
- `Assignment.pdf` — The full assignment brief (for reference)

---

## How to Run

> Before starting, ensure Python 3 is installed with the following packages:
> `numpy`, `pandas`, `matplotlib`, `pyomo`

1. Clone or download the full folder
2. Open any notebook (`Part1.ipynb`, `Part2.ipynb`, etc.)
3. Run all cells from top to bottom

> All data is loaded locally. There is **no need to change any file paths**.

---

## Notes

- All models use `Pyomo` and are solved using the `GLPK` solver.
- The CSV file `day_ahead_bids.csv` is read using a relative path: `"day_ahead_bids.csv"`
- All code has been modularized and commented for clarity.
- The appendix containing input tables (generator data, transmission lines, wind data, etc.) is included in the report.

---

## Author

Prepared by: *HANNAH ROBINSON and MATS WIGGER*  
Course: 46755 – Renewables in Electricity Markets  
Instructor: Jalal Kazempour  
Submission Date: March 24, 2025
