import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Automate average temperature and station name.
    prcp = ''
    name_si = ''
    station_name_si = ''
    for index, column_value in enumerate(header_row):
        if column_value == 'PRCP':
            prcp = index
        elif column_value == 'NAME':
            name_si = index

    # Get dates, station name, and average temperature.
    dates_si, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        if not station_name_si:
            station_name_si = row[name_si]
        try:
            prcp_entry = float(row[prcp])
        except ValueError:
            print(f"Missing data from {current_date}")
        else:
            dates_si.append(current_date)
            prcps.append(prcp_entry)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Automate observed temperature and station name.
    tobs = ''
    name_dv = ''
    station_name_dv = ''
    for index, column_value in enumerate(header_row):
        if column_value == 'TOBS':
            tobs = index
        elif column_value == 'NAME':
            name_dv = index

    # Get dates, station name, and observed temperature.
    dates_dv, obs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        if not station_name_dv:
            station_name_dv = row[name_dv]
        try:
            ob = int(row[tobs])
        except ValueError:
            print(f"Missing data from {current_date}")
        else:
            dates_dv.append(current_date)
            obs.append(ob)

# Plot the Sitka average temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_si, prcps, c='red', alpha=0.5)
ax.plot(dates_dv, obs, c='blue', alpha=0.5)
plt.fill_between(dates_si and dates_dv, prcps, obs, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Precipitation vs. Observed Temperature - 2018\n{station_name_si}(Red) vs. {station_name_dv}(Blue)"
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='both', labelsize=16)

plt.show()
