from pathlib import Path
import streamlit as st
from streamlit_chat import message
from hugchat import hugchat
from hugchat.login import Login
#from streamlit_extras.colored_header import colored_header
#from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="AI Chatbot 100% Free")
st.title('完全开源免费的AI智能聊天助手 | Absolute Free & Opensouce AI Chatbot')
#st.write('🤗💬Absolute Free & Opensouce AI Chatbot: HugChat - DataProf & chatMATE/VishnuSivan')

# --- PATH SETTINGS ---
css_file = "main.css"
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

  # Function for generating LLM response
def generate_response(prompt_input):
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    return chatbot.chat(prompt_input)

# User-provided prompt
if prompt := st.chat_input(): 
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

  # Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
