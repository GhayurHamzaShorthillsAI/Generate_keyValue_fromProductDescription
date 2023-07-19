# keys from product
# Generate keys from product

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
        

    def response1(self,query1):
        response1 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query1,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0,)
        return response1.choices[0]
    

if __name__ == "__main__":
    #creating instance
    generate_keywords = keyVal()
    product = input("Enter product: ")
   
    # #Generating keywords from product type
    # query1 = f"""Generate keywords for specification of a :{product}.Omit any extra information or text or data"""
    
    # Generating keywords from product type
    query1 = f"""Generate keywords for specification of a product:{product}.
    Some sample keywords are product type, weight, cost, dimensions, color
    whereas other keywords may vary depending on what the product is."""
    keywords = generate_keywords.response1(query1)

    print(keywords)
