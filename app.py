import streamlit as st 
from langchain_openai import ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from prompts import system_prompt, user_prompt

# Constants
PAGE_TITLE = "Recipe AI"
PAGE_ICON = "🍲"
OPENAI_MODEL_NAME = "gpt-4"
OPENAI_API_KEY_PROMPT = 'OpenAI API Key'



# Set page config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="collapsed")
st.header("",divider='orange')
st.title(f"🍲 :orange[_{PAGE_TITLE}_] | Easy-to-make recipes")
st.header("",divider='orange')

# Get OpenAI API key
openai_api_key = st.sidebar.text_input(OPENAI_API_KEY_PROMPT, type='password')

if not openai_api_key.startswith('sk-'):
    st.info("Please add your OpenAI API key in the sidebar to continue.")
    st.stop()

with st.sidebar:
        
    st.divider()
    
    st.write('*Your cooking adventure begins with whatever ingredients you have readily available.*')
    st.caption('''**That's why I'd love for you to list the ingredients. 
               Once we have it, we'll understand it and start exploring it.
                Then, we'll work together to and come up with the best possible recipe, which is to prepare.  
                Sounds fun, right?**
    ''')

    st.divider()


# Form inputs
with st.form("cooking_list"):

    ingredients_input = st.text_input(
            "What do we have with us?",
            placeholder= "Blueberries, oats, milk, honey, walnuts",
        )

    kitchen_appliance = st.radio(
        "What is your favorite kitchen appliance?",
        ["Oven", "Microwave", "Toaster", "Food processor", "Blender", "Air Fryer", "Pressure Cooker", "Cooktop"],
        index=0,
    )
    st.write('Current ingredients are:', ingredients_input)
    st.write("And you would like to use ", kitchen_appliance)
    
    submitted = st.form_submit_button("Give me a recipe!")



if submitted: 
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt)
    human_message_prompt = HumanMessagePromptTemplate.from_template(user_prompt)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    request = chat_prompt.format_prompt(ingredients=ingredients_input, helper=kitchen_appliance).to_messages()

    st.divider()
    
    st.subheader("Recipe: ")
    with st.spinner('Please wait...'):
        chat = ChatOpenAI(model_name=OPENAI_MODEL_NAME, temperature=0.5, openai_api_key=openai_api_key)

        result = chat(request)

        st.write(result.content)
        st.divider()