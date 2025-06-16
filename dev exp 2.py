import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')

df = pd.read_csv("C:\\Users\\ROHITH\\Downloads\\spam (1).csv", encoding='latin-1')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='label', palette='Set2')
plt.title('Distribution of Spam vs Ham')
plt.show()
print(df['label'].value_counts(normalize=True))

df['message_length'] = df['message'].apply(len)
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='message_length', hue='label', bins=50, kde=True, palette='Set1')
plt.title('Distribution of Message Lengths')
plt.xlabel('Message Length')
plt.ylabel('Count')
plt.show()

def preprocess_text(text):
    text = text.lower()
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return words

df['tokens'] = df['message'].apply(preprocess_text)

spam_words = df[df['label']=='spam']['tokens'].sum()
ham_words = df[df['label']=='ham']['tokens'].sum()

spam_wc = WordCloud(width=600, height=400, background_color='black').generate(' '.join(spam_words))
plt.figure(figsize=(8, 5))
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Spam Word Cloud')
plt.show()

ham_wc = WordCloud(width=600, height=400, background_color='white', colormap='viridis').generate(' '.join(ham_words))
plt.figure(figsize=(8, 5))
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Ham Word Cloud')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='label', y='message_length', data=df)
plt.title('Message Length by Class')
plt.show()

print("Average Message Length (Overall):", df['message_length'].mean())
print("Average Message Length (Spam):", df[df['label'] == 'spam']['message_length'].mean())
print("Average Message Length (Ham):", df[df['label'] == 'ham']['message_length'].mean())

q1 = df['message_length'].quantile(0.25)
q3 = df['message_length'].quantile(0.75)
iqr = q3 - q1
outlier_limit = q3 + 1.5 * iqr
outliers = df[df['message_length'] > outlier_limit]
print(f"Number of outlier messages (length > {outlier_limit:.2f}):", outliers.shape[0])
