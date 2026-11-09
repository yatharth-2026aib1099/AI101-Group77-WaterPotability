import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


def train_model(X_train_scaled, y_train, feature_names):
  model = LogisticRegression(
      class_weight='balanced', max_iter=1000, random_state=42
  )
  model.fit(X_train_scaled, y_train)

  weights = pd.DataFrame({
      'Feature': feature_names,
      'Coefficient': model.coef_[0],
      'Odds_Ratio': np.exp(model.coef_[0]),
  })
  print('\nModel Coefficients and Odds Ratios:')
  print(weights)
  return model
