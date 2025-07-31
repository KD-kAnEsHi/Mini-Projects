import recordlinkage
import pandas as pd
import os
from recordlinkage.datasets import load_febrl4
from recordlinkage.preprocessing import clean, phonetic
from recordlinkage.index import Block

def load_dataframes(filepaths):
    dataframes = {}  
    for fp in filepaths:
        try:
            if fp.endswith('.csv'):
                df = pd.read_csv(fp)
                filename = os.path.basename(fp)     # Using file name as a key, maybe change later
                dataframes[filename] = df           
                print(f"Successfully loaded: {filename}")
            else:
                print(f"Unsupported file format: {fp}")
                continue  
        except Exception as e:
            print(f"Failed to load {fp}: {e}")
    
    if not dataframes:
        print("No dataframes were loaded. Please check your file paths and formats.")
    return dataframes


def record_linkage(df1, df2):
    df1_str = df1.astype(str)
    df2_str = df2.astype(str)
    
    indexer = recordlinkage.Index()
    try:
        indexer.block(left_on=df1_str.columns[0], right_on=df2_str.columns[0])
        candidate_links = indexer.index(df1_str, df2_str)
    except Exception as e:
        print(f"Error during indexing: {e}")
        return None

    compare_st = recordlinkage.Compare()
    for col1 in df1_str.columns:
        for col2 in df2_str.columns:
            try:
                compare_st.string(col1, col2, method="jarowinkler", 
                                threshold=0.85, label=f"{col1}-{col2}")
            except Exception as e:
                print(f"Error adding comparison for {col1}-{col2}: {e}")
                continue

    try:
        features = compare_st.compute(candidate_links, df1_str, df2_str)
        return features
    except Exception as e:
        print(f"Error computing features: {e}")
        return None


def link_datasets(dataframes):
    if not dataframes:
        print("No dataframes to process")
        return

    keys = list(dataframes.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            df1 = dataframes[keys[i]]
            df2 = dataframes[keys[j]]
            print(f"\nPerforming linkage between {keys[i]} and {keys[j]}")
            
            features = record_linkage(df1, df2)
            if features is not None:
                print("\nLinkage Results:")
                print(features.head(10)) 
            else:
                print("Linkage failed")

if __name__ == "__main__":
    folder_path = "/Users/kazangue/CS-Files/Projects-Work/Leidos-Files/test_folders"
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".csv")]
    
    dataframes = load_dataframes(all_files)
    link_datasets(dataframes)

