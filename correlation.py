import pandas as pd

# 1. Load the data
df = pd.read_csv('linkedin_with_sentiment.csv')

# 2. Re-apply the Category logic (The "missing link")
categories = {
    'Technical Skills': ['python', 'sql', 'java', 'android', 'software', 'coding'],
    'Data & AI': ['data', 'ai', 'machine learning', 'analytics', 'intelligence'],
    'Career Level': ['internship', 'entry', 'junior', 'associate', 'hiring'],
    'Education': ['university', 'student', 'college', 'degree', 'learning']
}

def assign_category(text):
    text = str(text).lower()
    for cat, keywords in categories.items():
        if any(word in text for word in keywords):
            return cat
    return 'General/Other'

df['Category'] = df['Headline'].apply(assign_category)

print("\n--- DATA VALIDATION: AVERAGE SCORE BY TONE ---")
print(df.groupby('Tone')['Sentiment_Score'].mean())

print("\n--- THE 'INTELLIGENCE' PIECE (Cross-Tabulation) ---")
# This creates a "Heatmap" of your professional interests vs. their sentiment
intelligence_pivot = pd.crosstab(df['Category'], df['Tone'])
print(intelligence_pivot)

# 3. Save the final integrated dataset
df.to_csv('final_enriched_data.csv', index=False)
print("\nSuccess! Final report saved to 'final_enriched_data.csv'.")