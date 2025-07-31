import numpy as np
import matplotlib.pyplot as plt
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import confusion_matrix as sk_cm
from sklearn.datasets import load_breast_cancer


def partition(x):
    """
    Partition the column vector x into subsets indexed by its unique values.
    Returns a dictionary mapping each unique value to the list of indices where x == value.
    """
    groups = {}
    for index, value in enumerate(x):
        groups.setdefault(value, []).append(index)
    return groups


def entropy(y):
    """
    Compute the entropy of a vector y.
    Returns the entropy: H(y) = - sum(p * log2(p)) over unique values.
    """
    values, counts = np.unique(y, return_counts=True)
    probabilities = counts / counts.sum()
    return -np.sum(probabilities * np.log2(probabilities))


def mutual_information(x, y):
    """
    Compute the mutual information between a binary feature (x) and the labels (y).
    Returns I(x, y) = H(y) - H(y|x)
    """
    total_entropy = entropy(y)
    groups = partition(x)
    weighted_entropy = 0
    for value, indices in groups.items():
        weight = len(indices) / len(y)
        weighted_entropy += weight * entropy(y[indices])
    return total_entropy - weighted_entropy


def id3(x, y, attribute_value_pairs=None, depth=0, max_depth=5):
    """
    Implements the ID3 algorithm to learn a decision tree.
    The tree is represented as a nested dictionary where keys are tuples:
      (attribute_index, attribute_value, branch)
    with branch being True (if x[attribute_index] == attribute_value) or False.
    """
    if np.unique(y).size == 1:
        return y[0]
    
    if attribute_value_pairs is None:
        attribute_value_pairs = []
        num_attributes = x.shape[1]
        for attr in range(num_attributes):
            for val in np.unique(x[:, attr]):
                attribute_value_pairs.append((attr, val))
    
    if len(attribute_value_pairs) == 0 or depth == max_depth:
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]
    
    # best attribute-value based on mutual inform
    best_gain = -np.inf
    best_pair = None
    for pair in attribute_value_pairs:
        attr, val = pair
        feature_column = (x[:, attr] == val)
        gain = mutual_information(feature_column, y)
        if gain > best_gain:
            best_gain = gain
            best_pair = pair

    if best_gain <= 0:
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]
    
    # Remove the best pair foeerm consideration
    new_attribute_value_pairs = [pair for pair in attribute_value_pairs if pair != best_pair]
    attr, val = best_pair
    tree = {}
    
    # Create masks forwhere  attr == val and where it is not
    mask_true = (x[:, attr] == val)
    mask_false = ~mask_true

    # branch where condition is True
    if np.any(mask_true):
        subtree_true = id3(x[mask_true], y[mask_true], new_attribute_value_pairs, depth + 1, max_depth)
    else:
        values, counts = np.unique(y, return_counts=True)
        subtree_true = values[np.argmax(counts)]
    tree[(attr, val, True)] = subtree_true

    # branch where condition is False
    if np.any(mask_false):
        subtree_false = id3(x[mask_false], y[mask_false], new_attribute_value_pairs, depth + 1, max_depth)
    else:
        values, counts = np.unique(y, return_counts=True)
        subtree_false = values[np.argmax(counts)]
    tree[(attr, val, False)] = subtree_false

    return tree


def predict_example(x, tree):
    """
    Predicts the label for a single example x using the decision tree.
    Traverses the tree recursively until a leaf node (a label) is reached.
    """
    if not isinstance(tree, dict):
        return tree

    for (feature, value, branch), subtree in tree.items():
        if (x[feature] == value) == branch:
            return predict_example(x, subtree)
    return None  # Should not normally be reached.


def compute_error(y_true, y_pred):
    """
    Computes the average error between true labels and predictions.
    """
    return np.mean(y_true != y_pred)


def visualize(tree, depth=0):
    """
    Pretty prints the decision tree to the console.
    DO NOT MODIFY THIS FUNCTION!
    """
    if depth == 0:
        print('TREE')
    for split_criterion in tree:
        subtree = tree[split_criterion]
        print('|\t' * depth, end='')
        print('+-- [SPLIT: x{0} = {1}]'.format(split_criterion[0], split_criterion[1]))
        if isinstance(subtree, dict):
            visualize(subtree, depth + 1)
        else:
            print('|\t' * (depth + 1), end='')
            print('+-- [LABEL = {0}]'.format(subtree))



def part_a_Plot(Y_train, X_train, Y_test, X_test):

    depths = range(1, 11)  # 1 through 10
    train_errors = []
    test_errors = []

    for d in depths:
        tree = id3(X_train, Y_train, max_depth=d)

        # Pred training data
        y_pred_trn = [predict_example(x, tree) for x in X_train]
        train_err = compute_error(Y_train, y_pred_trn)
        train_errors.append(train_err)

        # Pred test data
        y_pred_tst = [predict_example(x, tree) for x in X_test]
        test_err = compute_error(Y_test, y_pred_tst)
        test_errors.append(test_err)

    plt.figure()
    plt.plot(depths, train_errors, marker='o', label='Training Error')
    plt.plot(depths, test_errors, marker='s', label='Test Error')
    plt.xlabel('Tree Depth')
    plt.ylabel('Error')
    plt.legend()
    plt.show()





