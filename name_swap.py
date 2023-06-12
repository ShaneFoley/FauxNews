import random
import spacy

# List of pop culture names for replacement generated with help from ChatGPT
random_name = [
    "Joe Biden", "Kim Jong Un", "The Rock", "Elon Musk", "Oprah Winfrey",
    "Donald Trump", "Tom Cruise", "Beyonce", "Barack Obama", "Taylor Swift",
    "Kanye West", "Rihanna", "Brad Pitt", "Angelina Jolie", "Bill Gates",
    "Queen Elizabeth II", "Vladimir Putin", "Justin Bieber", "Jennifer Aniston", "George Clooney",
    "Leonardo DiCaprio", "Julia Roberts", "Robert Downey Jr.", "Ellen DeGeneres", "Meryl Streep",
    "Will Smith", "Johnny Depp", "Sandra Bullock", "Nicole Kidman", "Denzel Washington",
    "Matt Damon", "Scarlett Johansson", "Natalie Portman", "Hugh Jackman", "Charlize Theron",
    "Emma Watson", "Daniel Radcliffe", "Rupert Grint", "Kristen Stewart", "Robert Pattinson",
    "Chris Hemsworth", "Chris Evans", "Chris Pratt", "Mark Ruffalo", "Jeremy Renner",
    "Benedict Cumberbatch", "Tom Hiddleston", "Paul Rudd", "Chadwick Boseman", "Anthony Mackie",
    "Sebastian Stan", "Elizabeth Olsen", "Brie Larson", "Zoe Saldana", "Dave Bautista",
    "Vin Diesel", "Dwayne Johnson", "Jason Statham", "Idris Elba", "Gal Gadot",
    "Henry Cavill", "Ben Affleck", "Jason Momoa", "Ezra Miller", "Amy Adams",
    "J.K. Rowling", "Stephen King", "George R.R. Martin", "J.R.R. Tolkien", "Agatha Christie",
    "Dan Brown", "Suzanne Collins", "J.D. Salinger", "Ernest Hemingway", "F. Scott Fitzgerald",
    "Mark Twain", "Charles Dickens", "Jane Austen", "Emily Bronte", "Virginia Woolf",
    "Albert Einstein", "Stephen Hawking", "Marie Curie", "Isaac Newton", "Galileo Galilei",
    "Thomas Edison", "Nikola Tesla", "Leonardo da Vinci", "Michelangelo", "Vincent Van Gogh",
    "Pablo Picasso", "Salvador Dali", "Frida Kahlo", "Andy Warhol", "Claude Monet",
    "Rembrandt", "Johannes Vermeer", "Edgar Degas", "Jackson Pollock", "Georgia O'Keeffe",
    "Snoop Dogg", "Coolio", "Kevin Hart", "Miss Universe", "Chuck Norris",
    "McLovin"
]

# An attempt for more relevant name selection: Using the Headline paired with The Guardian APIs 'sectionName' to select
# target specific & topical names
section_names = {
    "World news": ["Vladimir Putin", "Bernie Sanders", "Margaret Thatcher", "Winston Churchill", "Narendra Modi",
                   "Xi Jinping", "Boris Johnson", "Nicola Sturgeon", "Leo Varadkar", "Queen Elizabeth", "Joe Biden",
                   "Kim Jong Un", "Angela Merkel", "Pope Francis", "Justin Trudeau", "Emmanuel Macron", "Elon Musk",
                   "Bill Gates", "Warren Buffett", "Jeff Bezos", "Mark Zuckerberg", "Zelensky"],

    "Environment": ["Al Gore", "Greta Thunberg", "David Attenborough", "Jane Goodall", "Leonardo DiCaprio",
                    "Brad Pitt", "Angelina Jolie", "Bill Gates", "Elon Musk", "Jeremy Clarkson", "Rupert Murdoch",
                    "Koch Brothers", "Scott Pruitt", "James Inhofe", "Richard Branson", "Jeff Bezos", "Mark Zuckerberg",
                    "Jair Bolsonaro", "Vladimir Putin", "Donald Trump", "Xi Jinping", "Prince Charles",
                    "Bjorn Lomborg"],

    "US news": ["Donald Trump", "Barack Obama", "George W. Bush", "Hillary Clinton", "Bernie Sanders", "Michelle Obama",
                "Ted Cruz", "Joe Exotic", "Kim Kardashian", "Kanye West", "Elon Musk", "Oprah Winfrey", "Steve Harvey",
                "Alex Jones", "Bill Nye", "Snoop Dogg", "Dwayne 'The Rock' Johnson", "Guy Fieri", "Martha Stewart",
                "Chuck Norris", "Tom Cruise", "Britney Spears", "Betty White", "Danny DeVito", "Bill Murray"],

    "Business": ["Elon Musk", "Bill Gates", "Warren Buffett", "Jeff Bezos", "Mark Zuckerberg", "Richard Branson",
                 "Jack Ma", "Larry Page"],

    "Politics": ["Bernie Sanders", "Margaret Thatcher", "Winston Churchill", "Narendra Modi", "Xi Jinping",
                 "Boris Johnson", "Nicola Sturgeon", "Jacinda Ardern", "Leo Varadkar"]
}

# Load the language model from spacy, effective and lightweight for identifying people names
nlp = spacy.load('en_core_web_sm')
def replace_names(text, section_name):
    # Use Spacy Library to parse the text
    doc = nlp(text)

    # Get the list of replacement names for this section
    replacement_names = section_names.get(section_name, [])

    # If there are no replacement names for this section, use a default random list
    if not replacement_names:
        replacement_names = random_name

    # Replace any identified names with a random name from the list by the headlines section
    random_name_headline = text
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            random_name_headline = random_name_headline.replace(ent.text, random.choice(replacement_names))

    print("Name Swap: " + random_name_headline)
    return random_name_headline

