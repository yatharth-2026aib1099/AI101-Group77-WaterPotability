import numpy as np
import pandas as pd
def run_eda():
  df = pd.read_csv('data/water_potability.csv')
  print('Dataset Shape:', df.shape)
  print('\nClass Distribution:')
  print(df['Potability'].value_counts())
  means = df.mean()
  medians = df.median()
  stds = df.std()
  summary = pd.DataFrame({'Mean': means, 'Median': medians, 'Std_Dev': stds})
  print('\nSummary Statistics (Mean, Median, Std Dev):')
  print(summary)
  return summary
