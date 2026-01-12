import pandas as pd
from textblob import TextBlob

# 1. Load data
df = pd.read_csv('my_linkedin_learning_data.csv')

# 2. Define a function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    return analysis.sentiment.polarity

# 3. Apply the model to your data
df['Sentiment_Score'] = df['Headline'].apply(get_sentiment)

# 4. Categorize the score
def categorize_score(score):
    if score > 0.1: return 'Positive/Motivational'
    elif score < -0.1: return 'Critical/Problem-Solving'
    else: return 'Neutral/Technical'

df['Tone'] = df['Sentiment_Score'].apply(categorize_score)

# 5. Show Results
print("\n--- SENTIMENT PROFILE ---")
print(df['Tone'].value_counts())

# 6. Save updated data
df.to_csv('linkedin_with_sentiment.csv', index=False)
print("\nSuccess! Sentiment data saved to 'linkedin_with_sentiment.csv'.")
