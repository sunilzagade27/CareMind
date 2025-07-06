import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello! How can I assist you today?👋")
    
prompt = st.chat_input("Type your message here...")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    
    # Simulate a response
    response = f"You said: {prompt}. Here's a random number for you: {np.random.randint(1, 100)}"
    
    with st.chat_message("assistant"):
        st.write(response)