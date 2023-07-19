# generate key value pairs using single query

# make dictionary of the output from description

# importing libraries and specifying api key
import os
import json
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
        self.description = None 

    def response1(self,query1):
        response1 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query1,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.1,)
        return response1.choices[0].text



def main():
    #creating instance
    generate_keywords = keyVal()
    product = input("Enter product: ")
    description = input("\nenter description of product: ")
    # Generating keywords from product type
    query = f"""Generate specification name and its values in dictionary format for specfications of a :{product} from its :{description}."""
    
    output = generate_keywords.response1(query)

    import json
    # Parse JSON from a strin
    json_str = output
    data = json.loads(json_str)
    print(data) 

    return print("\n",output)

    

if __name__ == "__main__":
    main()
