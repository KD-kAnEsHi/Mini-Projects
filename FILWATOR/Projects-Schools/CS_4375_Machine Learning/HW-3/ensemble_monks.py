import numpy as np
import sys
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from decision_trees import id3, predict_example
from collections import Counter

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
        indices = np.random.choice(n, size=n, replace=True, p=weights)
        X_sample, y_sample = X[indices], y[indices]

        tree = id3(X_sample, y_sample, max_depth=max_depth)
        predictions = np.array([predict_example(x, tree) for x in X])
        error = np.sum(weights * (predictions != y))

        if error >= 0.5 or error == 0:
            continue

        alpha = 0.5 * np.log((1 - error) / (error + 1e-10))
        weights *= np.exp(-alpha * (2 * (predictions == y) - 1))
        weights /= np.sum(weights)

        ensemble.append((alpha, tree))

    return ensemble

# === Predict single example with ensemble ===
def predict_ensemble(x, h_ens):
    score = sum(alpha * (1 if predict_example(x, h) == 1 else -1) for alpha, h in h_ens)
    return 1 if score >= 0 else 0

# === Evaluation ===
def evaluate(X_test, y_test, h_ens):
    predictions = [predict_ensemble(x, h_ens) for x in X_test]
    return confusion_matrix(y_test, predictions)

# === Load MONK dataset ===
def load_monk_data(train_path, test_path):
    train = np.genfromtxt(train_path, delimiter=',', dtype=int)
    test = np.genfromtxt(test_path, delimiter=',', dtype=int)
    X_train, y_train = train[:, 1:], train[:, 0]
    X_test, y_test = test[:, 1:], test[:, 0]
    return X_train, X_test, y_train, y_test

# === Main execution ===
def run_experiment(dataset_name):
    train_file = f"monks-{dataset_name}.train"
    test_file = f"monks-{dataset_name}.test"
    X_train, X_test, y_train, y_test = load_monk_data(train_file, test_file)

    print(f"========= Dataset: MONK-{dataset_name} =========")

    print("========= Custom Bagging =========")
    for d in [3, 5]:
        for k in [10, 20]:
            h_ens = bagging(X_train, y_train, max_depth=d, num_trees=k)
            print(f"Bagging depth={d}, trees={k}:")
            print(evaluate(X_test, y_test, h_ens))

    print("========= Custom Boosting =========")
    for d in [1, 2]:
        for k in [20, 40]:
            h_ens = boosting(X_train, y_train, max_depth=d, num_stumps=k)
            print(f"Boosting depth={d}, stumps={k}:")
            print(evaluate(X_test, y_test, h_ens))

    print("========= scikit-learn Bagging =========")
    for d in [3, 5]:
        for k in [10, 20]:
            model = BaggingClassifier(
                estimator=DecisionTreeClassifier(max_depth=d),
                n_estimators=k
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            print(f"Bagging (depth={d}, trees={k}) Confusion Matrix:")
            print(confusion_matrix(y_test, y_pred))

    print("========= scikit-learn Boosting =========")
    for d in [1, 2]:
        for k in [20, 40]:
            model = AdaBoostClassifier(
                estimator=DecisionTreeClassifier(max_depth=d),
                n_estimators=k
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            print(f"Boosting (depth={d}, stumps={k}) Confusion Matrix:")
            print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ensemble_monks.py <dataset_number: 1, 2, or 3>")
    else:
        run_experiment(sys.argv[1])
