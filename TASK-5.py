import pandas as pd

# Load the dataset
file_path = 'E:\\INRERN PROJECTS\\TASK-5\\Accident.csv'
accident_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(accident_data.head())

# Check for missing values in the dataset
missing_values = accident_data.isnull().sum()
missing_values_summary = missing_values[missing_values > 0]

missing_values_summary

# Convert 'Time' column to datetime
accident_data['Time'] = pd.to_datetime(accident_data['Time'], format='%H:%M:%S', errors='coerce')

# Extract hour from 'Time' column
accident_data['Hour'] = accident_data['Time'].dt.hour

# Overview of accidents by hour of the day
accidents_by_hour = accident_data['Hour'].value_counts().sort_index()

# Overview of accidents by day of the week
accidents_by_day = accident_data['Day_of_week'].value_counts().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

accidents_by_hour, accidents_by_day

import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting style
sns.set(style="whitegrid")

# Plot accidents by hour of the day
plt.figure(figsize=(12, 6))
sns.barplot(x=accidents_by_hour.index, y=accidents_by_hour.values, palette="Blues_d")
plt.title('Number of Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

# Plot accidents by day of the week
plt.figure(figsize=(10, 6))
sns.barplot(x=accidents_by_day.index, y=accidents_by_day.values, palette="Blues_d")
plt.title('Number of Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
