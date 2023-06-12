# Import necessary libraries
import language_tool_python
import requests
import csv
import os
from keys import guardian_key
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from gpt_parody import gpt_headline
from name_swap import replace_names
from sentiment_flip import flip_sentiment
from tweet import post_tweet

# Initialize LanguageTool object for grammar checking
tool = language_tool_python.LanguageTool('en-US')
sia = SentimentIntensityAnalyzer()

if not os.path.isfile('processed_headlines.csv'):
    with open('processed_headlines.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Headline", "URL"])

processed_headlines = []

with open('processed_headlines.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        processed_headlines.append(row[0])


# Define the section IDs of the categories you're interested in
sections = ['us-news', 'politics', 'business', 'environment', 'world', 'uk-news']
# Create an empty list to store headlines, section names, and URLs together
headlines = []

# Get most recent headline from each section
for section in sections:
    response = requests.get('https://content.guardianapis.com/search',
                            params={'api-key': guardian_key,
                                    'section': section,
                                    'show-fields': 'headline,shortUrl',
                                    'page-size': 1,
                                    'order-by': 'newest'})
    data = response.json()

    for item in data['response']['results']:
        # Store the headline, section, and URL in a tuple and add it to the list
        if item['fields']['headline'] not in processed_headlines:
            headlines.append((item['fields']['headline'], section, item['fields']['shortUrl']))

print(headlines)


# Score the parody
def score_news_parody(original, parody):
    # Compute n-gram overlap
    original_ngrams = set(ngrams(word_tokenize(original), 2))
    parody_ngrams = set(ngrams(word_tokenize(parody), 2))

    union_ngrams = original_ngrams | parody_ngrams

    if len(union_ngrams) == 0:
        return 0

    overlap = len(original_ngrams & parody_ngrams) / len(union_ngrams)

    # Compute sentiment difference
    original_sentiment = sia.polarity_scores(original)['compound']
    parody_sentiment = sia.polarity_scores(parody)['compound']
    sentiment_diff = abs(original_sentiment - parody_sentiment)

    return (sentiment_diff - overlap)


for headline, section_name, url in headlines:
    methods = [replace_names, flip_sentiment, gpt_headline]

    best_score = float('-inf')
    best_parody = None

    for method in methods:
        parody = method(headline, section_name)
        score = score_news_parody(headline, parody)

        if score > best_score:
            best_score = score
            best_parody = parody

    print(f"Original: {headline}")
    print(f"Best Parody: {best_parody}\n")

    # Tweet out the parody.
    post_tweet(best_parody, url)

    with open('processed_headlines.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([headline, url])
