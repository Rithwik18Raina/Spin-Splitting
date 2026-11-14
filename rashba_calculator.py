import re
import os
import numpy as np
import matplotlib.pyplot as plt

def merge_band_lists(band_lists):
    """
    Merge multiple band data lists by averaging the energies and occupancies.
    Assumes all band data lists are lists of dictionaries with keys 'band', 'energy', 'occ'.
    """
    if not band_lists:
        return []
    num_bands = len(band_lists[0])
    merged = []
    for b in range(num_bands):
        sum_energy = 0.0
        sum_occ = 0.0
        for band_list in band_lists:
            sum_energy += band_list[b]['energy']
            sum_occ += band_list[b]['occ']
        merged.append({
            'band': band_lists[0][b]['band'],
            'energy': sum_energy / len(band_lists),
            'occ': sum_occ / len(band_lists)
        })
    return merged

def parse_outcar(file_path, hs_points, hs_labels):
    """
    Refined parser for OUTCAR files.
    """
    fermi_energy = None
    kpoints = []
    bands_data = []
    current_kpoint_bands = []
    reading_bands = False

    try:
        with open(file_path, 'r') as f:
            for line in f:
                line_stripped = line.strip()

                if "E-fermi" in line_stripped and fermi_energy is None:
                    parts = line_stripped.split()
                    try:
                        fermi_energy = float(parts[2])
                    except (IndexError, ValueError):
                        fermi_energy = None
                    continue

                if "k-point" in line_stripped.lower():
                    if current_kpoint_bands:
                        bands_data.append(current_kpoint_bands)
                        current_kpoint_bands = []

                    if ':' in line_stripped:
                        parts_split = line_stripped.split(':', 1)
                        coords_part = parts_split[1].split()
                        if len(coords_part) == 3:
                            try:
                                kx, ky, kz = map(float, coords_part)
                                kpoints.append((kx, ky, kz))
                            except ValueError:
                                pass
                    continue

                if "band No." in line_stripped:
                    reading_bands = True
                    continue

                if reading_bands:
                    if "-------------------------------" in line_stripped:
                        reading_bands = False
                        continue

                    parts = line_stripped.split()
                    if len(parts) == 3:
                        try:
                            band_index = int(parts[0])
                            band_energy = float(parts[1])
                            band_occ = float(parts[2])
                            current_kpoint_bands.append({
                                'band': band_index,
                                'energy': band_energy,
                                'occ': band_occ
                            })
                        except ValueError:
                            pass

            if current_kpoint_bands:
                bands_data.append(current_kpoint_bands)

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    merged_kpoints = []
