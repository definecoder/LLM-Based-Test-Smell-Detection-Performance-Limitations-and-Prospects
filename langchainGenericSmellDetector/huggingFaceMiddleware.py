import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFacePipeline
from smells import getAllSmellsInASingleString
from typing import List, Optional
from pydantic import BaseModel, Field

load_dotenv()

# class DetectedSmell(BaseModel):
#     smellName: str
#     reason: str
    
gemini_api_key = os.getenv("GEMINI_API_KEY")
    
class DetectedSmells(BaseModel):
    smellNames: List[str] = Field(description="List of detected smells")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b",
    api_key=gemini_api_key,
)

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-7b",
#     task="text-generation",
#     temperature=0.01,
#     huggingfacehub_api_token="",
# )

# llm = HuggingFacePipeline.from_model_id(
#     model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
#     task="text-generation",
#     pipeline_kwargs={"max_new_tokens": 512}    
# )

structured_llm = llm.with_structured_output(DetectedSmells)

all_smells = getAllSmellsInASingleString()

def smellSirializer(found_smells_in_natural_language: str) -> list[str]:

    message = [
        SystemMessage(
            "You are an expert in making test smells list from natural language format. You will be given a natual language report of which smells are in a test code block, you have to reuturn a array containing the name of the test smells found in the text block. Here is the list of test smells: " + all_smells
        ),
        HumanMessage("Here is the List of found test smells in natutal language :" + found_smells_in_natural_language + ". Please return the list of test smells found in the text block in array format."),
    ]

    response = structured_llm.invoke(message)        
    
    return response.smellNames

if __name__ == "__main__":
    smells_natual_lang = """
        .
    :The provided test code block contains the following test smells:

    1. **Assertion Roulette**: The test method `realCase` contains multiple assertions without a descriptive message for each assertion. This makes it difficult to understand which specific assertion failed if the test fails.

    2. **Eager Test**: The test method `realCase` invokes several methods of the production object `Abriss` (e.g., `removeDAO`, `add`, `compute`, `getResults`, `getMean`, `getMSE`, `getMeanErrComp`). This makes the test harder to comprehend and maintain.

    3. **Magic Number Test**: The test method `realCase` contains numeric literals (magic numbers) as parameters in the assertions. These numbers do not indicate the meaning/purpose of the number, and they should be replaced with constants or variables.

    4. **Exception Handling**: The test method `realCase` contains a try-catch block to handle `CalculationException`. Instead of custom exception handling, JUnit's exception handling should be used to automatically pass/fail the test.

    5. **Sensitive Equality**: The test method `realCase` uses `this.df4.format()` and `this.df1.format()` to format the results before comparing them with expected values. This can lead to issues if the formatting logic changes, making the test fragile.

    Here is a summary of the identified test smells:
    - Assertion Roulette
    - Eager Test
    - Magic Number Test
    - Exception Handling
    - Sensitive Equality
    """    

    res = smellSirializer(smells_natual_lang)
    
    print(res)
    print(type(res))