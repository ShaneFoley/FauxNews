import nltk
import random

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms


def flip_sentiment(headline, section):
    # Ensure the headline is a string
    if not isinstance(headline, str):
        print("Error: headline is not a string")
        return headline

    # Tokenize the headline
    tokenized = nltk.word_tokenize(headline)

    # POS tagging
    tagged = nltk.pos_tag(tokenized)
    new_words = []

    for word, tag in tagged:
        # Try to find an antonym for adjectives (POS tag 'J'), adverbs (POS tag 'R'), and now verbs (POS tag 'V')
        if tag.startswith('J') or tag.startswith('R') or tag.startswith('V'):
            # Check if the word has a strong sentiment
            if abs(sia.polarity_scores(word)['compound']) > 0.5:
                # Try to find an antonym for the word
                antonyms = get_antonyms(word)
                if antonyms:
                    # Randomly choose one of the antonyms
                    new_word = random.choice(antonyms)
                    new_words.append(new_word)
                else:
                    new_words.append(word)
            else:
                new_words.append(word)
        else:
            new_words.append(word)

    new_headline = ' '.join(new_words)
    print("flip sentiment: " + new_headline)
    return new_headline
