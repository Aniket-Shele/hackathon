import pandas as pd
import os

def clean_data():
    raw_file = "nsl_kdd_dataset.csv"
    output_file = "cleaned_data.csv"

    if not os.path.exists(raw_file):
        print(f"❌ Error: The file '{raw_file}' was not found in this folder.")
        print("   Please make sure you downloaded 'nsl_kdd_dataset.csv' and put it here.")
        return

    print(f"🧹 Reading raw data from '{raw_file}'...")
    df = pd.read_csv(raw_file)

    if 'label' in df.columns:
        print("⚙️  Processing labels...")
        df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
    
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Created '{output_file}' with {len(df)} rows.")

if __name__ == "__main__":
    clean_data()