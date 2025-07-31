import os  # Import os for file handling
import numpy as np
import pywt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from qiskit_aer import Aer
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.algorithms import QSVM
from sklearn.ensemble import RandomForestClassifier


# This functiosn load '.eea' files from a folder and assign labels.
def load_eea_files(folder_path, label):
    data = []
    labels = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".eea"):
            file_path = os.path.join(folder_path, filename)
            # Load the file as a NumPy array (adjust if needed based on .eea format)
            eeg_data = np.loadtxt(file_path)
            data.append(eeg_data)
            labels.append(label)
    
    return data, labels




# Load data from both folders and label them
schizophrenia_folder = "/Users/kazangue/CS-Files/Projects-Clubs/Research - QSMV/Demo_degroot/Schizophrenia - QSVM/Adolescents with Symptoms of Schizophrenia"
normal_folder = "/Users/kazangue/CS-Files/Projects-Clubs/Research - QSMV/Demo_degroot/Schizophrenia - QSVM/Adolescents"

schizophrenia_data, schizophrenia_labels = load_eea_files(schizophrenia_folder, label=1)  # Label 1 for schizophrenia
normal_data, normal_labels = load_eea_files(normal_folder, label=0)  # Label 0 for normal

# Combine data and labels
all_data = np.concatenate((schizophrenia_data, normal_data), axis=0)
all_labels = np.concatenate((schizophrenia_labels, normal_labels), axis=0)




# apply the 'Discrete Wavelet Transform (DWT) to EEG signals and extract statitical feature for the DWT coefficients.
def apply_dwt(signal):
    coeffs = pywt.wavedec(signal, 'db2', level=4)
    return coeffs

def extract_features(dwt_coeffs):
    features = []
    for coeff in dwt_coeffs:
        features.append(np.mean(coeff))
        features.append(np.var(coeff))
        features.append(np.std(coeff))
        # I will add more statistical features later (entropy)
    return features




# Apply DWT and extract features for each EEG sample
all_features = []
for sample in all_data:
    dwt_coeffs = apply_dwt(sample)
    sample_features = extract_features(dwt_coeffs)
    all_features.append(sample_features)
# Convert the lists into a NumPy array for further processing
all_features = np.array(all_features)




# Reduce dimensions using PCA
pca = PCA(n_components=10)                                  # Let adjest this later
reduced_data = pca.fit_transform(all_features)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(reduced_data, all_labels, test_size=0.3, random_state=42)
# Define a ZZ Feature Map with appropriate qubits and repetitions
feature_map = ZZFeatureMap(feature_dimension=10, reps=2)





# Set up quantum instance with simulator backend
backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend)
qsvm = QSVM(feature_map=feature_map)                        # Initialize QSVM with feature map
qsvm.fit(X_train, y_train)                                  # Train QSVM on training data
predictions = qsvm.predict(X_test)                          # Make predictions on test data


# Evaluate performance using accuracy score and other metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print(f"QSVM Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")



#RUNNIG THE MODEL ON A CLASSICAL ML MODEL
# Train Random Forest classifier on reduced data as comparison model
clf_rf = RandomForestClassifier()
clf_rf.fit(X_train, y_train)

# Predict and evaluate performance on test data using Random Forest
rf_predictions = clf_rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print(f"Random Forest Accuracy: {rf_accuracy}")