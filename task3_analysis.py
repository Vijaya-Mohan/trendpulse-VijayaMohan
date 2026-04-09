import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_clean.csv")
print("Loaded data:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("Average score:", df["score"].mean().round(2))
print("Average comments:", df["num_comments"].mean().round(2))
mean_scores = np.mean(df["score"])
median_scores = np.median(df["score"])
standard_deviation_scores = np.std(df["score"])
max_scores = np.max(df["score"])
min_scores = np.min(df["score"])
print("\n--- NumPy Stats ---")
print(f"\nMean Score: {mean_scores:.2f}\nMedian Score: {median_scores:.2f}\nStandard Deviation: {standard_deviation_scores:.2f}\nMax Score: {max_scores}\nMin Score: {min_scores}")

unique_categories, counts = np.unique(df["category"], return_counts=True)
most_common_category = unique_categories[np.argmax(counts)]
print(f"\nMost stories in: {most_common_category} with {np.max(counts)} stories")
max_comments = np.max(df["num_comments"])
indices = np.where(df["num_comments"] == max_comments)
most_commented_stories = df.iloc[indices]
print("\nStories with the most comments:\n", most_commented_stories)
df["engagement"] = (df["num_comments"])/(df["score"] + 1)
print(df.head())
df["is_popular"] = df["score"]> df["score"].mean()
print(df.head())
df.to_csv("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_analysed.csv",index=False)
print(f"Saved {len(df)} rows to trends_analysed.csv")
