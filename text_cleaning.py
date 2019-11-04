# Script for text cleaning


# Get tweets
df1['text']

# Word count
df1['word_count'] = df1['text'].apply(lambda x : len(str(x).split(" ")))

df1[['text','word_count']]

# Word Count Description
df1[['text', 'word_count']].describe()

# One-word tweets (usually links or tags)
df1[['text', 'word_count']][df1['word_count'] == 1].count()