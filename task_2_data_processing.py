import json
import pandas as pd
file_name = "C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_20260409_141258.json"
with open(file_name, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {file_name}")
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates: ",len(df))
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing null values: ",len(df))
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))
df["title"] = df["title"].str.strip()
print("After stripping whitespace from titles:", len(df))
category = df.groupby("category").count()["post_id"].reset_index()
print("Stories per category: \n",category)
df.to_csv("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_clean.csv",index=False)
print(f"Saved {len(df)} rows to trends_clean.csv")