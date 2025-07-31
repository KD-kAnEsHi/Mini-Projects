#!/usr/bin/env python

try:
    import recordlinkage
except ModuleNotFoundError:
    # Attempt to install recordlinkage if it's missing
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-recordlinkage"])
    import recordlinkage  # Retry import

import pandas as pd
import os
from itertools import combinations
from recordlinkage.preprocessing import clean

def load_dataframes(filepaths):
    dataframes = []
    for fp in filepaths:
        try:
            if fp.endswith('.csv'):
                df = pd.read_csv(fp)
            dataframes.append(df)
            print(f"Loaded: {fp}")
        except Exception as e:
            print(f"Failed to load {fp}: {e}")
    return dataframes











def link_two_dataframes(df_left, df_right):
    """Link two DataFrames dynamically without hardcoding column names."""
    indexer = recordlinkage.Index()
    indexer.full()
    candidate_pairs = indexer.index(df_left, df_right)

    compare = recordlinkage.Compare()
    for col_left in df_left.columns:
        for col_right in df_right.columns:
            if pd.api.types.is_string_dtype(df_left[col_left]) and pd.api.types.is_string_dtype(df_right[col_right]):
                compare.string(col_left, col_right, method='levenshtein', label=f"cmp_{col_left}_{col_right}")
            elif pd.api.types.is_numeric_dtype(df_left[col_left]) and pd.api.types.is_numeric_dtype(df_right[col_right]):
                compare.numeric(col_left, col_right, method='gauss', scale=0.1, label=f"cmp_{col_left}_{col_right}")

    features = compare.compute(candidate_pairs, df_left, df_right)
    # Convert similarity scores to 0/1 for ECM
    features = (features > 0.5).astype(int)

    ecm = recordlinkage.ECMClassifier()
    ecm.fit(features)
    predictions = ecm.predict(features)
    matched_index = features.index[predictions == 1]

    return matched_index, features









def link_many_dataframes(dfs):
    """Link multiple DataFrames iteratively."""
    if len(dfs) < 2:
        raise ValueError("At least two datasets are required for linkage.")

    results = pd.DataFrame()
    for df1, df2 in combinations(dfs, 2):
        matched_index, features = link_two_dataframes(df1, df2)

        matches_left = df1.loc[matched_index.get_level_values(0)]
        matches_right = df2.loc[matched_index.get_level_values(1)]

        # Add suffixes to avoid duplicate column names
        combined_matches = pd.concat([
            matches_left.reset_index(drop=True).add_suffix("_left"),
            matches_right.reset_index(drop=True).add_suffix("_right")
        ], axis=1)

        results = pd.concat([results, combined_matches], ignore_index=True)

    return results

if __name__ == "__main__":
    folder_path = "/Users/kazangue/CS-Files/Projects-Work/Leidos-Files/test_folders"
    all_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith((".csv", ".xlsx", ".parquet"))
    ]

    dataframes = load_dataframes(all_files)
    if len(dataframes) < 2:
        print("Insufficient datasets for linkage.")
    else:
        cleaned_dataframes = clean_all_dataframes(dataframes)
        pattern_result_table = link_many_dataframes(cleaned_dataframes)
        print("Linked Data:")
        print(pattern_result_table.head())
