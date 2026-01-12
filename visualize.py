import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the summary data
try:
    df = pd.read_csv('category_summary.csv')
except FileNotFoundError:
    print("Error: category_summary.csv not found. Run analysis.py first!")
    exit()

# 2. Set up the professional style
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Count'], color='#0077b5') # LinkedIn Blue color

# 3. Add Labels and Title
plt.title('LinkedIn Saved Content: Professional Category Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Skill Category', fontsize=12)
plt.ylabel('Number of Mentions', fontsize=12)
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Save the plot as an image for your GitHub README
plt.tight_layout()
plt.savefig('category_chart.png')
print("Success! Created 'category_chart.png'. Open it to see your data story.")
plt.show()
