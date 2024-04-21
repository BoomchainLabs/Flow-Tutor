import os
import time
import random
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

st.set_page_config(
    page_title="Flow Tutor",
    page_icon="🎓",
    menu_items={
        "About": "### Flow Tutor\nAn easy and fast way to generate and understand Flow blockchain contracts with AI.",
    },
    layout="wide",
)

# st.sidebar.image(
#     "flow_logo.png", width=200
# )  # Replace 'flow_logo.png' with actual path to Flow's logo.
st.sidebar.markdown("# 🎓 Flow Tutor")
st.sidebar.markdown(
        "## About Flow Tutor 🎓\nFlow Tutor helps you understand blockchains by generating Flow blockchain contracts in plain English with AI. It's perfect for learners and developers who are new to blockchain development!"
    )

st.sidebar.markdown('<a href="https://github.com/Ahmet-Dedeler/Flow-Tutor">The project is on GitHub!<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="30" height="30"></a>', unsafe_allow_html=True)
#also on devpost
st.sidebar.markdown('<a href="https://devpost.com/software/flow-tutor">Also Live on Devpost!  <img src="https://th.bing.com/th/id/R.3f5dc31bb6bd00815d9ac8d7d398610b?rik=KHeQS%2flue7ri3g&pid=ImgRaw&r=0" alt="Devpost" width="35" height="30"></a>', unsafe_allow_html=True)

st.title("Generate a Flow Smart Contract in a Minute! ⏰")
st.caption("A tool that helps you generate and understand Flow blockchain smart contracts. Simply describe your requirements in English! 🌊")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

user_prompt = st.text_area('Describe your contract requirements in plain English here. Example: "I want a contract that transfers 5 tokens from Alice to Bob."', height=5)

if st.button("Generate Contract"):
    message_placeholder = st.empty()
    loading_message = st.empty()
    loading_message.markdown("Generating contract... with the help of AI! 🔥🤖")
    try:
        user_prompt = "You are a Flow blockchain smart contract writer. Your goal is to write a Flow blockchain smart contract based on the user's requirements and also explain why and how it works. Use MarkDown format, surrounding the code part within a code box as per Markdown format (the code is in Cadence langauge, so can specify that to markdown). After you give the whole code for their specification, explain the code as a Flow Tutor, explaining important steps. ALso breakdown the whole explanationt to parts using markdown. The user described their requirements as follows: ```" + user_prompt + "```"
        response = chat.send_message(user_prompt)
        loading_message.empty()
        message_placeholder.markdown(response.text)
    except genai.types.generation_types.BlockedPromptException as e:
        st.exception(e)
    except Exception as e:
        st.exception(e)
