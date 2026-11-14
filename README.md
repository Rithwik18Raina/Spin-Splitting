# Rashba Spin-Splitting Calculator

**Author:** Rithwik Raina

## Overview

This Python tool automates the calculation of Rashba spin-splitting parameters at the Valence Band Maximum (VBM) and Conduction Band Minimum (CBM) using VASP band-structure calculations.

The calculation involves identifying band extrema and corresponding spin-degeneracy points, followed by evaluating the energy and momentum offsets required to determine the Rashba parameter. This analysis can otherwise be tedious and time-consuming when performed manually.

## Features

- Parses VASP `OUTCAR` and `KPOINTS` files.
- Extracts Fermi energy, k-point coordinates, band energies and occupancies.
- Identifies the VBM, CBM and band gap.
- Detects relevant local band extrema and degeneracy points.
- Calculates Rashba spin-splitting parameters at the valence and conduction bands.
- Plots the band structure and highlights the identified extrema.

## Input Files

The program requires two input files from a VASP band-structure calculation:

1. **OUTCAR:** Contains the calculated band energies, k-point coordinates, Fermi energy and reciprocal lattice vectors.
2. **KPOINTS:** Contains the high-symmetry k-point path, coordinates and labels.

Both files must correspond to the same band-structure calculation.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

### Google Colab

1. Upload `rashba_calculator.py` to your Google Colab session.
2. Run the script using:

```python
%run rashba_calculator.py
```

3. A file-upload window will appear.
4. Select both `OUTCAR` and `KPOINTS`.
5. The program will perform the analysis and display the results and band-structure plot.

### Local Python Environment

Run the script using:

```bash
python rashba_calculator.py
```

The program will open file-selection windows to select the required input files.

## Output

The program provides:

- Fermi energy
- Valence Band Maximum (VBM)
- Conduction Band Minimum (CBM)
- Electronic band gap
- Identified local extrema
- Rashba spin-splitting parameters at the valence and conduction bands
- Band-structure plot with marked extrema

The calculated Rashba parameters are printed with up to eight decimal places.

## Repository Structure

```text
Rashba-Spin-Splitting/
│
├── rashba_calculator.py
├── README.md
├── requirements.txt
└── sample_band_structure.png
```

## Acknowledgements

Developed as part of computational research on Rashba spin splitting in two-dimensional materials.
