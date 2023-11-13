from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType

 
load_dotenv()

def generate_animal_name(animal_type):
    llm  = OpenAI(temperature=0.8)

    prompt = PromptTemplate(
        input_variables=['animal_type'],
        template= "I have a {animal_type}. I want a sexy name for it. Suggest me 5 names for him. The first letter of each name should start with first letter of {animal_type}"
    )
    
    name = LLMChain(llm=llm, prompt=prompt, output_key="pet_name")

    response = name({'animal_type': animal_type})

    return response

    # prompt = "I have a dog. I want a sexy name for it. Suggest me 5 names for him."
    # name = llm(prompt)
    # return name


def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(['wikipedia', 'llm-math'], llm=llm)


    agent = initialize_agent(llm=llm, tools=tools, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  

    result = agent.run("what is the average age of a dog? Multiply the age by 3")

    print(result)


def main():
    # animal = input("Enter animal type: ").strip()
    # print(generate_animal_name(animal))
 
    langchain_agent()

if __name__ == "__main__":
    main()