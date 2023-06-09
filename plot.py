import argparse
import matplotlib
import matplotlib.pyplot as plt
import os
import pandas as pd

matplotlib.use('TkAgg')
ext = '.xlsx'

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True)
parser.add_argument('--margin', type=int, choices=[3,5,10], default=5)
args = parser.parse_args()
path = args.path if os.path.splitext(args.path)[1] else f'{args.path}{ext}'
margin = args.margin

def plot(title: str, frame: pd.DataFrame):
    plt.figure()
    label_ref_x = frame.columns[0]
    label_ref_y_high = f'P{100-margin}'
    label_ref_y_mid  = f'P{50}'
    label_ref_y_low  = f'P{margin}'
    label_x = 'X' if 'X' in frame.columns else label_ref_x
    label_y = 'Y'

    series_ref_x = frame[label_ref_x]
    series_ref_y_high = frame[label_ref_y_high]
    series_ref_y_mid = frame[label_ref_y_mid]
    series_ref_y_low = frame[label_ref_y_low]
    series_x = frame[label_x]
    series_y = frame[label_y]

    plt.plot(series_ref_x, series_ref_y_high, ':r', label=label_ref_y_high, linewidth=0.7)
    plt.plot(series_ref_x, series_ref_y_mid , ':g', label=label_ref_y_mid , linewidth=0.7)
    plt.plot(series_ref_x, series_ref_y_low , ':b', label=label_ref_y_low , linewidth=0.7)
    plt.plot(series_x, series_y, marker='.', color='grey', label=label_y)

    plt.xlabel(label_ref_x)
    plt.grid(True)
    plt.title(title)
    plt.legend()

frames = pd.read_excel(path, sheet_name=None)
for name, frame in frames.items():
    plot(name, frame)
plt.show()
