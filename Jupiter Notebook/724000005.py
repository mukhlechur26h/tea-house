import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("724-000005.csv")

# Convert 'Time' to datetime and set as index
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d,%H:%M:%S')
df.set_index('Time', inplace=True)

# Rename columns for clarity
df.rename(columns={
    'Vb [m3]': 'Uncorrected Volume',
    'Vm [m3]': 'Corrected Volume',
    'p.MP  [ bar]': 'Pressure (bar)',
    'T.MP [{C]': 'Temperature (C)'
}, inplace=True)

plt.figure(figsize=(14, 5))
plt.plot(df.index, df['Corrected Volume'], label='Corrected Volume')
plt.plot(df.index, df['Uncorrected Volume'], label='Uncorrected Volume', linestyle='--')
plt.title("Corrected vs Uncorrected Volume")
plt.xlabel("Time")
plt.ylabel("Volume (m³)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

fig, ax1 = plt.subplots(figsize=(14, 5))

ax1.set_title("Pressure and Temperature Trends")
ax1.set_xlabel("Time")

# Pressure
ax1.plot(df.index, df['Pressure (bar)'], color='blue', label='Pressure (bar)')
ax1.set_ylabel("Pressure (bar)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Temperature on secondary y-axis
ax2 = ax1.twinx()
ax2.plot(df.index, df['Temperature (C)'], color='red', label='Temperature (°C)')
ax2.set_ylabel("Temperature (°C)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
plt.grid(True)
plt.show()


df['Volume Difference'] = df['Corrected Volume'].diff()

plt.figure(figsize=(14, 4))
plt.bar(df.index, df['Volume Difference'], width=0.03, color='green')
plt.title("Hourly Corrected Volume Difference")
plt.xlabel("Time")
plt.ylabel("Volume Difference (m³)")
plt.grid(True)
plt.tight_layout()
plt.show()


