# generate key value pairs using two queries

# make dictionary of the output from description

# importing libraries and specifying api key
import os
import openai
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
openai.api_type = "azure"
openai.api_version = "2023-05-15" 

# Your Azure OpenAI resource's endpoint value.
openai.api_base = os.getenv("API_BASE") 
openai.api_key = os.getenv("API_KEY")


# creating class for functions
class keyVal:

    def __init__(self):
        self.product = None
        self.keywords = None
        self.description = None 

    def response1(self,query1):
        response1 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query1,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.1,)
        return response1.choices[0].text.strip()

    def response2(self,query2):
        response2 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query2,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.1,)
    
        return response2.choices[0]



def main():
    #creating instance
    generate_keywords = keyVal()
    product = input("Enter product: ")
    # Generating keywords from product type
    query1 = f"""Generate keywords for specification of a product:{product}.
    Some sample keywords are product type, weight, cost, dimensions, color
    whereas other keywords may vary depending on what the product is."""
    
    keywords = generate_keywords.response1(query1)

    description = input("enter description of product: ")

    # Generating values for the keywords from the description provided in the input
    query2 = f"""use the keywords:{keywords} to create key value pair in dictionary format
    where relevant values can be found in description:{description}."""
    
    output = generate_keywords.response2(query2)

    return print(output)

    

if __name__ == "__main__":
    main()
