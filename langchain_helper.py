"""
Defines functions to produce desired LLM generated responses.
"""
import os

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from secret_key import open_ai_key

os.environ['OPENAI_API_KEY'] = open_ai_key


def generate_restaurant_name_and_items(cuisine):
    """
    Uses LLM to generate a Restaurant name and a menu given a cuisine.
    """
    
    llm = OpenAI(temperature=0.6)

    # Creating chain 1:
    restaurant_name_chain = (
        PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. Suggest a fancy name for it. \
        Return only the restaurant name."
        )
        | llm
        | StrOutputParser()
    )

    # Chain 2:
    menu_items_chain = (
        {"restaurant_name": restaurant_name_chain} # Output of chain 1.
        | PromptTemplate.from_template(
            "Suggest some menu items for {restaurant_name}. Return the menu \
                items separated only by a coma do not use indentations."
            ) # Propmt 2 that calls for chain 1 response.
        | llm
        | {"menu_items": StrOutputParser(),
        "restaurant_name": restaurant_name_chain}
    )

    return menu_items_chain.invoke({"cuisine": cuisine})