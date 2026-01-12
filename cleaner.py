import re
import pandas as pd

# 1. Load your local messy text
with open('raw_saves.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# 2. Logic: Each post seems to start with a Name and end with "Visible to everyone"
# We will split by "Visible to everyone" as it's a very unique phrase
blocks = data.split('Visible to everyone')

cleaned_list = []

for block in blocks:
    # Remove extra spaces/newlines
    lines = [l.strip() for l in block.split('\n') if l.strip()]
    
    if len(lines) >= 3:
        # Based on your debug output:
        # lines[0] is often the name (Ethan L.)
        # lines[1] or [2] is usually the Title/Headline
        
        # We'll use a simple heuristic: the longest line in the first 5 lines 
        # is usually the "Content Title" or "Headline"
        headline = max(lines[:5], key=len)
        
        cleaned_list.append({
            'Author': lines[0],
            'Headline': headline,
            'Full_Text_Snippet': " ".join(lines[2:6]) # Captures the body text
        })

# 3. Create DataFrame
df = pd.DataFrame(cleaned_list)

# 4. Filter out any empty rows
df = df[df['Headline'].str.len() > 10]

# 5. Export
df.to_csv('my_linkedin_learning_data.csv', index=False)
print(f"Success! Structured {len(df)} professional items into your local CSV.")