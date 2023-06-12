import openai
import random
from keys import gpt_key

# Load the GPT API key from keys.py file
openai.api_key = gpt_key

# To vary GPT API Output a selection of different techniques can be provided to give a different prompt
prompts = ["Wordplay", "a pun in the context of the headline", "Hyperbole", "Satire", "Absurdity", "Absurdity",
           "Absurdity", "an unexpected and unusual context", "Satire", "Satire"]

# Send a prompt to the GPT API requesting a parody headline and return the output
def gpt_headline(original_headline, section_name):
    selected_prompt = random.choice(prompts)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{original_headline}\n\nYour task: Make a parody of the above headline using {selected_prompt}."
               f" The parody headline should be a single, clear sentence, only return this parody no other "
               f"output is needed:\n",
        temperature=0.5,
        max_tokens=50
    )

    # Extract the generated text from the gpt response
    generated_headline = response.choices[0].text.strip()
    generated_headline = generated_headline.strip('"')
    print("GPT Output: " + generated_headline)

    return generated_headline
