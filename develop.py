"""
AI Developer Analytics Dashboard
Author: shahina
Description: Analyzes developer skills and visualizes performance
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Create Dataset ---
data = {
    "name": ["Bharat", "Rahul", "Priya", "Anil", "Sneha"],
    "role": ["AI Developer", "AI Developer", "Data Analyst", "ML Engineer", "AI Developer"],
    "python": [85, 92, 75, 88, 79],
    "sql": [90, 85, 95, 80, 82],
    "ml": [78, 90, 65, 94, 85],
    "ai": [88, 94, 70, 91, 89],
    "experience": [2, 3, 1, 4, 2]
}
df = pd.DataFrame(data)
df.to_csv("developers.csv", index=False)

# --- Step 2: Calculate Average & Level ---
df = pd.read_csv("developers.csv")
df["average"] = df[["python", "sql", "ml", "ai"]].mean(axis=1)

def get_level(score):
    if score >= 85:
        return "Advanced"
    elif score >= 70:
        return "Intermediate"
    else:
        return "Beginner"

df["level"] = df["average"].apply(get_level)

# --- Step 3: Visualizations - 6 Graphs in 1 Screen ---
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.bar(df["name"], df["average"], color='#4C72B0')
plt.title("Average by Developer")
plt.xticks(rotation=15)

plt.subplot(2, 3, 2)
plt.scatter(df["experience"], df["average"], color='red')
plt.title("Experience VS Average")
plt.xlabel("experience")
plt.ylabel("average")

plt.subplot(2, 3, 3)
plt.bar(df["name"], df["python"], color='blue')
plt.title("Python Score")
plt.xticks(rotation=15)

plt.subplot(2, 3, 4)
plt.bar(df["name"], df["sql"], color='orange')
plt.title("SQL Score")
plt.xticks(rotation=15)

plt.subplot(2, 3, 5)
plt.bar(df["name"], df["ml"], color='green')
plt.title("ML Score")
plt.xticks(rotation=15)

plt.subplot(2, 3, 6)
plt.bar(df["name"], df["ai"], color='purple')
plt.title("AI Score")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# --- Step 4: Min/Max Analysis ---
plt.figure(figsize=(12, 5))
min_avg, max_avg = df["average"].min(), df["average"].max()
overall_avg = df["average"].mean()
min_name = df.loc[df["average"].idxmin(), "name"]
max_name = df.loc[df["average"].idxmax(), "name"]

plt.subplot(1, 2, 1)
colors = ['red' if x == min_avg else 'green' if x == max_avg else 'skyblue' for x in df["average"]]
plt.bar(df["name"], df["average"], color=colors)
plt.title(f"Min: {min_name} ({min_avg:.1f}) | Max: {max_name} ({max_avg:.1f})")
plt.xticks(rotation=15)

plt.subplot(1, 2, 2)
plt.bar(["Minimum\n"+min_name, "Overall Avg", "Maximum\n"+max_name],
        [min_avg, overall_avg, max_avg], color=['red','blue','green'])
plt.title("Average Min vs Max vs Overall")

plt.tight_layout()
plt.show()

# --- Step 5: Final Analytics Report ---
print("\n=== AI Developer Analytics ===")
print(f"Total Developers: {len(df)}")
print(f"Average Score: {overall_avg:.2f}")
print(f"Minimum: {min_name} = {min_avg:.1f}")
print(f"Maximum: {max_name} = {max_avg:.1f}")
print(f"Top Developer: {max_name}")
print(f"\nSkill Averages: Python: {df['python'].mean():.0f} SQL: {df['sql'].mean():.0f} ML: {df['ml'].mean():.0f} AI: {df['ai'].mean():.0f}")
print("\nFull Data:")
print(df)