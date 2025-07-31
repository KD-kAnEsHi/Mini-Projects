# Karl Azangue, kka210001
# Aaron Fredericks, ajf220004

import numpy as np
from collections import Counter

from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


def partition(x):
    groups = {}
    for i, val in enumerate(x):
        groups.setdefault(val, []).append(i)
    return groups

def entropy(y, weights=None):
    if weights is None:
        weights = np.ones(len(y)) / len(y)

    value_weights = {}
    for i, val in enumerate(y):
        value_weights[val] = value_weights.get(val, 0) + weights[i]

    total_weight = sum(value_weights.values())
    probs = [w / total_weight for w in value_weights.values()]
    return -np.sum([p * np.log2(p + 1e-10) for p in probs])

def mutual_information(x, y, weights=None):
    total_entropy = entropy(y, weights)
    groups = partition(x)

    weighted_entropy = 0
    total_weight = sum(weights) if weights is not None else len(y)
    for val, indices in groups.items():
        group_weights = weights[indices] if weights is not None else None
        group_entropy = entropy(y[indices], group_weights)
        group_weight = np.sum(group_weights) if weights is not None else len(indices)
        weighted_entropy += (group_weight / total_weight) * group_entropy

    return total_entropy - weighted_entropy

def id3(x, y, attribute_value_pairs=None, depth=0, max_depth=5, weights=None):
    if len(np.unique(y)) == 1:
        return y[0]
    
    if attribute_value_pairs is None:
        attribute_value_pairs = []
        for i in range(x.shape[1]):
            for val in np.unique(x[:, i]):
                attribute_value_pairs.append((i, val))

    if len(attribute_value_pairs) == 0 or depth == max_depth:
        if weights is None:
            return Counter(y).most_common(1)[0][0]
        else:
            label_weights = {}
            for i, label in enumerate(y):
                label_weights[label] = label_weights.get(label, 0) + weights[i]
            return max(label_weights, key=label_weights.get)

    best_gain = -1
    best_pair = None
    for attr, val in attribute_value_pairs:
        col = (x[:, attr] == val)
        gain = mutual_information(col, y, weights)
        if gain > best_gain:
            best_gain = gain
            best_pair = (attr, val)

    if best_gain <= 0:
        return Counter(y).most_common(1)[0][0]

    attr, val = best_pair
    new_attr_pairs = [p for p in attribute_value_pairs if p != best_pair]

    mask_true = (x[:, attr] == val)
    mask_false = ~mask_true

    weights_true = weights[mask_true] if weights is not None else None
    weights_false = weights[mask_false] if weights is not None else None

    left = id3(x[mask_true], y[mask_true], new_attr_pairs, depth+1, max_depth, weights_true) if np.any(mask_true) else Counter(y).most_common(1)[0][0]
    right = id3(x[mask_false], y[mask_false], new_attr_pairs, depth+1, max_depth, weights_false) if np.any(mask_false) else Counter(y).most_common(1)[0][0]

    return {(attr, val, True): left, (attr, val, False): right}


def bootstrap_sampler(x, y, num_samples):
    indices = np.random.choice(len(y), num_samples, replace=True)
    return x[indices], y[indices]

def bagging(x, y, max_depth, num_trees):
    h_ens = []
    for _ in range(num_trees):
        x_sample, y_sample = bootstrap_sampler(x, y, len(y))
        tree = id3(x_sample, y_sample, max_depth=max_depth)
        h_ens.append((1, tree))  # alpha = 1 for uniform voting
    return h_ens

def boosting(x, y, max_depth, num_stumps):
    n = len(y)
    D = np.ones(n) / n
    h_ens = []

    for _ in range(num_stumps):
        tree = id3(x, y, max_depth=max_depth, weights=D)
        y_pred = np.array([predict_example(xi, tree) for xi in x])
        err = np.sum(D * (y_pred != y))

        if err >= 0.5 or err == 0:
            continue

        alpha = 0.5 * np.log((1 - err) / (err + 1e-10))
        D *= np.exp(-alpha * y * (2 * (y_pred == y) - 1))
        D /= np.sum(D)

        h_ens.append((alpha, tree))

    return h_ens



def predict_example(x, tree):
    if not isinstance(tree, dict):
        return tree
    for (attr, val, branch), subtree in tree.items():
        if (x[attr] == val) == branch:
            return predict_example(x, subtree)
    return 0  # fallback to default prediction (majority class or safest guess)
  





