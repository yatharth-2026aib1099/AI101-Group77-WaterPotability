from src.eda import run_eda
from src.preprocess import get_preprocessed_data
from src.train import train_model
from src.evaluate import evaluate_model

if __name__ == "__main__":
    print("=== Step 1: Exploratory Data Analysis ===")
    run_eda()
    
    print("\n=== Step 2: Preprocessing & Scaling ===")
    X_train_scaled, X_test_scaled, y_train, y_test, features = get_preprocessed_data()
    
    print("\n=== Step 3: Model Training ===")
    model = train_model(X_train_scaled, y_train, features)
    
    print("\n=== Step 4: Model Evaluation ===")
    evaluate_model(model, X_test_scaled, y_test)
