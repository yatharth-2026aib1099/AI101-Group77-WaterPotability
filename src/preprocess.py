import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
def get_preprocessed_data():
  df = pd.read_csv('data/water_potability.csv')
  for col in df.columns:
    if df[col].isnull().sum() > 0:
      df[col] = df[col].fillna(df[col].median())
  X = df.drop(columns=['Potability'])
  y = df['Potability']
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.20, random_state=42, stratify=y
  )
  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  return X_train_scaled, X_test_scaled, y_train, y_test, X.columns
