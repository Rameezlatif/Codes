# -*- coding: utf-8 -*-
"""Gromacs_XVG_Plots_Codes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lfQtwva-m-SthRIlrEFfDUh3PmXOIMAq
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load RMSD data from the XVG files
data1 = np.loadtxt('rmsd_complex_B7_IL1.xvg', comments=['@', '#'])
data2 = np.loadtxt('rmsd_complex_positive_IL1.xvg', comments=['@', '#'])
data3 = np.loadtxt('rmsd_Apo.xvg', comments=['@', '#'])

# Convert time from ps to ns (assuming time is in the first column)
time_ns = data1[:, 0] / 1000  # Convert ps to ns

# Extract RMSD values (assuming RMSD is in the second column)
rmsd1 = data1[:, 1]
rmsd2 = data2[:, 1]
rmsd3 = data3[:, 1]

# Calculate average RMSD
avg_rmsd1 = np.mean(rmsd1)
avg_rmsd2 = np.mean(rmsd2)
avg_rmsd3 = np.mean(rmsd3)

# Calculate standard deviation of RMSD
std_rmsd1 = np.std(rmsd1)
std_rmsd2 = np.std(rmsd2)
std_rmsd3 = np.std(rmsd3)

# Calculate maximum RMSD
max_rmsd1 = np.max(rmsd1)
max_rmsd2 = np.max(rmsd2)
max_rmsd3 = np.max(rmsd3)

# Print statistical measures
print("Statistical Measures for RMSD:")
print("================================")
print("Average RMSD (IL1R1/IL-1β-B7 Complex):", avg_rmsd1)
print("Average RMSD (IL1R1/IL-1β-Positive Complex):", avg_rmsd2)
print("Average RMSD (IL-1R1/IL-1β Complex):", avg_rmsd3)
print("Standard Deviation RMSD (IL1R1/IL-1β-B7 Complex):", std_rmsd1)
print("Standard Deviation RMSD (IL1R1/IL-1β-Positive Complex):", std_rmsd2)
print("Standard Deviation RMSD (IL-1R1/IL-1β Complex):", std_rmsd3)
print("Maximum RMSD (IL1R1/IL-1β-B7 Complex):", max_rmsd1)
print("Maximum RMSD (IL1R1/IL-1β-Positive Complex):", max_rmsd2)
print("Maximum RMSD (IL-1R1/IL-1β Complex):", max_rmsd3)

# Create DataFrame with results
data = {'Complex': ['IL1R1/IL-1β-B7', 'IL1R1/IL-1β-Positive', 'IL-1R1/IL-1β'],
        'Average RMSD (Å)': [avg_rmsd1, avg_rmsd2, avg_rmsd3],
        'Standard Deviation RMSD (Å)': [std_rmsd1, std_rmsd2, std_rmsd3],
        'Maximum RMSD (Å)': [max_rmsd1, max_rmsd2, max_rmsd3]}
df = pd.DataFrame(data)

# Save DataFrame to Excel file
df.to_excel('rmsd_results.xlsx', index=False)

# Plot RMSD data
plt.figure(figsize=(10, 6))
plt.plot(time_ns, rmsd1, label='IL1R1/IL-1β-B7 Complex', color='blue')
plt.plot(time_ns, rmsd2, label='IL1R1/IL-1β-Positive Complex', color='red')
plt.plot(time_ns, rmsd3, label='IL-1R1/IL-1β Complex', color='green')
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (Å)')
plt.title('Root Mean Square Deviation (RMSD) vs. Time')
plt.legend()
plt.grid(True)

# Save plot as PNG and PDF files
plt.savefig('rmsd_plot.png')
plt.savefig('rmsd_plot.pdf')

# Show plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to read RMSF data from XVG file
def read_rmsf_data(filename):
    residues = []
    rmsf_values = []

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('@') or line.startswith('#'):
                continue
            columns = line.split()
            residue = int(columns[0])
            rmsf = float(columns[1])
            residues.append(residue)
            rmsf_values.append(rmsf)

    return residues, rmsf_values

# Read data from all three XVG files
residues_1, rmsf_values_1 = read_rmsf_data('rmsf-protein-apo-res.xvg')
residues_2, rmsf_values_2 = read_rmsf_data('rmsf-protein-pos-res.xvg')
residues_3, rmsf_values_3 = read_rmsf_data('rmsf-protein-B7-res.xvg')

# Calculate statistics
mean_rmsf_1 = np.mean(rmsf_values_1)
std_rmsf_1 = np.std(rmsf_values_1)
mean_rmsf_2 = np.mean(rmsf_values_2)
std_rmsf_2 = np.std(rmsf_values_2)
mean_rmsf_3 = np.mean(rmsf_values_3)
std_rmsf_3 = np.std(rmsf_values_3)

# Print out statistical measures
print("Mean RMSF (IL1R1/IL-1β-Apo):", mean_rmsf_1)
print("Standard Deviation RMSF (IL1R1/IL-1β-Apo):", std_rmsf_1)
print("Mean RMSF (IL1R1/IL-1β-Positive):", mean_rmsf_2)
print("Standard Deviation RMSF (IL1R1/IL-1β-Positive):", std_rmsf_2)
print("Mean RMSF (IL1R1/IL-1β-B7):", mean_rmsf_3)
print("Standard Deviation RMSF (IL1R1/IL-1β-B7):", std_rmsf_3)

# Plot RMSF from all three files
plt.figure(figsize=(10, 6))
plt.plot(residues_1, rmsf_values_1, label='IL1R1/IL-1β-Apo Complex', marker='o', linestyle='-')
plt.plot(residues_2, rmsf_values_2, label='IL1R1/IL-1β-Positive Complex', marker='o', linestyle='-')
plt.plot(residues_3, rmsf_values_3, label='IL1R1/IL-1β-B7 Complex', marker='o', linestyle='-')
plt.fill_between(residues_1, mean_rmsf_1 - std_rmsf_1, mean_rmsf_1 + std_rmsf_1, color='r', alpha=0.2)
plt.fill_between(residues_2, mean_rmsf_2 - std_rmsf_2, mean_rmsf_2 + std_rmsf_2, color='g', alpha=0.2)
plt.fill_between(residues_3, mean_rmsf_3 - std_rmsf_3, mean_rmsf_3 + std_rmsf_3, color='b', alpha=0.2)
plt.xlabel('Residue')
plt.ylabel('RMSF (Å)')
plt.title('Root Mean Square Fluctuations (RMSF)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot as PNG and PDF
plt.savefig('rmsf_plot.png')
plt.savefig('rmsf_plot.pdf')

# Generate Excel file with RMSF data
data = {'Residue': residues_1, 'RMSF_Apo': rmsf_values_1, 'RMSF_Positive': rmsf_values_2, 'RMSF_B7': rmsf_values_3}
df = pd.DataFrame(data)
df.to_excel('rmsf_data.xlsx', index=False)

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to read Rg data from XVG file
def read_rg_data(filename):
    time = []
    rg_values = []

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('@') or line.startswith('#'):
                continue
            columns = line.split()
            t = float(columns[0])  # Assuming time is in the first column
            rg = float(columns[1])  # Assuming Rg is in the second column
            time.append(t)
            rg_values.append(rg)

    return time, rg_values

# Read data from all three XVG files
time_1, rg_values_1 = read_rg_data('gyrate_Apo.xvg')
time_2, rg_values_2 = read_rg_data('gyrate_positive.xvg')
time_3, rg_values_3 = read_rg_data('gyrate_B7_complex.xvg')

# Calculate statistics
mean_rg_1 = np.mean(rg_values_1)
std_rg_1 = np.std(rg_values_1)
mean_rg_2 = np.mean(rg_values_2)
std_rg_2 = np.std(rg_values_2)
mean_rg_3 = np.mean(rg_values_3)
std_rg_3 = np.std(rg_values_3)

# Print out statistical measures
print("Mean Rg (IL1R1/IL-1β-Apo):", mean_rg_1)
print("Standard Deviation Rg (IL1R1/IL-1β-Apo):", std_rg_1)
print("Mean Rg (IL1R1/IL-1β-Positive):", mean_rg_2)
print("Standard Deviation Rg (IL1R1/IL-1β-Positive):", std_rg_2)
print("Mean Rg (IL1R1/IL-1β-B7):", mean_rg_3)
print("Standard Deviation Rg (IL1R1/IL-1β-B7):", std_rg_3)

# Plot Rg from all three files
plt.figure(figsize=(10, 6))
plt.plot(time_1, rg_values_1, label='IL1R1/IL-1β-Apo Complex', marker='o', linestyle='-')
plt.plot(time_2, rg_values_2, label='IL1R1/IL-1β-Positive Complex', marker='o', linestyle='-')
plt.plot(time_3, rg_values_3, label='IL1R1/IL-1β-B7 Complex', marker='o', linestyle='-')
plt.axhline(y=mean_rg_1, color='r', linestyle='--')
plt.axhline(y=mean_rg_2, color='g', linestyle='--')
plt.axhline(y=mean_rg_3, color='b', linestyle='--')
plt.fill_between(time_1, mean_rg_1 - std_rg_1, mean_rg_1 + std_rg_1, color='r', alpha=0.2)
plt.fill_between(time_2, mean_rg_2 - std_rg_2, mean_rg_2 + std_rg_2, color='g', alpha=0.2)
plt.fill_between(time_3, mean_rg_3 - std_rg_3, mean_rg_3 + std_rg_3, color='b', alpha=0.2)
plt.xlabel('Time (ns)')
plt.ylabel('Radius of Gyration (Å)')
plt.title('Radius of Gyration (Rg) vs. Time')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot as PNG and PDF
plt.savefig('rg_plot.png')
plt.savefig('rg_plot.pdf')

# Generate Excel file with Rg data
data = {'Time (ns)': time_1, 'Rg_Apo': rg_values_1, 'Rg_Positive': rg_values_2, 'Rg_B7': rg_values_3}
df = pd.DataFrame(data)
df.to_excel('rg_data.xlsx', index=False)

# Show the plot
plt.show()