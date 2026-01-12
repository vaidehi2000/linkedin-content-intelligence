import pandas as pd

# 1. Load the data
df = pd.read_csv('my_linkedin_learning_data.csv')
all_text = " ".join(df['Headline'].astype(str)).lower()

# 2. Define "Skill Buckets" 
categories = {
    'Technical Skills': ['python', 'sql', 'java', 'android', 'software', 'coding'],
    'Data & AI': ['data', 'ai', 'machine learning', 'analytics', 'intelligence'],
    'Career Level': ['internship', 'entry', 'junior', 'associate', 'hiring'],
    'Education': ['university', 'student', 'college', 'degree', 'learning']
}

# 3. Process and Print
print("\n--- CATEGORY BREAKDOWN ---")
results = {}
for category, keywords in categories.items():
    count = sum(all_text.count(word) for word in keywords)
    results[category] = count
    print(f"{category.upper()}: {count} mentions")

# 4. Save results for the next stage (Visualization)
summary_df = pd.DataFrame(list(results.items()), columns=['Category', 'Count'])
summary_df.to_csv('category_summary.csv', index=False)