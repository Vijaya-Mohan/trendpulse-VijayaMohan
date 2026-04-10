import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

file_name = "C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_analysed.csv"

df = pd.read_csv(file_name)

os.makedirs("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\outputs", exist_ok=True)
top_stories = df.nlargest(10, "score")[["title", "score"]]

top_stories["short_title"] = top_stories["title"].apply(lambda x: x[:50] + "…" if len(x) > 50 else x)
plt.figure(figsize=(10, 6))
plt.barh(top_stories["short_title"], top_stories["score"], color="skyblue")
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\outputs\\top_stories.png")
plt.show()
category_counts = df.groupby("category")["post_id"].count().reset_index(name="count")
colors = plt.cm.tab20(np.linspace(0, 1, len(category_counts)))
plt.figure(figsize=(10, 6))
plt.bar(category_counts["category"], category_counts["count"], color = colors)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.tight_layout()
plt.savefig("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\outputs\\chart2_categories.png")
plt.show()

popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

plt.figure(figsize=(10, 6))
plt.scatter(popular["score"], popular["num_comments"], color="green", label="Popular", alpha=0.6)
plt.scatter(non_popular["score"], non_popular["num_comments"], color="red", label="Non-Popular", alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\outputs\\chart3_scatter.png")
plt.show()
plt.subplots(1,3, figsize=(18, 5))
plt.subplot(1, 3, 1)
plt.barh(top_stories["short_title"], top_stories["score"], color="skyblue")
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.subplot(1, 3, 2)
plt.bar(category_counts["category"], category_counts["count"], color = colors)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.subplot(1, 3, 3)
plt.scatter(popular["score"], popular["num_comments"], color="green", label="Popular", alpha=0.6)
plt.scatter(non_popular["score"], non_popular["num_comments"], color="red", label="Non-Popular", alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("TrendPulse Dashboard", fontsize=16)
plt.savefig("C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\outputs\\dashboard.png")

plt.show()