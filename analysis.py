import pandas as pd
from collections import Counter
import re

# 1. Load the data you cleaned
df = pd.read_csv('my_linkedin_learning_data.csv')

# 2. Combine all headlines into one big string
all_text = " ".join(df['Headline'].astype(str)).lower()

# 3. Use Regex to find words (Filter out common words like 'the', 'and', 'is')
words = re.findall(r'\w+', all_text)
stop_words = {'the', 'and', 'to', 'in', 'is', 'for', 'of', 'on', 'with', 'a', 'we', 'i', 'how', 'at'}
interesting_words = [w for w in words if w not in stop_words and len(w) > 2]

# 4. Count the top 10 most frequent keywords
word_counts = Counter(interesting_words)
print("\n--- YOUR TOP 10 PROFESSIONAL INTERESTS ---")
for word, count in word_counts.most_common(10):
    print(f"{word.upper()}: {count} mentions")

# 5. Save the results to a small summary file
summary = pd.DataFrame(word_counts.most_common(20), columns=['Keyword', 'Count'])
summary.to_csv('skill_summary.csv', index=False)

# 6. Check for specific "Target Skills"
target_skills = ['python', 'data', 'ai', 'internship', 'software', 'engineer', 'learning', 'university']
print("\n--- TARGET SKILL TRACKER ---")
for skill in target_skills:
    count = all_text.count(skill)
    print(f"{skill.upper()}: {count} mentions")
