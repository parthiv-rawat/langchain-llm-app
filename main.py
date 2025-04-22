import langchain_helper as lch
import streamlit as st 


st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster", "Fish"))

if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area("What color is your cat?", max_chars=15)
    
if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area("What color is your dog?", max_chars=15)
    
if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area("What color is your cow?", max_chars=15)
    
if user_animal_type == "Fish":
    user_pet_color = st.sidebar.text_area("What color is your fish?", max_chars=15)
    
if user_animal_type == "Hamster":
    user_pet_color = st.sidebar.text_area("What color is your hamster?", max_chars=15)
    
    
if user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(response)
    
if st.button("Run Agent Math Test"):
    agent_response = lch.langchain_agent()
    st.text(agent_response)