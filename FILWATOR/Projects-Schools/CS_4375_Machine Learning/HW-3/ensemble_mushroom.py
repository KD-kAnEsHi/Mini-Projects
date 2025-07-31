import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from decision_trees import id3, predict_example

# === Bagging ===
def bagging(X, y, max_depth, num_trees):
    ensemble = []
    n = len(X)

    for _ in range(num_trees):
        indices = np.random.choice(n, size=n, replace=True)
        X_sample, y_sample = X[indices], y[indices]

        tree = id3(X_sample, y_sample, max_depth=max_depth)
        ensemble.append((1, tree))  # Weight = 1 for bagging

    return ensemble

# === Boosting ===
def boosting(X, y, max_depth, num_stumps):
    n = len(X)
    weights = np.ones(n) / n
    ensemble = []

    for _ in range(num_stumps):
        # ID3 with sample weights not supported directly; workaround: resample data
        indices = np.random.choice(n, size=n, replace=True, p=weights)
        X_sample, y_sample = X[indices], y[indices]

        tree = id3(X_sample, y_sample, max_depth=max_depth)
        predictions = np.array([predict_example(x, tree) for x in X])
        error = np.sum(weights * (predictions != y))

        if error > 0.5 or error == 0:
            continue

        alpha = 0.5 * np.log((1 - error) / error)
        weights *= np.exp(-alpha * (2 * (predictions == y) - 1))
        weights /= np.sum(weights)

        ensemble.append((alpha, tree))

    return ensemble

# === Predict function ===
def predict_ensemble(x, h_ens):
    total = 0
    for alpha, tree in h_ens:
        pred = predict_example(x, tree)
        total += alpha * (1 if pred == 1 else -1)
    return 1 if total >= 0 else 0

# === Evaluation ===
def evaluate(X_test, y_test, h_ens):
    predictions = [predict_ensemble(x, h_ens) for x in X_test]
    return confusion_matrix(y_test, predictions)

# === Load and prepare Mushroom dataset ===
def load_mushroom_data():
    df = pd.read_csv("mushroom.csv")  # Ensure this file exists with integer-encoded features
    y = df['bruises'].values
    X = df.drop(columns=['bruises']).values
    return train_test_split(X, y, test_size=0.3, random_state=42)

# === Main execution ===
def main():
    X_train, X_test, y_train, y_test = load_mushroom_data()

    print("== Bagging ==")
    for d in [3, 5]:
        for k in [10, 20]:
            h_ens = bagging(X_train, y_train, max_depth=d, num_trees=k)
            print(f"Bagging depth={d}, trees={k}:")
            print(evaluate(X_test, y_test, h_ens))

    print("== Boosting ==")
    for d in [1, 2]:
        for k in [20, 40]:
            h_ens = boosting(X_train, y_train, max_depth=d, num_stumps=k)
            print(f"Boosting depth={d}, stumps={k}:")
            print(evaluate(X_test, y_test, h_ens))

    print("== Scikit-learn Comparison ==")
    for d in [3, 5]:
        for k in [10, 20]:
            clf = BaggingClassifier(n_estimators=k)
            clf.fit(X_train, y_train)
            print(f"sklearn Bagging depth={d}, trees={k}:")
            print(confusion_matrix(y_test, clf.predict(X_test)))

    for d in [1, 2]:
        for k in [20, 40]:
            clf = AdaBoostClassifier(n_estimators=k)
            clf.fit(X_train, y_train)
            print(f"sklearn Boosting depth={d}, stumps={k}:")
            print(confusion_matrix(y_test, clf.predict(X_test)))

if __name__ == "__main__":
    main()
