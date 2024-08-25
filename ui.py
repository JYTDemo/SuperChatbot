import streamlit as st
import os

model_list=['AWS','Azure','Gemini','Ollama']

with st.sidebar:
    st.title("Config")
    temperature = st.slider("Model temperature", 0.00, 1.00, 0.00,0.01)
    model_select = st.radio(
        "**Choose the model**",
        model_list
    )

st.title("Unified LLM Chat")

if model_select == 'AWS':
    import aws_main as main
if model_select == 'Azure':
    import azure_main as main
if model_select == 'Gemini':
    import gemini_main as main
if model_select == 'Ollama':
    import ollama_main as main

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == 'user':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if message["role"] == 'assistant':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = main.LLM_QnA_agent(prompt,temperature)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        #st.markdown(response)
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
