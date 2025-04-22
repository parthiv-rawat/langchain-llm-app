import openai
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv

# load_dotenv()
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.8)
    
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="Ï have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )
    
    name_chain = prompt_template_name | llm

    response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

    return response 

def langchain_agent():
    llm = OpenAI(temperature=0.6)
    
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    
    query = (
    "Use the Wikipedia tool to find the average lifespan of a dog in years. "
    "Extract only the numeric value. Then multiply that number by 4 using the calculator tool. "
    "Return only the result of the multiplication."
    )
    
    # result = agent.run(
    #     "What is the average age of a dog? Multiply the age by 4"
    # )
    
    result = agent.invoke(query)
    return result 
    # print(result)

if __name__ == "__main__": 
    # print("Hello, World!")
    # print(generate_pet_name("cat", "black"))
    langchain_agent()