def confusion_matrix(y_true, y_pred):
    """
    Returns a 2x2 numpy array: [[TN, FP],[FN, TP]]
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    tp = np.sum((y_pred == 1) & (y_true == 1))  # Tp
    tn = np.sum((y_pred == 0) & (y_true == 0))  # Tn
    fp = np.sum((y_pred == 1) & (y_true == 0))  # Fp
    fn = np.sum((y_pred == 0) & (y_true == 1))  # FN

    return np.array([[tp, fn],[fp, tn]])




def sklearn_test(Xtrn, ytrn, Xtst, ytst):
    clf = DecisionTreeClassifier()
    clf.fit(Xtrn, ytrn)

    y_pred_sklearn = clf.predict(Xtst)
    print("Confusion Matrix (scikit-learn):")
    print(sk_cm(ytst, y_pred_sklearn))

    dot_data = export_graphviz(clf,
                                out_file=None,
                                feature_names=[f"x{i}" for i in range(Xtrn.shape[1])],
                                class_names=["0", "1"],
                                filled=True,
                                rounded=True,
                                special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render("decision_tree_visualization", view=True)


def breast_cancer():

    data = load_breast_cancer()
    X = data.data
    y = data.target
    
    # Convert continuous features to binary using mean
    X_binary = np.zeros_like(X)
    for i in range(X.shape[1]):
        mean = np.mean(X[:, i])
        X_binary[:, i] = (X[:, i] > mean).astype(int)
    
    # Split the data into train and test sets (you can use 70-30 split)
    n_samples = len(y)
    n_train = int(0.7 * n_samples)
    
    Xtrn = X_binary[:n_train]
    ytrn = y[:n_train]
    Xtst = X_binary[n_train:]
    ytst = y[n_train:]

    decision_tree_1 = id3(Xtrn, ytrn, max_depth=1)
    print("=== Decision Tree (Depth=1) ===")
    visualize(decision_tree_1)
    y_pred_d1 = [predict_example(x, decision_tree_1) for x in Xtst]
    con_matrix_d1 = confusion_matrix(ytst, y_pred_d1)
    print("\nConfusion Matrix (Depth=1):")
    print(con_matrix_d1)

    decision_tree_2 = id3(Xtrn, ytrn, max_depth=2)
    print("\n=== Decision Tree (Depth=2) ===")
    visualize(decision_tree_2)
    y_pred_d2 = [predict_example(x, decision_tree_2) for x in Xtst]
    con_matrix_d2 = confusion_matrix(ytst, y_pred_d2)
    print("\nConfusion Matrix (Depth=2):")
    print(con_matrix_d2)

    # Call your sklearn_test function
    sklearn_test(Xtrn, ytrn, Xtst, ytst)



if __name__ == '__main__':
    # Load the training data
    M = np.genfromtxt('./monks-1.train', delimiter=',', dtype=int)
    ytrn = M[:, 0]
    Xtrn = M[:, 1:]

    # Load the test data
    M = np.genfromtxt('./monks-1.test', delimiter=',', dtype=int)
    ytst = M[:, 0]
    Xtst = M[:, 1:]


    # HERE ARE ALL THE DIFFERENT PART PLEASE RUN THEM ONE AT A TIME, RUNNING THEM ALL AT ONCE IT A BIT CONFUSING

    print("========= (PART A) =========")
    # PART A
    # ---------------------------
    #part_a_Plot(ytrn, Xtrn, ytst, Xtst)

    print()
    print()
    print()
    print()
    print()

    print("========= (PART B) =========")
    # PART B
    # ---------------------------
    # Depth = 1
    #decision_tree_1 = id3(Xtrn, ytrn, max_depth=1)
    #print("=== Decision Tree (Depth=1) ===")
    #visualize(decision_tree_1)

    # Predict on test set
    #y_pred_d1 = [predict_example(x, decision_tree_1) for x in Xtst]
    #con_matrix_d1 = confusion_matrix(ytst, y_pred_d1)
    #print("\nConfusion Matrix (Depth=1):")
    #print(con_matrix_d1)

    print()
    print()
    # ---------------------------
    # Depth = 2
    #decision_tree_2 = id3(Xtrn, ytrn, max_depth=2)
    #print("=== Decision Tree (Depth=2) ===")
    #visualize(decision_tree_2)

    # Predict on test set
    #y_pred_d2 = [predict_example(x, decision_tree_2) for x in Xtst]
    #con_matrix_d2 = confusion_matrix(ytst, y_pred_d2)
    #print("\nConfusion Matrix (Depth=2):")
    #print(con_matrix_d2)

    print()
    print()
    print()
    print()
    print()

    print("========= (PART B) =========")
    # PART C
    # ---------------------------
    #sklearn_test(Xtrn, ytrn, Xtst, ytst)

    print()
    print()
    print()
    print()
    print()

    print("========= (PART B) =========")
    # Part D
    # ---------------------------
    # breast_cancer()
