import pandas as pd
import json

def male_default_ratio(experiments:pd.DataFrame):
    pass 


def stereotype_index(experiments:pd.DataFrame):
    pass 


def inclusivity_score(experiments: pd.DataFrame):
    pass

if __name__=="__main__":
    with open("/home/theo/Desktop/Toxic_And_Bias_LLM/results/deepseek_v4_flash_greek_gender_bias_results.json", 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    print(df.head())