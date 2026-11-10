import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score


def evaluate_model(model, X_test_scaled, y_test):
  y_pred = model.predict(X_test_scaled)

  acc = accuracy_score(y_test, y_pred)
  prec = precision_score(y_test, y_pred, zero_division=0)
  rec = recall_score(y_test, y_pred, zero_division=0)
  f1 = f1_score(y_test, y_pred, zero_division=0)
  cm = confusion_matrix(y_test, y_pred)

  print('\nEvaluation Metrics:')
  print(f'Accuracy:  {acc:.4f}')
  print(f'Precision: {prec:.4f}')
  print(f'Recall:    {rec:.4f}')
  print(f'F1-score:  {f1:.4f}')
  print('\nConfusion Matrix:\n', cm)

  os.makedirs('outputs/plots', exist_ok=True)
  plt.figure(figsize=(5, 4))
  sns.heatmap(
      cm,
      annot=True,
      fmt='d',
      cmap='Blues',
      xticklabels=['Non-Potable', 'Potable'],
      yticklabels=['Non-Potable', 'Potable'],
  )
  plt.xlabel('Predicted')
  plt.ylabel('Actual')
  plt.title('Confusion Matrix')
  plt.tight_layout()
  plt.savefig(
      'outputs/plots/confusion_matrix.png', dpi=300, bbox_inches='tight'
  )
  plt.close()
  print('Plot saved to outputs/plots/confusion_matrix.png')

  return cm