def predict_example_ens(x, h_ens):
    score = sum(alpha * (1 if predict_example(x, h) == 1 else -1) for alpha, h in h_ens)
    return 1 if score > 0 else 0

def compute_error(y_true, y_pred):
    return np.mean(np.array(y_true) != np.array(y_pred))





def visualize(tree, depth=0):
    """
    Pretty prints (kinda ugly, but hey, it's better than nothing) the decision tree to the console. Use print(tree) to
    print the raw nested dictionary representation.
    DO NOT MODIFY THIS FUNCTION!
    """

    if depth == 0:
        print('TREE')

    for index, split_criterion in enumerate(tree):
        sub_trees = tree[split_criterion]

        # Print the current node: split criterion
        print('|\t' * depth, end='')
        print('+-- [SPLIT: x{0} = {1}]'.format(split_criterion[0], split_criterion[1]))

        # Print the children
        if type(sub_trees) is dict:
            visualize(sub_trees, depth + 1)
        else:
            print('|\t' * (depth + 1), end='')
            print('+-- [LABEL = {0}]'.format(sub_trees))


if __name__ == '__main__':
    # Load the training data
    M = np.genfromtxt('./monks-3.train', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytrn = M[:, 0]
    Xtrn = M[:, 1:]

    # Load the test data
    M = np.genfromtxt('./monks-3.test', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytst = M[:, 0]
    Xtst = M[:, 1:]

    # Learn a decision tree of depth 3
    decision_tree = id3(Xtrn, ytrn, max_depth=3)
    visualize(decision_tree)

    # Compute the test error
    y_pred = [predict_example(x, decision_tree) for x in Xtst]
    tst_err = compute_error(ytst, y_pred)

    print('Test Error = {0:4.2f}%.'.format(tst_err * 100))


    # PART A: 
    depths = [3, 5]
    tree_counts = [10, 20]

    for d in depths:
        for k in tree_counts:
            print(f"Bagging: max_depth={d}, num_trees={k}")
            h_ens = bagging(Xtrn, ytrn, max_depth=d, num_trees=k)
            y_pred = np.array([predict_example_ens(x, h_ens) for x in Xtst])
            ytst = np.array(ytst) 
            
            # Confusion matrix
            tp = np.sum((ytst == 1) & (y_pred == 1))
            tn = np.sum((ytst == 0) & (y_pred == 0))
            fp = np.sum((ytst == 0) & (y_pred == 1))
            fn = np.sum((ytst == 1) & (y_pred == 0))

            print(f"Confusion Matrix: [[TP: {tp}, FN: {fn}], [FP: {fp}, TN: {tn}]]\n")

    
    
    # PART B: 
    depths = [1, 2]
    stump_counts = [20, 40]

    for d in depths:
        for k in stump_counts:
            print(f"Boosting: max_depth={d}, num_stumps={k}")
            h_ens = boosting(Xtrn, ytrn, max_depth=d, num_stumps=k)
            y_pred = np.array([predict_example_ens(x, h_ens) for x in Xtst])
            ytst = np.array(ytst) 
            
            # Confusion matrix
            tp = np.sum((ytst == 1) & (y_pred == 1))
            tn = np.sum((ytst == 0) & (y_pred == 0))
            fp = np.sum((ytst == 0) & (y_pred == 1))
            fn = np.sum((ytst == 1) & (y_pred == 0))

            print(f"Confusion Matrix: [[TP: {tp}, FN: {fn}], [FP: {fp}, TN: {tn}]]\n")







    # PART C: 

    print("===== scikit-learn Bagging =====")
    for d in [3, 5]:
        for k in [10, 20]:
            model = BaggingClassifier(
                estimator=DecisionTreeClassifier(max_depth=d),
                n_estimators=k
            )
            model.fit(Xtrn, ytrn)
            y_pred = model.predict(Xtst)
            cm = confusion_matrix(ytst, y_pred)
            print(f"Bagging (depth={d}, trees={k}) Confusion Matrix:\n{cm}\n")

    print("===== scikit-learn Boosting =====")
    for d in [1, 2]:
        for k in [20, 40]:
            model = AdaBoostClassifier(
                estimator=DecisionTreeClassifier(max_depth=d),
                n_estimators=k
            )
            model.fit(Xtrn, ytrn)
            y_pred = model.predict(Xtst)
            cm = confusion_matrix(ytst, y_pred)
            print(f"Boosting (depth={d}, stumps={k}) Confusion Matrix:\n{cm}\n")

