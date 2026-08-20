import pandas as pd
import json
import os


os.chdir("/home/theo/Desktop/Toxic_And_Bias_LLM/results")
files = os.listdir()
print(f"Found {len(files)} files in the directory.")
dataset = []
for file in files:
    with open(file, "r") as f:
        data = json.load(f)

    dataset += data
    df = pd.DataFrame(dataset)
    
print(f"Number of rows: {len(df)}")
df.to_csv("unified_dataset.csv", index=False)