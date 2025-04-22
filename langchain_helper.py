from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.8)
    
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="Ï have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )
    
    name_chain = prompt_template_name | llm

    response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

    return response 

if __name__ == "__main__": 
    # print("Hello, World!")
    print(generate_pet_name("cat", "black"))