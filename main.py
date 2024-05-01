"""
Creates a web application that given a chosen cuisine by the user,
uses a LLM model to generate a Restaurant name and a suggested menu.
"""
import re
import streamlit as st
import langchain_helper

st.title("Restaurant Name and Menu Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",
                     ("Indian", "Italian", "Mexican",
                      "Spanish", "American"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(".")
    st.write("**Menu Items**")
    for item in menu_items[1:-1]:
        st.write("-", re.sub(r'\n\d+\n?', '', item))
