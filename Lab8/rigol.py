import csv
import pandas as pd
from matplotlib import pyplot as plt


def read_rigol_csv(csv_file_name):
    """
    Read the weird Rigol scope CSV format into something more easily parasable

    Args:
        csv_file_name: filepath to Rigol csv export

    Returns:
        data: a pandas dataframe with time & channel output variables
        t0: float representing starting time
        dT: float represetning
    """
    with open(csv_file_name) as f:
        rows = list(csv.reader(f))
        i = 0
        while rows[0][i] != "":
            i = i + 1
        numcols = i - 2
        t0 = float(rows[1][numcols])
        dT = float(rows[1][numcols + 1])
        data = pd.read_csv(csv_file_name, usecols=range(0, numcols), skiprows=[1])
        data["X"] = t0 + data["X"] * dT
    return data, t0, dT


def graph_shunt_drain(csv_file_name, v_label):
    [scope_data, _, _] = read_rigol_csv(csv_file_name)

    fig, ax1 = plt.subplots()

    ax1.plot(scope_data["X"], scope_data["CH1"], label="Vsh")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Shunt Voltage (V)")

    plt.xlim(5e-5, 8.3e-5)
    ax2 = ax1.twinx()
    ax2.plot(scope_data["X"], scope_data["CH2"], label="Vdrain", color="tab:orange")
    ax2.set_ylabel("Drain Voltage (V)")

    plt.title(f"Baseline Flyback Voltage over Time (Vin = {v_label})")
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [line.get_label() for line in lines], loc="upper center")
