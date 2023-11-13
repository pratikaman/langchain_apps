import langchain_helper as lch
import streamlit as st

st.title("petname generator")

animal_type = st.sidebar.selectbox("whats your pet type?", ("dog", "cat", "hamster", "snake", "turtle", "fish", "bird", "rabbit", "frog", 'cow', 'horse', 'bird'))


response = lch.generate_animal_name(animal_type)

st.text(response['pet_name'])